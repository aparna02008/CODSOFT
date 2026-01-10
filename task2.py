class Calculator:
    def __init__(self,num1,num2,op):
        self.num1=num1
        self.num2=num2
        self.op=op
        

    def add(self):
        return self.num1+self.num2
    def sub(self):
        return self.num1-self.num2
    def mul(self):
        return self.num1*self.num2
    def div(self):
        try:
            return self.num1/self.num2
        except ZeroDivisionError:
            return "Denominator cannot be zero"
    

a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
c=input("Enter a operator: ")
calc=Calculator(a,b,c)
if c == "+":
    print(calc.add())
elif c == "-":
    print(calc.sub())
elif c == "*":
    print(calc.mul())
elif c == "/":
    print(calc.div())
else:
    print("Enter a valid operator")



    