def bmi(weight, height):
    return weight / height ** 2

def condition(weight, height):
    con = bmi(weight, height)
    if con < 18.5:
        return "Underweight"
    elif 25 > con >= 18.5:
        return "Normal Weight"
    elif 30 > con >= 25:
        return "Overweight"
    elif con >= 30:
        return "Obesity"


w = float(input("Enter your weight (kg) : "))
h = float(input("Enter your height (meter) : "))
print(f"Your BMI value is : {round(bmi(w, h),2)} with the state : {condition(w,h)}")
