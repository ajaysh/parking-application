import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','parking_project.settings')

import django

django.setup()
import random
from parking_reservation.models import Parking,SlotDetail

from faker import Faker

fakegen = Faker()

def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''
    bulding_number_list = random.sample(range(100), N)
    direction = ['North','South','East','West']
    for entry in range(N):

        # Create Fake Data for entry
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_locality = fakegen.street_suffix()
        faker_lane = random.choice(direction) +':'+str(bulding_number_list[entry])
        faker_slot_name =random.randint(1,101)

        # Create new User Entry
        parking = Parking.objects.get_or_create(locality = fake_locality,lane=faker_lane, slot_name=faker_slot_name)[0]
        parking.save()
        for i in range(5):
            faker_start_date = fakegen.future_date(end_date="+30d", tzinfo=None)
            faker_end_date = fakegen.date_time_between(start_date=faker_start_date, end_date="+1d", tzinfo=None)
            faker_reserved = fakegen.boolean(chance_of_getting_true=50)
            slotDetails = SlotDetail.objects.get_or_create(slot=parking,start_date=faker_start_date,
                                                            end_date=faker_end_date ,reserved=faker_reserved)[0]
            slotDetails.save()


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')
