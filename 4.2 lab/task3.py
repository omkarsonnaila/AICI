#write a python function that extract domain name from email adddress
def extract_domain(email):
    return email.split('@')[-1]

# Example usage
emails = [
    "alice@example.com",
    "bob@gmail.com",
    "charlie@university.edu"
]

for email in emails:
    print(f"Domain of {email}: {extract_domain(email)}")