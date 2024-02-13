weight=int(input("Enter your weight in kilograms:"))
height=float(input("Enter your height in centimeters:"))
bmi= weight/(height** 2)

if bmi<18.5:
    print("Underweight")
elif 18.5<= bmi < 25:
    print("Normal weight")
elif 25 <= bmi < 29.9:
    print("Overweight")
else:
    print("Obese")



