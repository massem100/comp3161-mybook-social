from faker import Faker
fake = Faker()

fake.bothify()
fake.first_name()
fake.last_name()
fake.email()
fake.password()
fake.numerify()
fake.date_of_birth()
fake.random_choices()

for _ in range(5):
  print(fake.bothify(text='??-###'),fake.first_name(), fake.last_name(),fake.email(),
        fake.password(length=8),fake.numerify('###-###-####'),fake.date_of_birth(), 
        fake.random_choices(elements=[('male'),('female')],length=1))

