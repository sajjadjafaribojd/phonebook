import random

def generate_phone_number(Prefix_number,q):
    phonebook_arr=[]
    final=""
    num_arr=[]
    for total in range(0,q):
        for num in range(0,7):
            n=random.randint(0,9)
            num_arr.append(n)
            final=final+str(n)  
        if num == 6:
            phonebook_arr.append(random.choice(Prefix_number)+final)
            final=""
    return phonebook_arr


#Inital value
Prefix_number=["0915","0912","0910"]
quantity=1500

phonebook= generate_phone_number(Prefix_number,quantity)
for phone_number in phonebook:
    print (phone_number)
