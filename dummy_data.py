from faker import Faker
fake = Faker()

fake.first_name()
fake.last_name()
#fake.birthdate()
fake.email()
fake.password()
fake.phone_number()

for _ in range(10):
  print(fake.first_name(), fake.last_name(),fake.email(),
        fake.password(),fake.phone_number())

