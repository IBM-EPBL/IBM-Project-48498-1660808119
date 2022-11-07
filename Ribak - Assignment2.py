import random

#Assigning random temperature value to a variable m in celsius

m=random.uniform(22.0,60.0)
print ("Temperature is",m)
if (m>25):
    print ("Alarm is on since the temperature is above 25 celcius")
else:
    print ("Alarm is off since the temperature is below 25 celcius")

#Assigning random humidity value to a variable r in percentage

r=random.uniform(40,100)
print ("Humidity is",r)
if (r>40):
    print ("Alarm is on since the humidity is above 40%")
else:
    print ("Alarm is off since the humidity is below 40%")