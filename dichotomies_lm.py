# original file name: mirdicot_Imgonnafuckingkillyou.py
import math

string = "0001001010001001110011111101110011010100100000011010100110111110"
lower_bound = 0
upper_bound = 1

def transform(x):
    tempstring = ""

    for i in range(64):
        if x > 0.5:
            tempstring += "1"
        else:
            tempstring += "0"
        
        x = 4*(x-x**2)

    return tempstring

# strat: search first and last quarter
def recursion(middle, iteration):
    converted = transform(middle)
    if converted[:math.floor(iteration*0.8)] == string[:math.floor(iteration*0.8)]:
        print(middle, converted)
        res1 = recursion(middle - 2**-(iteration+3), iteration+1)
        res2 = recursion(middle + 2**-(iteration+3), iteration+1)
    else:
        return None


recursion(0.25, 0)
