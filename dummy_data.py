from faker import Faker
fake = Faker()

fake.alphaNumeric()
fake.first_name()
fake.last_name()
#fake.birthdate()
fake.email()
fake.password()
fake.phoneNumberFormat()

for _ in range(10):
  print(fake.alphaNumeric(),fake.first_name(), fake.last_name(),fake.email(),
        fake.password(),fake.phoneNumberFormat())

