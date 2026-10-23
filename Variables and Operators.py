import random

def main():
    
    # goals: 
    # 0. variables
    # whole number: int
    # decimal: float
    # string: text
    a = "text"
    print(a)
    print(type(a))

    # 1.  basic functions: print, input. 
    value = input("input a value here: ")
    #float function will not convert a text. 
    flt_value = float(value)
    print(f"data type of value is {type(flt_value)}.")

    # 2. ways to print stuff
    print("the value is"+ value + ".")
    print("the value is", value, ".")
    print(f'the value is {value}.')
    
    # 3. arithmetic: +, -, /, *, **
    val_1 = 1
    val_2 = 2
    sum_val = val_1 + val_2
    sub_val = val_1 - val_2
    div_val = val_1/val_2 #what if val_2 was 0 here?
    mul_val = val_1*val_2
    sqr_val = val_1**2
    # unfortunately cannot do a square root with an inbuild 
    print("Sum is", sum_val, ".",
       "Subtraction is", sub_val, ".",
       "Division is", div_val, ".",
       "Multiplication is", mul_val, ".",
       "Square is", sqr_val, ".",        
    )
    # try printing them in different lines in the terminal

    # 3.2 operators: <, >, ==, <=, >=, is, not, and, or, in
    if 2<3:
        #less than
        print("2 is less than 3.")
   
    if 3>2:
        #greater than
        print("3 is greater than 2")
    if 2==2:
        #equals to. 
        #try insering single = instead of == and see why it does not work here
        print("2 is equals to 2")
    if 2<3 and 4>=4:
        # check two operation at once but BOTH MUST be true
        print("2 is less than 3 and 4 is greater than or equal to 4")
    if 2<3 or 4<3:
        # check two operation at once but ONLY ONE MUST be true
        print("Either 2 is less than 3 or  4 is less than 3")
    if type(val_1) is int:
        #"is" checks for positive possibility
        #"int is integer data type"
        print(val_1, "has a data type int")
    if type(val_2) is not str:
        #val_2 must not be a str for the following code to run 
        print(val_2, "does not have a data type str")
    if "e" in "hello":
        #checks whether value exists inside the str or other things
        print("'e' string is present in 'hello' string.")
    
    elif 2<3:
        # if your "if" is true, elif or else does not run.
        print("you are inside elif statement.")
    else:
        #not a necessary command with if and elif unless required
        print("you are inside else statement.")
    
    # 4. round function
    variable_1 = 2
    variable_2 = 3
    print(variable_1/variable_2)
    print(round(variable_1/variable_2, 5))
    

if __name__ == "__main__":
    main()