#!/usr/bin/env python3

#name = input("What is your name? : ")
#birthdate = input("what is your birthdate? : ")
#age = int(input("how old are you? : "))
#
#print(f"{name} was born on {birthdate}")
#print(f"Half of your age is {age /2}")

# BMI = (weight in kg / height in meters squared)
# Unoeruak version: BMI * 703

import os

stage = os.environ["STAGE"].upper()

output = f"we are running in {stage}"

if stage.starswith("PROD"):
    output = "DNAGER" + output

print(output)
