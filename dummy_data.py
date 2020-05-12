from faker import Faker
import pandas as pd
import numpy as np
import csv 
import datetime
from time import time

fake = Faker()
  
# this function creates the dummy data for the csv file Raw_data
def dummy_data(x,headers):
    with open('userTable.csv','wt') as csvFile:
              writer = csv.DictWriter(csvFile,fieldnames=headers)
              writer.writeheader()
              #for statement use to populate the the csv file by x amount into a list
              #to represent data that would be in reach row 
              p=('profile.png')
              for i in range(0,x):
                  writer.writerow({
                      'userid':fake.random_int(min=1, max=500000),
                      'username':fake.profile()['username'],
                      'f_name':fake.first_name(),
                      'l_name':fake.last_name(),
                      'gender':fake.profile()['sex'],
                      'date_of_birth':fake.date_of_birth(minimum_age=18, maximum_age=80),
                      'user_password':fake.password(length=8)
              })
if __name__ == '__main__':
    start=time()
    headers = ["userid", "username", "f_name","l_name", "gender", 
               "date_of_birth", "user_password"]
    dummy_data(500000,headers)
    elapsed=time() - start
    print('created csv file time: {}'.format(elapsed))
   