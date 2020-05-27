#!/usr/bin/python3
#
#Author: Brian T. Carr
#Website: briancarr.org
#Email: brian@briantcarr.com
#
#Ohm's Law Script
#Use this for your electrical calculations!

print("Welcome to Brian's Ohm's Law Calculator")
print("V=IR\nI=V/R\nR=V/I")
print("Please enter the variable you wish to find")
var_select = input("V = Volatage, I = Current, R = Resistance: ")
var_select = var_select.upper()
if var_select == "V":
    current = float(input("Please enter the current: "))
    resistance = float(input("Please enter the the resistance: "))
    print(" V=IR")
    voltage = float(current * resistance)
    print("The voltage is: " + str(voltage) + "Volts")
elif var_select == "I":
    voltage = float(input("Please enter the voltage: "))
    resistance = float(input("Please enter the resistance: "))
    print(" I=V/R")
    current = float(voltage / resistance)
    print("The currnet is: " + str(current) + "Amperes")
elif var_select == "R":
    voltage = float(input("Please enter the voltage: "))
    current = float(input("Please enter the current: "))
    print(" R=V/I")
    resistance = float(voltage / current)
    print("The resistance is: " + str(resistance) + "ohms")
