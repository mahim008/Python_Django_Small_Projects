def fahrenhite(temparature):
    return temparature*9/5+32

celcius = []

print("Enter 5 celcius temparature : ")

for _ in range(5):
    temp = float(input())
    celcius.append(temp)
    
fahrenhite_list = []
for temparature in celcius:
    fahrenhite_list.append(fahrenhite(temparature))

print(f"Celcius : {celcius}")  
print(f"Fahrenhite : {fahrenhite_list}")
    