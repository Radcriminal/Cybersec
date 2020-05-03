import argparse
import base64

parser = argparse.ArgumentParser(description='create base authentication from usernames and passwords')

parser.add_argument('-p', '--password',
                    dest='one_password',
                    action='store',
                    help='specify one password(only one word)')
parser.add_argument('-P', '--passwords',
                    dest='list_of_passwords',
                    action='store',
                    help='choose a file with a passwords')
parser.add_argument('-l', '--login',
                    dest='one_login',
                    action='store',
                    help='specify one login(only one word)')
parser.add_argument('-L', '--logins',
                    dest='list_of_logins',
                    action='store',
                    help='choose a file with logins')

args = parser.parse_args()

list_of_password = []
list_of_logins = []
list_of_credentials = []


def get_lists():
    if args.one_password:
        list_of_password.append(args.one_password)

    if args.list_of_passwords:
        with open(args.list_of_passwords) as f:
            for i in f:
                list_of_password.append(i)

    if args.one_login:
        list_of_logins.append(args.one_login)

    if args.list_of_logins:
        with open(args.list_of_logins) as f:
            for i in f:
                list_of_logins.append(i)


def create_file_with_credentials():
    for password in list_of_password:
        password = password.strip()
        for login in list_of_logins:
            login = login.strip()
            string_to_convert = login + ':' + password
            e = base64.b64encode(string_to_convert.encode('UTF-8'))
            e = str(e, 'UTF-8')
            list_of_credentials.append(e)


def main():
    get_lists()  # fill lists with data
    create_file_with_credentials()  # start encode credentials
    with open('./credentials.txt', 'w') as f:
        for i in list_of_credentials:
            f.writelines(i + '\n')


if __name__ == "__main__":
    main()
