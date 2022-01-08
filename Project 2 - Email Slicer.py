# Email slicer

# Get user email address

email = input("Enter your email address: ").strip() #strip() will remove any spaces in email


# Slice out user name

user = email[:email.index("@")]


# Slice out domain name

domain = email[email.index("@")+1:]


# Displaying message

message = "Your Email address is {}\nYour email user name is {}\nYour email domain name is {}"
output = message.format(email, user, domain)

print(output)


# Format Shortcut

message = "Your Email address is {}\nYour email user name is {}\nYour email domain name is {}".format(email, user, domain)

print(message)
