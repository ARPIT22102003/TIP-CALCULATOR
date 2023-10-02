#tip calculator
print("Enter the bill:")


bill = float(input())    #taking input of the total bill

print("Enter the occupation type:")

occupation_type= str(input())  #taking input of the occupation to findout the tip percent to be charged

#types
if(occupation_type == 'Restraunts' ):
    tip_percent = 15


elif(occupation_type == 'Food delivery'):
    tip_percent = 15


elif(occupation_type == 'Hotel service'):
    tip_percent = 15


elif(occupation_type == 'Driver'):
    tip_percent = 10


elif(occupation_type == 'Dressing Parlour'):
    tip_percent = 10


elif(occupation_type == 'Home service'):
    tip_percent = 5


else:
    tip_percent = 0


tip = (tip_percent/100)*bill

total_bill = bill + tip

print("Bill "+ str(bill))

print("Tip Percent " + str(tip_percent))

print("Total Bill "+str(total_bill))