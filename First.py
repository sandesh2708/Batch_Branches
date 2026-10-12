class Calculator:
    
    @staticmethod
    def fxadd(*args):
        print(sum(args))
        
    @staticmethod 
    def fxsubs(n1,n2):
        print(n1-n2)
    
    @staticmethod 
    def fxmul(*args):
        res = 1 
        for itr in args:
            res *=itr 
        print(res) 
        
    @staticmethod
    def fxdiv(n1,n2):
        print(n1/n2)
                   
        
Calculator.fxadd(1,2,3)
Calculator.fxsubs(3,2)
Calculator.fxmul(6,7,8)
Calculator.fxdiv(100,10)