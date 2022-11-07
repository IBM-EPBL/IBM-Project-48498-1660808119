import random

#Assigning random temperature value to a variable s in celsius

s=random.uniform(22.0,60.0)
print ("Temperature is",s)
if (s>40):
    print ("Alarm is on since the temperature is above 40 celcius")
else:
    print ("Alarm is off since the temperature is below 40 celcius")

#Assigning random humidity value to a variable k in percentage

k=random.uniform(40,100)
print ("Humidity is",k)
if (k>45):
    print ("Alarm is on since the humidity is above 45%")
else:
    print ("Alarm is off since the humidity is below 45%")