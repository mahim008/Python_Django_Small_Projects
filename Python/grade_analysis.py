def grade(number):
    avg = sum(number)/len(number)
    if avg>=93:
        return "A+"
    elif 80<=avg<93:
        return "A"
    elif 70<=avg<80:
        return "A-"
    elif 60<=avg<70:
        return "B"
    elif 50<=avg<60:
        return "C"
    elif 40<=avg<50:
        return "D"
    elif avg<40:
        return "F"

print("Enter student's obtained number for 5 subjects : ")
number = []
for i in range(5):
    n = int(input())
    number.append(n)

print(f"\nThe minimum number of the student : {min(number)}")
print(f"\nThe maximum number of the student : {max(number)}")
print(f"\nThe sum total of numbers : {sum(number)}")
print(f"\nThe average number of the student : {sum(number)/len(number)}")
print(f"\nObtained Grade is = {grade(number)}\n")