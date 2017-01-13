orderTotal = 0

userInputCountry = input("Which country are you ordering from? ").upper()
userInputOrder = float(input("What is your orderTotal? $"))

generalsalesTax = 0.05
provincialsalesTax = 0.06
harmonizedsalesTax = 0.13

if userInputCountry == "CANADA" :
	userInputProvince = input("Which province of CANADA do you belong to? ").upper()
	if userInputProvince.upper() == "ALBERTA" :
		orderTotal = userInputOrder + (generalsalesTax*userInputOrder)
		print("The total amount you will be charged is $%.2f" %orderTotal)
	if userInputProvince.upper() in ["ONTARIO", "NEW BRUNSWICK", "NOVA SCOTIA"] :
		orderTotal = userInputOrder + (harmonizedsalesTax*userInputOrder)
		print("The total amount you will be charged is $%.2f" %orderTotal)
	if userInputProvince.upper() not in ["ALBERTA", "ONTARIO", "NEW BRUNSWICK", "NOVA SCOTIA"] :
		orderTotal = userInputOrder + (provincialsalesTax*userInputOrder) + \
			(generalsalesTax*userInputOrder)
		print("The total amount you will be charged is $%.2f" %orderTotal)
else:
	print(" The total amount you will be charged is $%.2f" %userInputOrder)
