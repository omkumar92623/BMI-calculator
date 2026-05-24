print("This program determines that your weight is in a healthy range for your height or not.")
print("______________________________________________________________________________________\n")
your_height_cm = float(input("enter your height in cm: "))
weight = float(input("enter your weight in kg: "))
height_meter= your_height_cm/100
height= height_meter*height_meter

BMI = weight / height

print(f"your BMI is {BMI:.2f}: ")
if BMI<18.5:
    print("you are underweight")

elif  BMI <=24.9:
    print("you are in healthy weight")

elif BMI <=29.9:
    print("you are over weight")

elif BMI >30:
    print("you are obese ")