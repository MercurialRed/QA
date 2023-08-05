from Python_autotests.data.data import Person
from faker import Faker

faker_ = Faker('uk_UA')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_.first_name() + " " + faker_.last_name(),
        email=faker_.email(),
        current_address=faker_.address(),
        permanent_address=faker_.address(),
    )
