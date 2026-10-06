"""
A program that implements the following process:
Have the user input a positive integer, call it n.
If n is even, divide it by two.
If n is odd, multiply it by three and add one.
Continue this process until n is equal to one.
"""

def main():
    #Have the user input a positive integer, call it n.
    n = input("Enter a number: ") 
    n = int(n)
    while n!=1 and n>0:
        n = action_on_n(n)
        
def action_on_n(n):
    if n%2==0:
        new_n= n/2
        new_n = int(new_n)
        print(f'{n} is even, so I take half: {new_n}')
    else:
        new_n= n*3 + 1
        new_n = int(new_n)
        print(f'{n} is odd, so I make 3n + 1: {new_n}')
    return new_n

if __name__ == "__main__":
    main()