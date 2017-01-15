#To calculate the amount of tax one would incur depending upon which country you \
#are ordering from and which province you belong to(if it applies).

#Getting user input.
userInputCountry = input("Which country are you ordering from? ").upper()
userInputOrder = float(input("What is your orderTotal? $"))

#Defining variables for tax purposes.
orderTotal = 0
generalSalesTax = 0.05
provincialSalesTax = 0.06
harmonizedSalesTax = 0.13

#if user is from Canada and we need to determine which province they are ordering from.
#as different taxes apply depending on the province.
#any other country other than CANADA, there is no tax.
if userInputCountry == "CANADA" :
	userInputProvince = input("Which province of CANADA do you belong to? ").upper()
	if userInputProvince.upper() == "ALBERTA" :
		orderTotal = userInputOrder + (generalSalesTax*userInputOrder)
		print("The total amount you will be charged is $%.2f" %orderTotal)
	if userInputProvince.upper() in ["ONTARIO", "NEW BRUNSWICK", "NOVA SCOTIA"] :
		orderTotal = userInputOrder + (harmonizedSalesTax*userInputOrder)
		print("The total amount you will be charged is $%.2f" %orderTotal)
	if userInputProvince.upper() not in ["ALBERTA", "ONTARIO", "NEW BRUNSWICK", "NOVA SCOTIA"] :
		orderTotal = userInputOrder + (provincialSalesTax*userInputOrder) + \
			(generalSalesTax*userInputOrder)
		print("The total amount you will be charged is $%.2f" %orderTotal)
else:
	print("The total amount you will be charged is $%.2f" %userInputOrder)
