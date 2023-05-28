import os
import django
from faker import Faker
from model_bakery import baker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "new_project.settings")
django.setup()


def generate_fake_data():
    fake = Faker()

    # Generate fake data using Faker and create objects using Model Bakery
    for _ in range(1000):  # Generate 10 instances of fake data
        name = fake.name()
        email = fake.email()
        message = fake.phone_number()

        # Create an object using Model Bakery
        baker.make('news_app.Contact', name=name, email=email, message=message)


if __name__ == '__main__':
    generate_fake_data()
