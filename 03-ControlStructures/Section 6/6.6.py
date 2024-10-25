###
# Program that calculates the parking fee based on the number of hours the car was parked
#
parking_hours = int(input("Enter how many hours car was parked: "))

if parking_hours> 6 :
    print("20 PLN")
elif parking_hours >= 3: 
    print("15 PLN")
elif parking_hours >=1:
    print("5 PLN")
else:
    print("Invalid input")