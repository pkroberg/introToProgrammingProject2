#Project 2B

#Video Rental Calculator

#Programmer: Oberg, Parker

#Course: CSC1019-FBN


#constants
newVideoPrice = 3.00
oldVideoPrice = 2.00

#input
newVideoCount = int(input("Enter the number of NEW videos rented: "))
oldVideoCount = int(input("Enter the number of OLD videos rented: "))

#processing
totalCost = (newVideoCount * newVideoPrice) + (oldVideoCount * oldVideoPrice)

#output
print("The total cost of renting", newVideoCount, "new videos and", oldVideoCount, "old videos is $", format(totalCost, '.2f'))