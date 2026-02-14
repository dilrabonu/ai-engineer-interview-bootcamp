# Parse a full name into parts
full_name = "Dr. John Michael Smith Jr."

# Your task: Extract
# - Title: Dr.
# - First name: John
# - Middle name: Michael
# - Last name: Smith
# - Suffix: Jr.

# Hint: Use split() and strip()
def parse_name(full_name):
    parts = full_name.strip().split()

    title = parts[0]
    first_name = parts[1]
    middle_name = parts[2]
    last_name = parts[3]
    suffix = parts[4]
    return {
        "Title": title,
        "First name": first_name,
        "Middle name": middle_name,
        "Last name": last_name,
        "Suffix": suffix
    }

result = parse_name(full_name)
print(result)

# Second variant much more prestigious
def parse_name(full_name):
    parts = full_name.strip().split()

    title = None
    suffix = None

    # Detect title
    if parts[0].endswith("."):
        title = parts.pop(0)

    if parts[-1].endswith("."):
        suffix = parts.pop()

    first_name = parts[0]
    last_name = parts[-1]
    middle_name = " ".join(parts[1:-1]) if len(parts) > 2 else None

    return {
        "Title": title,
        "First name": first_name,
        "Middle name": middle_name,
        "Last name": last_name,
        "Suffix": suffix
    }
result = parse_name(full_name)
print(result)