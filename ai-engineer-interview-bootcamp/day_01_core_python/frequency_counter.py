
customers = [
    {"name": "Ali", "age": 25, "email": "ali@test.com", "country": "UZ"},
    {"name": "Bob", "age": None, "email": "invalid", "country": "US"},
    {"name": "Sara", "age": 30, "email": "sara@test.com", "country": None},
    {"name": "John", "age": -5, "email": "john@test.com", "country": "UK"},
    {"name": "", "age": 28, "email": "empty@test.com", "country": "UZ"}
]

# Your tasks:
# 1. Remove records with missing or invalid data
# 2. Count how many customers per country (valid records only)
# 3. Return average age (excluding invalid ages like None or negative)

# ==============================
# STEP 1 VALIDATE AND FILTER
# ==============================

valid_customers = []
for customer in customers:
    # Extract each field
    name = customer.get("name")
    age = customer.get("age")
    email = customer.get("email")
    country = customer.get("country")

    # RULES
    # First rule name must exist and not empty
    if not name or name == "":
        continue

    # Second rule age must exist and must be positive
    if age is None or age <= 0:
        continue

    # Third rule email must exist and contain @
    if not email or "@" not in email:
        continue

    # Forth rule country must exist and not be None
    if not country or country is None:
        continue

    # if we reach here customer is valid
    valid_customers.append(customer)

print("Valid customers:", valid_customers)

# ==================================
# STEP 2 Count CUSTOMER PER COUNTRY
# ==================================

count_customer = {}
for customer in valid_customers:
    country = customer.get("country")
    count_customer[country] = count_customer.get(country, 0) + 1
print("Customer per country:", count_customer)

# ===============================
# STEP 3 CALCULATE AVERAGE AGE
# ===============================

valid_ages = [customer.get("age") for customer in valid_customers]


# Calculate average age
if len(valid_ages) > 0:
    average_age = sum(valid_ages) / len(valid_ages)
    print(f"Average age: {average_age:.2f}")
else:
    print("No valid ages to calculate average")