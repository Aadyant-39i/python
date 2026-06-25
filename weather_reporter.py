city = input("Enter the city name: ")
temp = float(input("Enter the temperature in Celsius: "))

if temp > 35:
    print("CAUTION: It's a scorching hot day in", city)

if temp > 30:
    print("It's a warm day in", city)

if temp > 25:
    print("It's a pleasant day in", city)
else:
    print("Grab a jacket! It's chilly in", city)

if temp > 35:
    print("Weather: Scorching hot")
elif temp > 30:
    print("Weather: Warm")
elif temp > 25:
    print("Weather: Pleasant")
elif temp > 15:
    print("Weather: Cool and Breezy")
elif temp > 5:
    print("Weather: Very cold")
else:
    print("Weather: Freezing cold, stay warm!")

import datetime
import calendar

now = datetime.datetime.now()
print("City:", city)
print("Time now: ", now)
print(calendar.calendar(now.month)  )