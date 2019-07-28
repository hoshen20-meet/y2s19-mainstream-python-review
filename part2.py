# Part 2 of the Python Review lab.

def is_prime(n):
        if n > 1:
                for i in range(2, n):
                        if n % i == 0:
                                return False
        return True

def encode(x, y):
        is_prime(x)
        is_prime(y)
        if(1<y<250) and (500<x<1000):
                return(x*y)
        else:
                print('Invalid input: Outside range.')
                return None


        

def decode(coded_message):
	
