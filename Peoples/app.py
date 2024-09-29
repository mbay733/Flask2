"""
С помощью библиотеки faker необходимо создать три файла:
1. humans.txt - ФИО (hint -> .name(), разделитель запятая)
2. names.txt - Имена (hint -> .first_name())
3. users.txt - Профиль (hint -> .simple_profile(), разделитель точка с запятой)

Создать по 10 строк в каждом файле.
"""
import sys
from flask import Flask, abort, render_template
from faker import Faker

app = Flask(__name__)
fake = Faker("ru_RU")


def create_files() -> None:
    """ Function to create three txt files."""
    with open("./files/humans.txt", 'w', encoding="utf-8") as humans_f:
        for _ in range(10):
            # str -> list -> *list -> str,str,str
            print(*fake.name().split(), sep=',', file=humans_f)

    with open("./files/names.txt", 'w', encoding="utf-8") as names_f:
        for _ in range(10):
            print(fake.first_name(), sep=',', file=names_f)

    with open("./files/users.txt", 'w', encoding="utf-8") as users_f:
        for _ in range(10):
            print(*fake.simple_profile().values(), sep=';', file=users_f)        
    

@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/names")
def get_names():
    names = list()
    with open("./files/names.txt", encoding="utf-8") as f:
        for raw_line in f:
            names.append(raw_line.strip())
    return render_template("names.html", people_names=names)  # {"people_names": names}


@app.route('/table')
def get_table():
    datas = []
    with open('./files/humans.txt', encoding='utf-8') as f:
        keys = ('surname', 'name', 'middle_name')
        for raw_line in f:
            data = raw_line.strip().split(',')       
            person = dict(zip(keys, data))
            datas.append(person)
    return render_template('table.html', people_datas=datas)


@app.route('/users')
def get_users_list():
    datas = []
    with open('./files/users.txt', encoding='utf-8') as f:
        keys = ('login', 'fio', 'sex', 'address', 'email', 'birth_date')
        for raw_line in f:
            data = raw_line.strip().split(';')
            datas.append(dict(zip(keys, data)))
        
    return render_template('users_list.html', users_datas=datas)


@app.route("/users/<login>")
def get_user_info(login: str):
    element = None
    with open('./files/users.txt', encoding='utf-8') as f:
        for raw_line in f:
            data = raw_line.strip().split(';')
            if data[0] == login:
                fio = data[1].split()
                surname = fio[0]
                name = fio[2]
                middle_name = fio[1]
                birth_date = data[5].split('-')     # делаю красивую дату
                birth_date.reverse()                # делаю красивую дату
                birth_date = '.'.join(birth_date)   # делаю красивую дату
                element = {
                    'login': data[0], 'surname': surname,
                    'name': name, 'middle_name': middle_name,
                    'birth_date': birth_date, 'email': data[4],
                    'phone': fake.phone_number()
                     }
                break
    if element is None:
        abort(404)
    return render_template('user_info.html', user_info=element)


if __name__ == '__main__':
    # sys.argv[0] - это имя файла, остальные аргументы - это параметры запуска файла
    if len(sys.argv) > 1 and sys.argv[1] == "--files":
        create_files()
    app.run(debug=True)