class student:
  id=''
  name=''
  cg=''

abid=student()
abid.id= int(input("Your ID: "))
abid.name=input("Enter your Name: ")
abid.cg=float(input("Enter your CGPA: "))
if abid.cg<=1.00:
  print("Grade is D")
  print("Status: Very Bad")
  print("তোমার জীবনটাই লস")

elif abid.cg<=2.00:
  print("Grade is C")
  print("Status: Bad")
elif abid.cg<=3.00:
  print("Grade is B")
  print("Status: Good")
else:
  print("Grade is A")
  print("Status: Very Good")






