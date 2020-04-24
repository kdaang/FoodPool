import json
import os

from django.core.management import BaseCommand
from django.db import transaction
from django.db.transaction import TransactionManagementError
from django.template.defaultfilters import upper

from foodpool.settings import BASE_DIR
from foodpool.v1.core.models import Calendar
from foodpool.v1.menus.models import MenuGroups, MenuItems, MenuGroupAvailability, MenuOptions, MenuOptionChoices, Menu, \
    Restaurant, RestaurantLocation, RestaurantLocationAvailability


class Command(BaseCommand):
    def handle_exception(self, ex, model):
        print(str(ex))
        msg = "\n\nSomething went wrong saving this model: {}\n{}".format(model, str(ex))
        print(msg)
        raise TransactionManagementError

    @transaction.atomic
    def import_menu_option_choices(self, menu_option_choices, menu_option, max_each):
        for menu_option_choice in menu_option_choices:
            # MenuOptionChoices Model
            try:
                choice, created = MenuOptionChoices.objects.get_or_create(
                    menu_option=menu_option,
                    choice=menu_option_choice.get("name", None),
                    price=menu_option_choice.get("centsPriceModifier", None),
                    minimum=0,
                    maximum=max_each
                )
            except Exception as ex:
                self.handle_exception(ex, "MenuOptionChoices")

    @transaction.atomic
    def import_menu_options(self, menu_options, menu_item):
        for menu_option in menu_options:
            # MenuOptions Model
            try:
                option, created = MenuOptions.objects.get_or_create(
                    menu_item=menu_item,
                    name=menu_option.get("name", None),
                    description=menu_option.get("description", ""),
                    minimum=menu_option.get("minimum", None),
                    maximum=menu_option.get("maximum", None)
                )

            except Exception as ex:
                self.handle_exception(ex, "MenuOptions")

            self.import_menu_option_choices(menu_option.get("options", None), option,
                                            menu_option.get("maximumEach", None))

    @transaction.atomic
    def import_menu_item(self, menu_items, menu_group):
        for menu_item in menu_items:
            # MenuItems Model
            try:
                item, created = MenuItems.objects.get_or_create(
                    name=menu_item.get("name", None),
                    description=menu_item.get("description", None),
                    group=menu_group,
                    price=menu_item.get("centsPrice", None)
                )

            except Exception as ex:
                self.handle_exception(ex, "MenuItems")

            self.import_menu_options(menu_item.get("options", None), item)

    @transaction.atomic
    def import_menu_data(self, menu):
        data_folder = os.path.join(BASE_DIR, 'foodpool', 'resources/scrapped_menu_data')
        for data_file in os.listdir(data_folder):
            with open(os.path.join(data_folder, data_file), encoding='utf-8') as data_file:
                data = json.loads(data_file.read())
                menu_groups = data.get("menuGroups", None)
                for i in range(1, len(menu_groups)):
                    menu_group = menu_groups[i]

                    # MenuGroups model
                    try:
                        group, created = MenuGroups.objects.get_or_create(
                            name=menu_group.get("name", None),
                            menu=menu
                        )

                        time_constraint = menu_group.get("timeConstraint", None)
                        if time_constraint:
                            for weekday in Calendar.WEEKDAYS:
                                availability, created = MenuGroupAvailability.objects.get_or_create(
                                    group=group,
                                    weekday=weekday[0],
                                    startHour=time_constraint.get("startHour", None),
                                    startMinute=time_constraint.get("startMinute", None),
                                    endHour=time_constraint.get("endHour", None),
                                    endMinute=time_constraint.get("endMinute", None)
                                )

                    except Exception as ex:
                        self.handle_exception(ex, "MenuGroups")

                    self.import_menu_item(menu_group.get("menuItems", None), group)

    @transaction.atomic
    def import_restaurant_availability(self, hours, restaurant_location):
        if not hours:
            return

        # RestaurantLocationAvailability Model
        for day, time in hours.items():
            for weekday in Calendar.WEEKDAYS:
                if upper(day) == upper(weekday[1]):
                    curr_weekday = weekday[0]

            start = time[0].get("start", None)
            end = time[0].get("end", None)
            try:
                restaurant_location_availability, created = RestaurantLocationAvailability.objects.get_or_create(
                    restaurant_location=restaurant_location,
                    weekday=curr_weekday,
                    startHour=start.get("hour", None),
                    startMinute=start.get("minute", None),
                    endHour=end.get("hour", None),
                    endMinute=end.get("minute", None)
                )

            except Exception as ex:
                self.handle_exception(ex, "RestaurantLocation")

    def import_restaurant_location(self, location, hours, restaurant):
        if not location:
            return

        # RestaurantLocation Model
        try:
            restaurant_location, created = RestaurantLocation.objects.get_or_create(
                restaurant=restaurant,
                address_1=location.get("address", None),
                latitude=location.get("latitude", None),
                longitude=location.get("longitude", None),
                city=location.get("city", None),
                province=location.get("province", None),
                postal_code=location.get("postalCode", None),
                country=location.get("country", None)
            )

        except Exception as ex:
            self.handle_exception(ex, "RestaurantLocation")

        self.import_restaurant_availability(hours, restaurant_location)

    @transaction.atomic
    def import_restaurant_menu(self):
        data_folder = os.path.join(BASE_DIR, 'foodpool', 'resources/scrapped_restaurant_data')
        for data_file in os.listdir(data_folder):
            with open(os.path.join(data_folder, data_file), encoding='utf-8') as data_file:
                data = json.loads(data_file.read())

                # Menu Model
                try:
                    menu, created = Menu.objects.get_or_create(
                        skip_id=data.get("id", None)
                    )

                except Exception as ex:
                    self.handle_exception(ex, "Menu")

                # Restaurant Model
                try:
                    restaurant, created = Restaurant.objects.get_or_create(
                        name=data.get("name", None),
                        shortName=data.get("shortName", None),
                        menu=menu
                    )

                except Exception as ex:
                    self.handle_exception(ex, "Restaurant")

                self.import_restaurant_location(data.get("location", None), data.get("hours", None),  restaurant)
                self.import_menu_data(menu)


    def handle(self, *args, **options):
        """
                Call the function to import data
                """
        self.import_restaurant_menu()