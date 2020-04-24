import os


def main():
    os.system('python3 manage.py makemigrations')
    os.system('python3 manage.py makemigrations core')
    os.system('python3 manage.py makemigrations authentication')
    os.system('python3 manage.py makemigrations users')
    os.system('python3 manage.py makemigrations menus')

    print('~~MAKEMIGRATIONS COMPLETE~~')


if __name__ == '__main__':
    main()