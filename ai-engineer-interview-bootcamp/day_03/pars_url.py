# Parse a URL into parts
url = "https://www.example.com/products/shoes?color=red&size=10"

# Your task: Extract
# - Protocol: https
# - Domain: www.example.com
# - Path: /products/shoes
# - Parameters: color=red&size=10

# Hint: Use split() multiple times
def parse_url(url):
    # step 1
    pro_split = url.split("://")
    protocol = pro_split[0]
    rest = pro_split[1]

    # step 2
    if "?" in rest:
        main_part, params = rest.split("?", 1)
    else:
        main_part = rest
        params = None

    # step 3
    parts = main_part.split("/", 1)
    domain = parts[0]
    path = "/" + parts[1] if len(parts) > 1 else "/"

    return {
        "Proctocol": protocol,
        "Domain": domain,
        "Path": path,
        "Parameters": params
    }
result = parse_url(url)
print(result)