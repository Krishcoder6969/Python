country_code = {'India':'0091',
                'Austraila':'0025',
                'Nepal':'00977'}
print("Country code for India -")
print(country_code.get('India', 'Not found'))
print("Country code for Japan -")
print(country_code.get('japan', 'not found'))