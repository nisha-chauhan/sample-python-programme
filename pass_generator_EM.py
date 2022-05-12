import random
Char_choice=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Num_choice=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
Special_chars_choice=['!', '"', '#', '$', '%', '&', '}', '~']
print("WELCOME TO PASWARD GENERATOR\n")

Letters=int(input("How Many Letters You want In Your Passward\n"))
Number=int(input(f"How Many Numbers You want In Your Passward\n"))
Special=int(input(f"How Many Special Character's You want In Your Passward\n"))
Passward=""
for char in range(1,Letters+1):
    random_choice=random.choice(Char_choice)
    Passward+=random_choice
    # print(random_choice)
 
for char in range(1,Number+1):
    random_choice=random.choice(Num_choice)
    Passward+=random_choice
    
for char in range(1,Special+1):
    random_choice=random.choice(Special_chars_choice)  
    Passward+=random_choice
    
print("your passward is\n",Passward)   