age=int(input("Enter appropriate age"))
sex=input("Enter sex(M/F)")
nd = int(input("Enter number of days"))
if age>=15 and age<25:   
     amt=nd*700    
     print("Total wages is",amt)     
elif age>=25 and age<35:   
     amt =nd*750   
     print("Total wages is",amt)    
elif age>=35 and age<=45:
     amt=nd*800     
     print("Total wages is",amt)    
elif age>=45 and age<=55:   
     amt=nd*850    
     print("Total wages is",amt)    
else:   
     print("you are wasting pay")