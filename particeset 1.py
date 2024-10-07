# que 1 
# name = input("enter your name:")
name = "mayank"
print(f"good afternoon,{name}")

# que 2 
letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> '''

print(letter.replace("<|Name|>", "mayank").replace("<|Date|", "24 September 2050"))

# que 3 
# name ="mayank is a good boy and  "
# print(name.find(" "))

# que 4 
name = "ram is a good boy and  "
print(name.replace(" "," "))
print(name)

# que 5 
letter = "dear mayank , \n\t this pytjon is nice.\n Thanks!!!"
print(letter)
