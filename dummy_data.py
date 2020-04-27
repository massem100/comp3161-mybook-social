from faker import Faker
fake = Faker()

fake.uuid()
fake.first_name()
fake.last_name()
#fake.birthdate()
fake.email()
fake.password()
fake.phoneNumberFormat()

for _ in range(10):
  print(fake.uuid(),fake.first_name(), fake.last_name(),fake.email(),
        fake.password(),fake.phoneNumberFormat())

