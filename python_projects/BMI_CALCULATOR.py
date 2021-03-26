# BMI CALCULATOR

height = float(input("Enter the height in centimeters: "))
weight = float(input("Enter the weight in kg: "))
height = height/100
BMI = weight/(height*height)

print("Your Body Mass Index is: ",BMI)

if (BMI>0):
    if(BMI<=16):
        print("you are severly underweight")
    elif(BMI<=18.5):
        print("You are underweight")
    elif(BMI<=25):
        print("You are Healthy")
    elif(BMI<=30):
        print("You are OverWeight")
    else:
        print("You are severly OverWeight")
else:
    ("Enter valid details")

