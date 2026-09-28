username="jyoti"
password="12345"
num_of_attempt=3
print(f"You have {num_of_attempt} attempts")

for i in range(1,4):
    un=input("Enter your name: ").strip()
    pas=input("Enter your password: ").strip()
    if((un==username)and(pas==password)):
        print("YOU LOGGED IN SUCCESSFULLY")
        break
    else:
        num_of_attempt=3-i
        if(num_of_attempt>0):
            print(f"Wrong details {num_of_attempt} attempts left")
                 
else:
    print("You have reached your limits")
