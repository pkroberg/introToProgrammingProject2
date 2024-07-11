#Project 2A

#Weekly Pay Calculator

#Programmer: Oberg, Parker

#Course: CSC1019-FBN


#input
hourlyWage = float(input("Enter your hourly wage: $"))
regularHoursWorked = float(input("Enter the number of regular hours worked: "))
overtimeHoursWorked = float(input("Enter the number of overtime hours worked: "))

#processing
overtimePay = hourlyWage * 1.5 * overtimeHoursWorked
weeklyPay = (hourlyWage * regularHoursWorked) + overtimePay

#output
print("Your weekly pay is: $", weeklyPay)