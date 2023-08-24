import random
from Python_autotests.data.data import Person, Color, Date
from faker import Faker

faker_ua = Faker('uk_UA')
faker_en = Faker('En')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_ua.first_name() + " " + faker_ua.last_name(),
        firstname=faker_ua.first_name(),
        lastname=faker_ua.last_name(),
        email=faker_ua.email(),
        age=random.randint(10, 80),
        salary=random.randint(10000, 100000),
        department=faker_ua.job(),
        current_address=faker_ua.address(),
        permanent_address=faker_ua.address(),
        mobile=faker_ua.msisdn(),
    )

def generated_file():
    path = rf'S:\Python Projects\QA\Python_autotests\filetest{random.randint(0,999)}.txt'
    file = open(path, 'w+')
    file.write(f"Test{random.randint(0,999)}")
    file.close()
    return file.name, path

def generated_color():
    yield Color(
        color_name=["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Violet", "Indigo", "Magenta", "Aqua"]
    )

def generated_date():
    yield Date(
        year="2020",
        month=faker_en.month_name(),
        day=faker_en.day_of_month(),
        time="12:00",
    )