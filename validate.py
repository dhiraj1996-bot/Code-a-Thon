# Question 1
import re 
  
def isValid(s):
    Pattern = re.compile("(0/91)?[7-9][0-9]{9}") 
    return Pattern.match(s) 
  
s = input("Enter Number: ")
        
if(isValid(s)):
        print ("Valid Number")      
else:
        print ("Invalid Number")


    
    


       
        




