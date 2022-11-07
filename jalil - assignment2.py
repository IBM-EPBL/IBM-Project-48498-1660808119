import random

#Assigning random temperature value to a variable a in celsius

a=random.uniform(22.0,60.0)
print ("Temperature is",a)
if (a>30):
    print ("Alarm is on since the temperature is above 30 celcius")
else:
    print ("Alarm is off since the temperature is below 30 celcius")

#Assigning random humidity value to a variable b in percentage

b=random.uniform(40,100)
print ("Humidity is",b)
if (b>43):
    print ("Alarm is on since the humidity is above 43%")
else:
    print ("Alarm is off since the humidity is below 43%")