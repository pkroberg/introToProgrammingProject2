#Project 2C

#Income Tax Calculator

#Programmer: Oberg, Parker

#Course: CSC1019-FBN

#constants
taxRate = 0.15 #average USA tax rate
standardDeduction = 14600 #standard deduction for a single or married filing seperately
deductionPerDependent = 2000

#input
grossIncome = float(input("Enter your gross income: $"))
numDependents = int(input("Enter the number of dependents you have: "))

#calculations
netIncome = grossIncome - standardDeduction - (numDependents * deductionPerDependent)
incomeTax = netIncome * taxRate

#output
print("Based on the average US tax rate and standard deduction, your income tax is: $", format(incomeTax, ".2f"))