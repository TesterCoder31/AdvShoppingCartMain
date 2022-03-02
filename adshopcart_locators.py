from faker import Faker

fake = Faker(locale='en_CA')
advantage_url = 'https://advantageonlineshopping.com/#/'
advantage_username = fake.first_name()
advantage_email = fake.email()
advantage_password = fake.password()
advantage_first_name = fake.first_name()
advantage_last_name = fake.last_name()
advantage_full_name = f'{advantage_first_name} {advantage_last_name}'
advantage_phone_number = fake.phone_number()
advantage_city = fake.city()
advantage_address = fake.street_address()
advantage_state = fake.country_code()
advantage_postal_code = fake.postcode()



