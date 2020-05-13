from faker import Faker
import pandas as pd
import numpy as np
import csv 
import datetime
from time import time

fake = Faker()

# this function creates the dummy data for the csv file Raw_data
def dummy_data(x,headers):
    with open('userInfoTable.csv','wt') as csvFile:
              writer = csv.DictWriter(csvFile,fieldnames=headers)
              writer.writeheader()
              #for statement use to populate the the csv file by x amount into a list
              #to represent data that would be in reach row 
              p=('profile.png')
              count=0
              for i in range(0,x):
                  count=count+1
                  writer.writerow({
                      #'userid':fake.random_int(min=1, max=500000),
                      'userid':count,
                      'email':fake.free_email(),
                      'phone_num':fake.numerify('###-###-####')
              })
if __name__ == '__main__':
    start=time()
    headers = ["userid","email", "phone_num",]
    dummy_data(500000,headers)
    elapsed=time() - start
    print('created csv file time: {}'.format(elapsed))
   
