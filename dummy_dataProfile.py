from faker import Faker
import pandas as pd
import numpy as np
import csv 
import datetime
from time import time

fake = Faker()
  
# this function creates the dummy data for the csv file Raw_data
def dummy_data(x,headers):
    with open('profileTable.csv','wt') as csvFile:
              writer = csv.DictWriter(csvFile,fieldnames=headers)
              writer.writeheader()
              #for statement use to populate the the csv file by x amount into a list
              #to represent data that would be in reach row 
              p=('profile.png')
              count=0
              for i in range(0,x):
                  count=count+1
                  writer.writerow({
                      'profile_id':count,
                      'userid':count,
                      'profile_photo':p,
                      'nationality':fake.country(),
                      'user_bio':fake.text(max_nb_chars=20)
              })
if __name__ == '__main__':
    start=time()
    headers = ["profile_id","userid","profile_photo", "nationality", "user_bio"]
    dummy_data(500000,headers)
    elapsed=time() - start
    print('created csv file time: {}'.format(elapsed))
   
   