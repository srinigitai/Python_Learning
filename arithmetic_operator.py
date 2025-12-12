# Task: Create a CLASS
# Syntax : class classname():
#              def function_name():
    
class arithmetic_operator():
    def addition():
        add_num1=int(input("Enter Number1 : "))
        add_num2=int(input("Enter Number2 :"))
        add=add_num1+add_num2
        #print(add)
        return add
    
    def substraction():
        sub_num1=int(input("Enter Number1 : "))
        sub_num2=int(input("Enter Number2 : "))
        sub=sub_num1-sub_num2
        return sub
    
    def division():
        div_num1=int(input("Enter Number1 : "))
        div_num2=int(input("Enter Number2 : "))
        div=div_num1/div_num2
        return div
    
    def multiplication():
        mul_num1=int(input("Enter Number1 : "))
        mul_num2=int(input("Enter Number2 : "))
        mul=mul_num1 * mul_num2
        return mul
