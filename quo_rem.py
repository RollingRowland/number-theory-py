import math

#divisibility functions regarding quotients and remainders

#calculates quotient and remainder
def q_r(a,b):
    if b==0:
        return "Undefined"
    quotient = math.floor(a/b)
    remainder = a%b
    return quotient, remainder

#calculates and displays quotient and remainder
def q_r_display(a,b):
    quotient,remainder = q_r(a,b)
    print(f"Quotient: {quotient}")
    print(f"Remainder: {remainder}")
    if remainder==0:
        print(f"{a} = {quotient}*{b}")
    else:
        print(f"{a} = {quotient}*{b} + {remainder}")

#calculates and displays quotient and remainder
def q_r_display_2(a,b):
    quotient_remainder = {"quotient":"","remainder":""}
    quotient_remainder["quotient"], quotient_remainder["remainder"] = q_r(a,b)
    print(quotient_remainder)
    if quotient_remainder["remainder"]==0:
        print(f"{a} - {quotient_remainder['quotient']}*{b} = 0")
    else:
        print(f"{a} - {quotient_remainder['quotient']}*{b} = {quotient_remainder['remainder']}")

#It is the case that if a = qb + r, then gcd(a,b)===gcd(b,r). We shall use in
#euclids algorithm to create a function that calculates the gcd(a,b)

def gcd(a,b):
    if b==0:
        return a
    if a<b:
        num1 = b
        num2 = a
    else:
        num1 = a
        num2 = b
    quo,rem = q_r(num1,num2)
    while rem!=1:
        if rem==0:
            return num2
        else:
            num1 = num2
            num2 = rem
            quo,rem = q_r(num1,num2)
    return 1

#Bezouts identity takes the above and states that gcd(a,b) = a*u + b*v for some
#integers u and v. There are multiple u and v solutions. Practically, we can determine the u and v by working backwards from
#euclids algorithm.

#Example:
#gcd(28,6)=2
#28 = 4*6 + 4
#6 = 1*4 + 2
#4 = 2*2 + 0
#gcd(28,6) = 2

#2 = 6 - 4
#2 = 6 - (28-6*4)
#2 = 5*6 - 1*28
#2 = -1*28 + 5*6
# u = -1, v = 5


def gather_quotients(a,b):
    if b==0:
        return [a]
    num1 = a
    num2 = b
    quotients = []
    quo, rem = q_r(num1,num2)
    quotients.append(-1*quo)
    while rem!=1 and rem!=0:
        num1 = num2
        num2 = rem
        quo,rem = q_r(num1,num2)
        if rem!=0 and rem!=1:
            quotients.append(-1*quo)
    quotients.reverse()
    return quotients

def bezout(a,b):
    quotients = gather_quotients(a,b)
    if len(quotients)==1:
        return print("b divides a")
    num1 = 1
    num2 = quotients[0]
    for i in range(len(quotients)-1):
         u_v = [num1,0]
         u_v[0] += num2*quotients[i+1]
         u_v[1] += num2
         num2 = u_v[0]
         num1 = u_v[1]
    return u_v



#We can calculate the gcd of n different numbers, i.e. gcd(a1, a2, a3, ..., an)
#by calculating the gcd thusly: gcd(gcd(a1,a2),a3,...,an) = gcd(gcd(d,a3),...,an)
#etcetc.

def gcd_extend(a,b,*nums):
    div = gcd(a,b)
    for num in nums:
        div = gcd(div,num)
    return div


def lcm(a,b):
    lcm = (a*b)/gcd(a,b)
    return lcm








        








        
        
        

    
