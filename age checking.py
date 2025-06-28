age = int(input("Enter your age: "))
if age <= 12:

age_type = "Child"

elif age <= 19:

age_type = "Teenager"

elif age <= 50:

age_type = "Adult"

else:

age_type = "Old"
print(f"You are categorized as a(n) {age_type}.")