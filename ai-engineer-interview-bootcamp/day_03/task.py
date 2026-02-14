full_name = "Harry Potter"
name_parts = full_name.split(" ")
print("First name:", name_parts[0])
print("Last name:", name_parts[1])

f_name= "Dilrabo Khidirova Rasuljonqizi"
parts = f_name.split(" ")
print("First name:", parts[0])
print("Last name:", parts[1])
print("Father's name:", parts[2])

words = ["Dilrabo" ,"is", "a", "Principal", "AI", "Engineer", "in", "Google", "!"]
real = " ".join(words) 
print(real)

parts = ["998", "90", "561", "60", "60"]
result = "-".join(parts)
print(result)

text = "I love O'zbekiston"
clean = text.replace("O'zbekiston", "Canada")
print(clean)

# strip() 
wow = "  dedmk"
truely = wow.strip()
print(truely)
email = "  user@hmb.com "
cl = email.strip()
print(cl)

print("="*60)
print("EMAIL PARSER - Understand Email Addresses")
print("="*60)

def parse_email(email):
    """
    Break email into parts

    Example: user@gmail.com
    username: user
    domain: gmail.com
    company gmail
    """
    # Step 1 Split by @ to get username and domain
    parts = email.split("@")
    if len(parts) != 2:
        return "Invalid email! (needs exactly @ one!)"

    username = parts[0]
    domain = parts[1]

    # Step 2 Split domain to get company name
    domain_parts = domain.split(".")
    company = domain_parts[0]

    # Step 3: Display results
    print(f"\nEmail: {email}")
    print(f" Username: {username}")
    print(f" Domain: {domain}")
    print(f" Company: {company}")

user_email = input("Enter your email: ")
parse_email(user_email.strip())






