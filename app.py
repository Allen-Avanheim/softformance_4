from os import system


def start_server():
    system('python manage.py runserver')


if __name__ == "__main__":
    start_server()
