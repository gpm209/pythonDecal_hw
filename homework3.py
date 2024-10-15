
#problem 1

def exp_(x, y):
    m = 1                  
    for i in range(y):
        m*=x 

    return m

print(exp_(2,3))


#problem 2
  
def temp(temperatures):
    
    min_temp = min(temperatures)
    max_temp = max(temperatures)
    
    return (min_temp, max_temp)


readings = [15, 14, 17, 20, 23, 28, 20]

print(temp(readings)) 

#problem 3

def isWeekend(day):

   d = 1
   
   if day == 6 or day == 7:
       d = True
   else:
       d =False
   return d

day =range(1,7) # Can we use a range? or, is day = 7?
print(isWeekend(5))

#problem 4

def fuel_efficiency(distance, fuel):
    x = distance/fuel

    return x

print(fuel_efficiency(70, 21.5))

#problem 5
def decode_Numbers(n):
    nmod = n%10
    nfloor = n//10

    nfloor_1 = n//10

    x = 1
    
    while nfloor > 0:
        nfloor = nfloor//10
        x*=10
    return nmod*x+nfloor_1

print(decode_Numbers(12345))

#problem 6.1
#def find_min(num):
def min_num(l):
    min_val = l[0]
    for i in l:
        if i < min_val:
            min_val = i 
    return min_val

print(min_num([1,5,7,98,34]))

def max_num(list):
    max_val = list[0]
    for i in list:
        if i > max_val:
            max_val = i
    return max_val

ls = [3,4,5,6,8,87]
print(max_num(ls))

#problem 6.2
def find_max(list):
    max = list[0]
    x = 1
    while x < len(list):
        if list[x] > max:
            max = list[x]
        x +=1
    return max

list = [2,6,8,9]
print(find_max(list))

def find_min(n):
    min = n[0]
    y = 1
    while y < len(n):
        if n[y] <min:
            min = n[y]
        y+=1
    return min

print(find_min(list))

#problem 7

def vowel_and_consonant_count(text):
    vowels_num =  "aeiouAEIOU"
    vowel = 0
    consonant = 0
   
    for character in text:
        if character.isalpha():
            if character in vowels_num:
                vowel+=1
            else:
                consonant+=1

    return (vowel, consonant)

print(vowel_and_consonant_count("UC Berkeley, founded in 1868!"))
#problem 8

def int_sum(digits):

    total = 0

    while digits > 0:
        total += digits %10
        digits//= 10
    return total

print(int_sum(2468))