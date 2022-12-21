#!/usr/bin/env python3.9

import time

start_time = time.localtime()
print(f"Time started at {time.strftime('%X', start_time)}")

# wait for user to stop timer
input("press 'Enter' to stop timer")

stop_time = time.localtime()
difference = time.mktime(stop_time) - time.mktime(start_time)

print(f"Timer stopped at {time.strftime('%X', stop_time)}")
print(f"Total time: {difference} seconds")





#name = input("What is your name? : ")
#birthdate = input("what is your birthdate? : ")
#age = int(input("how old are you? : "))
#
#print(f"{name} was born on {birthdate}")
#print(f"Half of your age is {age /2}")

# BMI = (weight in kg / height in meters squared)
# Unoeruak version: BMI * 703

#def gather_info():
#    height = float(input("what is your height? (inches or meter) "))
#    weight = float(input("what is your weight? (pounds or kilograms) ")
#    system = input("Are your measurements in metric or imperial units? ")
#    return (height, weight, system)
#
#def calculate_bmi(height, weight, system='metric'):
#    """
#    Return the Body Mass Index (BMI) for the 
#    given weight, height and measurement system.
#    """
#
#    if system == 'metric':
#        bmi = (weight / (height **2))
#    else:
#        bmi = 703 (weight / (height ** 2))
#    return bmi
#
#while True:
#    height, weight, system = gather_info()
#    if system.startswith('i'):
#        bmi = calculate_bmi(weight, height=height, system=system)
#        print(f"your BMI is { bmi }
#        break
#    elif system.startswith('m'):
#        bmi = calculate_bmi(weight, height=height, system=system)
#        print(f"your BMI is { bmi }
#        break
#    else:
#        print(f"Error: Unknown measurement system. Pl. use imperial or metric.")
#
