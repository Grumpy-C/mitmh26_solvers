import time

lower_bound = 0
upper_bound = 10
precision = 1

strindex = 0
string = "000000101100100001111110000001111111111111111111110110001101100000"
for char in string:
    print(string[:strindex+1])
    validatprecision = 0
    currUnder = False
    for i in range(lower_bound+1, upper_bound, 1):
        num = i/(10**precision) # bullshit because you can't have a float as a step value
        num2 = i/(10**precision)
        currstring = ""
        while abs(num - 1) > 0.0001: # generate from this test value, trial and error
            if num > 1:
                num -= 1
                currstring += "1"
            else:
                num /= (1 - num)
                currstring += "0"
            if len(currstring) > 2000:
                break
        #compare against our current number

        if len(currstring)-1 < strindex: # case: this will be a bound
            validatprecision += 1
            if string[strindex] == "0":
                if round(num2*10**precision) < upper_bound:
                    upper_bound = round(num2*10**precision)
            else:
                if round(num2*10**precision) > lower_bound:
                    lower_bound = round(num2*10**precision)
        elif string[:strindex] == currstring[:strindex]:
            if string[strindex] == "0" and currstring[strindex] == "1": # case: generated value is over
                if round(num2*10**precision) < upper_bound:
                    upper_bound = round(num2*10**precision)
                    break
            elif string[strindex] == "1" and currstring[strindex] == "0": # case: generated value is under
                currUnder = True
            else: # case all good
                if round(num2*10**precision) > lower_bound and currUnder:
                    lower_bound = round(num2*10**precision)-1
                    currUnder = False
                validatprecision += 1

        if len(currstring) < 500:
            print(num2, currstring, lower_bound, upper_bound)
        else:
            print(num2, "long number, >500", lower_bound, upper_bound)

    print(f"-------------- {validatprecision}")
    if validatprecision < 3:
        precision += 1
        lower_bound *= 10
        upper_bound *= 10
    strindex += 1