import os


def main():
    os.system('rm -rf foodpool/v1/authentication/migrations/')
    os.system('rm -rf foodpool/v1/core/migrations/')
    os.system('rm -rf foodpool/v1/menus/migrations/')
    os.system('rm -rf foodpool/v1/orderes/migrations/')
    os.system('rm -rf foodpool/v1/users/migrations/')
    os.system('rm db.sqlite3')

    print('~~CLEARED MIGRATION FILES~~')


if __name__ == '__main__':
    main()
