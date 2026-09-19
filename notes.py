Amount =int(input("Enter the amount for withdrawal: "))
note_1 = Amount //500
note_2 = (Amount % 500) // 200
note_3 = ((Amount % 500) % 200) // 100
note_4 = (((Amount % 500) % 200) % 100) // 50
print("The number of 500 Ksh notes is:", note_1)
print("The number of 200 Ksh notes is:", note_2)
print("The number of 100 Ksh notes is:", note_3)
print("The number of 50 Ksh notes is:", note_4)