from faker import Faker
fake = Faker()

fake.first_name()
fake.last_name()
fake.address()


for _ in range(10):
  print(fake.first_name(), fake.last_name())

