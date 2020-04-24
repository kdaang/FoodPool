import os


def main():
    os.system('python3 clear_migrations.py')
    os.system('python3 make_migrations.py')
    os.system('python3 manage.py migrate')

    print('~~SETUP COMPLETE~~')


if __name__ == '__main__':
    main()
