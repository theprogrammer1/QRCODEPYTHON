email = input("What is your email address?: ").strip() # a = "     jkhjlh    "   => jkhjlh



user_name = email[:email.index("@")]



domain_name = email[email.index("@")+1:]


output = "your username is '{}' and your domain name is '{}'".format(user_name,domain_name)


print(output)
