from faker import Faker
import pandas as pd
import numpy as np
import csv 
import datetime
from time import time

fake = Faker()

# this function creates the dummy data for the database
def dummy_data(x,headers):
    with open('Raw_data.csv','wt') as csvFile:
              writer = csv.DictWriter(csvFile,fieldnames=headers)
              writer.writeheader()
              #for statement use to populate the the database by x amount into a lis
              for i in range(0,x):
                  writer.writerow({
                      'User ID':fake.random_digit(0-499999),
                      'User Name':fake.profile()['username'],
                      'Full Name':fake.profile()['name'],
                      'Gender':fake.profile()['sex'],
                      'Date of Birth':fake.date_of_birth(minimum_age=18, maximum_age=80),
                      'Password':fake.password(length=8),
                      'Email':fake.free_email(),
                      'Phone Number':fake.numerify('###-###-####'),
                      'Profile ID':fake.bothify(text='PR?-######'),
                      'Profile Picture':fake.file_name(category='image',extension=('png')),
                      'Nationality':fake.country(),
                      'User Bio':fake.text(max_nb_chars=20)
              })
if __name__ == '__main__':
    start=time()
    headers = ["User ID", "User Name", "Full Name", "Gender", "Date of Birth", "Password",
               "Email", "Phone Number", "Profile ID","Profile Picture", "Nationality", "User Bio"]
    dummy_data(10,headers)
    elapsed=time() - start
    print('created csv file time: {}'.format(elapsed))
   