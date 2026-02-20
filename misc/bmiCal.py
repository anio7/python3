weight = 85
height = 1.85

bmi = weight / (height ** 2)

# Write your code below 👇
if bmi < 18.5:
    print("underweight")
elif 25 > bmi >= 18.5:
    print("normal weight")
else: 
    print("overweight")