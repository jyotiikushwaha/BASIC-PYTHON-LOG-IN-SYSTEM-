username="jyoti"
password=12345
numofattempt=3
print(f"You have{numofattempt}attempts")

for i in range(1,4):
    un=input("Enter your name: ")
    pas=int(input("Enter your password"))

    if(un==username)and(pas==password):
        print("YOU LOGGED IN SUCCESSFULLY")
        break
    else:
        numofattempt=3-i
        if(numofattempt>0):
            print(f"Wrong details {numofattempt} attempts left")
           
        
else:
    print("You have reached your limits")
