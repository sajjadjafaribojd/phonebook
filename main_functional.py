import random

def generate_phone_number(final,Prefix_number,num_arr):
    for total in range(0,500):
        for num in range(0,7):
            n=random.randint(0,9)
            num_arr.append(n)
       
        if num == 6:
            for j in num_arr:
                final=final+str(j)  
            print (random.choice(Prefix_number)+final+"\n")    
            num_arr.clear()
            final=""
            


generate_phone_number(final="",Prefix_number=["0915","0912","0910"],num_arr=[])

   
