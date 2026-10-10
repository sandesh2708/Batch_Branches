class Calculator:
    
    @staticmethod
    def fxadd(*args):
        print(sum(args))
        
    @staticmethod 
    def fxsubs(n1,n2):
        print(n1-n2)
        
        
Calculator.fxadd(1,2,3)
Calculator.fxsubs(3,2)