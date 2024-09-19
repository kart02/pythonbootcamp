userAge=int(input("Enter your age: "))
gender=input("Enter your Gender: ")
if(userAge>17 and gender=="Female"):
    print("You are eligible fr govt.jobs")
elif(userAge>17 and gender=="Male"):
    print("You are eligible for pvt.jobs")
else:
    print("You are not eligible for any jobs")
