## Hey, Hello! This project is about taking info from users about them and printing the answers they give.

# Ask user for name
name = input("What's your name?\n")


# Ask user for age
age = input("How old are you?\n")


# Ask user for city
city = input("Which city are you form?\n")


# Ask user what they enjoy
interest = input("What do you enjoy most?\n")


# Using Concatination

message = "Hey! Genious! We got you here.\nYour name is " + name +"." + "\nYou are "+ str(age) +" years old.\nYou live in "+ city +".\nYou love "+ interest +".\nThese is all we know about you. Hope you are doing fine."

print(message)


# Using string format

message = "Hey! Genious! We got you here.\nYour name is {}.\nYou are {} years old.\nYou live in {}.\nYou love {}.\nHope you are doing fine!\nFor now, These is all we know about you." 

output = message.format(name, age, city, interest)

print(output)

