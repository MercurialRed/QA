import random
from Python_autotests.data.data import Person
from faker import Faker

faker = Faker('uk_UA')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker.first_name() + " " + faker.last_name(),
        firstname=faker.first_name(),
        lastname=faker.last_name(),
        email=faker.email(),
        age=random.randint(10, 80),
        salary=random.randint(10000, 100000),
        department=faker.job(),
        current_address=faker.address(),
        permanent_address=faker.address(),
    )

def generated_file():
    path = rf'S:\Python Projects\QA\Python_autotests\filetest{random.randint(0,999)}.txt'
    file = open(path, 'w+')
    file.write(f"Test{random.randint(0,999)}")
    file.close()
    return file.name, path