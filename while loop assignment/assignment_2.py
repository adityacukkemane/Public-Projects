count_25_35 = 0

while True:
    age = int(input("Enter employee age: "))
    if age < 0 or age > 57:
        break
    if 25 <= age <= 35:
        count_25_35 += 1

print(f"Number of employees aged 25 to 35: " ,count_25_35)
