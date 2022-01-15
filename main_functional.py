import random

def generate_phone_number(Prefix_number,q):
    phonebook_arr=[]
    final=""
    num_arr=[]
    for total in range(0,q):
        for num in range(0,7):
            n=random.randint(0,9)
            num_arr.append(n)
       
        if num == 6:
            for j in num_arr:
                final=final+str(j)  
            phonebook_arr.append(random.choice(Prefix_number)+final)
            num_arr.clear()
            final=""
            
    return phonebook_arr

phonebook= generate_phone_number(Prefix_number=["0915","0912","0910"],quantity=1500)
for phone_number in phonebook:
    print (phone_number)
