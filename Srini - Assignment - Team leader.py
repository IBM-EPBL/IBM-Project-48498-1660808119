import random

#Assigning random temperature value to a variable c in celsius

c=random.uniform(22.0,60.0)
print ("Temperature is",c)
if (c>41):
    print ("Alarm is on since the temperature is above 41 celcius")
else:
    print ("Alarm is off since the temperature is below 41 celcius")

#Assigning random humidity value to a variable y in percentage

y=random.uniform(40,100)
print ("Humidity is",y)
if (y>50):
    print ("Alarm is on since the humidity is above 50%")
else:
    print ("Alarm is off since the humidity is below 50%")
    