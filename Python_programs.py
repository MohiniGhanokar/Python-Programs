print("\n--------1.Create simple variables------")
name = "Mohini"
age = 20
city = "Khamgaon"
print(name)
print(age)
print(city)
print(f"My name is {name}, I am {age} years old, and I live in {city}.")

print("\n-------2.Different data types---------")
num_int = 10
num_float = 12.5
strvar = "Hello"
boolvar = True
print(num_int, type(num_int))
print(num_float, type(num_float))
print(strvar, type(strvar))
print(boolvar, type(boolvar))

print("\n-----3.Multiple assignments-------")
x, y, z = 5, 10, 15
print(x, y, z)

print("\n-------4.Swapping variables-------")
a, b = 10, 20
print("Before swap:", a, b)
a, b = b, a
print("After swap:", a, b)

print("\n------Without third variable------")
a, b = a + b, a
b = a - b
a = a - b
print("Swap again:", a, b)

print("\n----5.Check valid/invalid variable names------")
_num = 100  # valid
# 2num = 50  # invalid 
# num@data = 30  # invalid
print(_num)




print("\n-----6.User input-----")
name = input("Enter your name: ")
age = input("Enter your age: ")
food = input("Enter your favorite food: ")
print(f"Hello {name}, you are {age} years old and love {food}.")

print("\n-------7.Simple calculator------")
n1, n2 = 10, 3
print("Addition:", n1 + n2)
print("Subtraction:", n1 - n2)
print("Multiplication:", n1 * n2)
print("Division:", n1 / n2)

print("\n----8.Geometry basics-----")
length, width = 5, 3
area_rect = length * width
peri_rect = 2 * (length + width)
print("Rectangle Area:", area_rect)
print("Rectangle Perimeter:", peri_rect)

radius = 7
area_circle = 3.14159 * radius ** 2
circumference = 2 * 3.14159 * radius
print("Circle Area:", area_circle)
print("Circle Circumference:", circumference)

print("\n----- 9.Temperature converter----------")
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")
fahrenheit = 98.6
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit}°F = {celsius}°C")

print("\n---10.Update variable values------")
count = 0
for i in range(5):
    count += 5
    print("Count:", count)



print("\n----11.Salary increment-----")
salary = 20000
new_salary = salary + (salary * 15 / 100)
print("New Salary:", new_salary)

print("\n----12.String operations-----")
sentence = "Python is awesome"
print("Length:", len(sentence))
print("First character:", sentence[0])
print("Last character:", sentence[-1])
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())

print("\n-----13.Shopping bill-----")
p1, p2, p3 = 100, 200, 300
total = p1 + p2 + p3
gst = total * 0.18
final_bill = total + gst
print("Final Bill with GST:", final_bill)

print("\n-----14.Swap three variables------")
a, b, c = 1, 2, 3
a, b, c = b, c, a
print("After circular swap:", a, b, c)

print("\n-----15.Bank balance-----")
balance = 5000
balance -= 1000  # shopping
balance += 2000  # salary
print("Final Balance:", balance)

print("\n----16.Student marksheet-----")
m1, m2, m3, m4, m5 = 78, 85, 90, 67, 80
total = m1 + m2 + m3 + m4 + m5
average = total / 5
percentage = (total / 500) * 100
print("Total:", total, "Average:", average, "Percentage:", percentage)

print("\n-----17.Simple interest----")
P, R, T = 1000, 5, 2
SI = (P * R * T) / 100
print("Simple Interest:", SI)

print("\n-----18.BMI Calculator----")
height = 1.65  # meters
weight = 60  # kg
bmi = weight / (height ** 2)
print("BMI:", bmi)

print("\n-----19.Age in days----")
age_years = 20
age_days = age_years * 365
print("Age in Days:", age_days)

print("\n----20.Currency converter----")
inr = 8300
usd = inr / 83
print(f"{inr} INR = {usd} USD")
