
# import necessary modules
import requests

base_url = 'http://api.openweathermap.org/data/2.5/weather?'
api_key = '02dbadd118823874738c09f7bd3306e5'

print("Welcome to the weather machine!")

while True:
    location = input("\n Enter the city or zipcode to search for the forcast. ")
    if location == "":
        print("Please enter a valid city or zipcode!")
        continue

    else:
        try:
            zip = int(location)
            print("Zip = " + location)
            qstring2 = "appid=" + api_key + "&zip=" + location
            zip_url = base_url + qstring2
            print(zip_url)
            response = requests.get(zip_url)
            print('ZIP:', response.json())

        except:
            city = str(location)
            print("City = " + city)
            qstring1 = "appid=" + api_key + "&q=" + city + ",US"
            city_url = base_url + qstring1
            print(city_url)
            response = requests.get(city_url)
            print('CITY',response.json())

        else:
            response = input("would you like to run it again (y/n)? ")
            if response == "n":
                break

"""