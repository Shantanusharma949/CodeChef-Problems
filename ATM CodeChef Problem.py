#Pooja would like to withdraw X $US from an ATM. The cash machine will only accept the transaction if X is a multiple of 5, and Pooja's account balance has enough cash to perform the withdrawal transaction (including bank charges). For each successful withdrawal the bank charges 0.50 $US. Calculate Pooja's account balance after an attempted transaction.
#EXAMPLE
#1) Input:
#30 120.00

#Output:
#89.50

#2) Input:
#42 120.00

#Output:
#120.00

#3)  Input:
#300 120.00

#Output:
#120.00


X=int(input("Enter how much Pooja would withdraw: "))
TBA=float(input("Total Bank Account of Pooja: "))

if X%5==0 and X<=TBA:
    print("{0:.2f}".format(TBA-(X+0.5)))
else:
    print(TBA)