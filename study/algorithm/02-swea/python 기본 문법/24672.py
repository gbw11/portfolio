mail = input()
idx = mail.find("@")

if idx == -1:
    print("Invalid email")

else:
    print(mail[idx+1:])
