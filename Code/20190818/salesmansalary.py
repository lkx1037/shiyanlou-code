#!/usr/bin/env python3
sum = 0
basic_salary = 1500
bonus_rate = 200
commission_rate = 0.02
numberofcamera = int(input("Enter the number"))
price = float(input("Enter the price of camera"))
bonus = (bonus_rate * numberofcamera)
commission = (commission_rate * price * numberofcamera)
print("Bonus        ={:6.2f}".format(bonus))
print("Commission    ={:6.2f}".format(commission))
print("Gross salary  ={:6.2f}".format(basic_salary + bonus + commission))

