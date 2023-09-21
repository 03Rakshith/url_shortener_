import pyshorteners

# Create a Shortener object
s = pyshorteners.Shortener()

# Prompt the user for a URL
user_url = input("Enter the URL: ")

# Shorten the URL
shortened_url = s.tinyurl.short(user_url)

# Print the shortened URL
print("Shortened URL:", shortened_url)
