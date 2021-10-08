import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','basic.settings')

import django
django.setup()

# FAKE POP SCRIPTS
import random
from myapp.models import User
from faker import Faker

fake_data = Faker()

def populate(N=5):
    for entry in range(N):
        fake_name = fake_data.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fake_data.email()
        fake_address = fake_data.address()

        user = User.objects.get_or_create(first_name=fake_first_name,
                                last_name=fake_last_name,email=fake_email,address=fake_address)[0]
        user.save()

if __name__ == '__main__':
    print('POPULATING DATABASES...Please Wait')
    populate(5)
    print('COMPLETE')