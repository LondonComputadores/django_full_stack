import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_fscourse.settings')

import django
django.setup()

#FAKE POP SCRIPT
import random
from first_app.models import AccessRecord,Webpage,Topic
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'Games', 'Hackings', 'Data Science']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        #get the topic for the entry
        top = add_topic()

        #create the fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        #create a fake access record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':
    print('populating script!')
    populate(20)
    print('populating complete.')

# dai no terminal depois deste código pronto 1)python populate_first_app.py e depois
# cont... 2) python manage.py runserver e fui ver no admin page
