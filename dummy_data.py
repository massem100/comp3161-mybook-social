from faker import Faker
import pandas as pd
import numpy as np


fake = Faker()

# this function creates the dummy data for the database
def dummy_data(x):
    fake_data={}
    #for statement use to populate the the database by x amount into a list
    for i in range(0,x):
        fake_data[i]={}
        fake_data[i]['User ID']=fake.bothify(text='U?-######')
        fake_data[i]['User Name']=fake.profile()['username']
        fake_data[i]['Full Name']=fake.profile()['name']
        fake_data[i]['Gender']=fake.profile()['sex']
        fake_data[i]['Date of Birth']=fake.date_of_birth(minimum_age=18, maximum_age=80)
        fake_data[i]['Password']=fake.password(length=8)
        fake_data[i]['Email']=fake.free_email()
        fake_data[i]['Phone Number']=fake.numerify('###-###-####')
        fake_data[i]['Profile ID']=fake.bothify(text='PR?-######')
        fake_data[i]['Profile Picture']=fake.file_name(category='image',extension=('png'))
        fake_data[i]['Nationality']=fake.country()
        fake_data[i]['User Bio']=fake.text(max_nb_chars=20)
        
        #fake_data[i]['Post ID']=fake.bothify(text='P?-######')
        #fake_data[i]['Post Date']=fake.date_this_century()
        #fake_data[i]['Post Time']=fake.time()
        #fake_data[i]['Group ID']=fake.bothify(text='G?-######')
        #fake_data[i]['Group Admin']=fake.name()
        #fake_data[i]['Group Name']=fake.bs()
        #fake_data[i]['Creator ID']=fake.bothify(text='C?-#######')
        #fake_data[i]['Date created']=fake.date_this_century()
        #fake_data[i]['Content Editors']=fake.name()
        #fake_data[i]['Permission']=fake.random_choices(elements=[('Private'),('Public')],length=1)
        #fake_data[i]['Group Type']=fake.random_choices(elements=[('Relatives'),('Friends'),('Work')],length=1)
        #fake_data[i]['Comment ID']=fake.bothify(text='CO?-######')
        #fake_data[i]['Comment Content']=fake.text(max_nb_chars=20)
        #fake_data[i]['Time Posted']=fake.time()
        #fake_data[i]['Date Posted']=fake.date_this_century()
        #fake_data[i]['Friend ID']=fake.bothify(text='F?-######')
        #fake_data[i]['Friend Firstname']=fake.first_name()
        #fake_data[i]['Friend Lastname']=fake.last_name()
        #fake_data[i]['Friend Type']=fake.random_choices(elements=[('Relatives'),('Friends'),('Work')],length=1)
        #fake_data[i]['Number of Friends']=fake.random_digit_not_null()
        #fake_data[i]['Friend email']=fake.free_email()
        #fake_data[i]['Pic ID']=fake.bothify(text='PI?-######')
        #fake_data[i]['Picture Description']=fake.text(max_nb_chars=10)
        #fake_data[i]['Picture Name']=fake.file_name(category='image',extension=('png'))
        #fake_data[i]['Date Pic Posted']=fake.date_this_century()
      
    return fake_data

data=dummy_data(2)
#prints out the list into a frame 
print(pd.DataFrame.from_dict(data))

