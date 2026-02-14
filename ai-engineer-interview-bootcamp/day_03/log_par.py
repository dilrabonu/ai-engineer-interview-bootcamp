# Log parser
print("="*70)
print("LOG PARSER - Understand Program Logs")
print("="*70)

logs = """
[2024-12-25 10:30:45] INFO: User logged in: alice
[2024-12-25 10:31:20] WARNING: Slow database query
[2024-12-25 10:32:15] ERROR: Failed to send email
[2024-12-25 10:33:00] INFO: User logged out: bob
[2024-12-25 10:34:30] ERROR: Connection timeout
"""

def parse_log_line(line):
    line = line.strip() # remove spaces from beginning end the end
    if not line:
        return None

    parts = line.split("]") # split 2 ] until here parts[0] - timestamp, parts[1]-rest
    if len(parts) < 2:
        return None

    timestamp = parts[0].replace("[", "") # remove [
    # split data and time 
    timestamp_parts = timestamp.split(" ")
    date = timestamp_parts[0]
    time = timestamp_parts[1]

    # get the rest (level and message)
    rest = parts[1].strip() # remove extra space
    # split rest to level and message
    rest_parts = rest.split(":", 1) # split only on first colon

    level = rest_parts[0]
    message = rest_parts[1] if len(rest_parts) > 1 else ""

    return {
        "date": date,
        "time": time,
        "level": level,
        "message": message
    }

print("\nPARSED LOG ENTRIES:")
print("="*70)

log_lines = logs.split("\n") # split logs into seperate lines
errors = []
warnings = []

for line in log_lines:
    result = parse_log_line(line)
    if result:
        print(f"\nDate: {result['date']}")
        print(f"Time: {result['time']}")
        print(f"Level: {result['level']}")
        print(f"Message: {result['message']}")

        # collect errors and warnings
        if result['level'] == 'ERROR':
            errors.append(result)
        elif result['level'] == 'WARNING':
            warnings.append(result)

# summary report
print("\n" + "="*70)
print("SUMMARY REPORT")
print("="*70)

print(f"\nTotal Errors: {len(errors)}")
for error in errors:
    print(f"  • {error['time']}: {error['message']}")

print(f"\n Total Warnings:{len(warnings)}")
for warning in warnings:
    print(f" • {warning['time']}: {warning['message']}")
