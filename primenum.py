print("Enter the numbers from 1 to 20")
flag =0

for i in range(2,21):

    for j in range(2,i//2 + 1):
        if i % j == 0:
            break
    else:
        print(i)
            

    
        
