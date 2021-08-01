print("This program let you to understand trailing stop and when to update")

print("initial position is the equity price which you buy the shares")
initialposition = float(input("Enter the value of initial position: "))

print("if you don't have last position start with equity price which you buy the shares")
lastposition = float(input("Enter the value of last position: "))

print("assure your acceptable loss is 15%")

trailingStop = 0
continueProg = "y"

while (continueProg == "y"):
	shareprice = float(input("Enter the current share price: "))
	if (shareprice > lastposition):
		lastposition = shareprice
		trailingStop = lastposition*.85
		print("New position is: " + str(lastposition))
		print("New trailing stop is: " + str(trailingStop))
	if (shareprice < lastposition and shareprice > trailingStop):
		print("New position is: " + str(lastposition))
		print("New trailing stop is: " + str(trailingStop))
	if (shareprice < trailingStop):
		print("sell your shares")
	continueProg = input("Do you want to continue (y/n): ")	