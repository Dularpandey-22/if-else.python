p=int(input("enter marks for physics"))
ch=int(input("enter marks for chemistry"))
b=int(input("enter marks for biology"))
m=int(input("enter marks for mathematic"))  
c=int(input("enter marks for computer"))
tot=p+ch+b+m+c
per=tot/5
if per>=90: 
    grade='A'  
elif per>=80:  
    grade='B'   
elif per>=70:    
    grade='C'    
elif per>=60:    
    grade='D'    
elif per>=40:    
    grade='E'        
elif per>=40:    
    grade='F'        
else:    
    grade="reappear"     
print("total marks:",tot)
print("percentage:",per)
print("grade:",grade)