from faker import Faker
import random
import string
class RandomDataUtil:
    def __init__(self):
        self.faker = Faker()

    def get_first_name(self):
        return self.faker.first_name()
    def get_last_name(self):
        return self.faker.last_name()
    def get_email(self):
        return self.faker.email()
    def get_phone(self):
        return self.faker.phone_number()
    def get_address(self):
        return self.faker.address()
    def get_city(self):
        return self.faker.city()
    def get_state(self):
        return self.faker.state()
    def get_zip(self):
        return self.faker.postcode()
    def get_country(self):
        return self.faker.country()
    def get_name(self):
        return self.faker.name()

    def get_age(self):
        return self.faker.date_of_birth()
    def get_gender(self):
        return self.faker.gender()
    def get_birth_date(self):
        return self.faker.date_of_birth()
    def get_password(self):
        return self.faker.password()
    def get_password2(self):
        return self.faker.password()
    def get_random_city(self):
        return self.faker.city()
    def get_random_state(self):
        return self.faker.state()
    def get_random_pin(self):
        return self.faker.phone_number()
    def get_random_address(self):
        return self.faker.address()