# Student1 = ["Arnob", "Deba", "Remon", "Ariq", "Imam" ]
# Math_marks = [20, 20, 19.5, 19, 0]
 
  
# for x in Student1:
#     for y in Math_marks:
#         print(x, ' = ', y)
        
def Mathemetics():
    var1 = int(input("Enter Number:"))
    var2 = int(input("Enter Number:"))
    operators = input("Enter a Operator:")
    decision(var1, var2, operators)

def addition(var1, var2):
    print(var1 + var2)
    continuer_str()

def subtraction(var1, var2):
    print(var1 - var2)
    continuer_str()

def multiply(var1, var2):
    print(var1 * var2)
    continuer_str()

def division(var1, var2):
    print(var1 / var2)
    continuer_str()


def decision(var1, var2, operators):
    if operators == "+":
        addition(var1, var2)
    elif operators == "-":
        subtraction(var1, var2)
    elif operators == "*":
        multiply(var1, var2)
    elif operators == "/":
        division(var1, var2)
    else:
        print("Invalid Number")
        continuer_str()

def continuer_str():
    continuer = input("Do u want to calculate more:")
    if (continuer == "Yes"):
        Mathemetics()
    else:
        exit()
        
Mathemetics()

    


  
            
        
   




 

   
 

   
    
   






    





