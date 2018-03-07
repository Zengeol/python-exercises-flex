# Bonus: Factor a Number
def get_all_factors (n):
    factors = []
    for i in range (1,n+1):
        if n%i == 0:
            factors.append(i)
    return factors
    
number = int(input('Give me a number:'))
list_of_factors = get_all_factors(number)
print("factors of {} are: {}".format(number,list_of_factors))