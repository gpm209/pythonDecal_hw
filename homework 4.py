
#problem 2.1 Making a list variable
#Create a a variable that is assigned a list with numbers o throuugh 20.
list_of_num = list(range(21))
print(list_of_num)

#problem 2.2 write a function that takes in your list from part 2.1 and square each element in the list. 
#Assign the result to a new variable
def squareList(lst):
    new_list = []
    for i in lst:
        new_list.append(i**2)
    return new_list

square_lst = squareList(list_of_num)
print(square_lst)


#Problem 2.3 Write a function that take in your list from 2.2 and returns the first 15 elements from the list using slicing

def first_fifteen(new_list):
    return new_list[:15]

print(first_fifteen(square_lst))

#Problem 2.4 write a function that takes in your list from part 2.2 and returns every 5th element from the list using striding
def every_fifth_elem(squared_list):
    return squared_list[4::5]

print(every_fifth_elem(square_lst))

#2.5 Write a function that takes your list from part 2.2 and slices the last 30 elements of the list
#returns every 3rd element from that list in reverse order

def thirty_element(squared_lst):
    return squared_lst[2::3][::-1]

print(thirty_element(square_lst))


#3.1 Write a function that uses nested for loops to create a 5x5 2D list where the numbers 1 thorugh 25 are stored sequentially

def create_2D_list():
    matrix = []
    number = 1
    for x in range(5):
        row = []
        for y in range(5):
            row.append(number)
            number +=1
        matrix.append(row)
    return matrix
 
print(create_2D_list())

#3.2 with the 2D list created in part 3.1, write a function that will replace all multiples of 3 witht the character "?"

def modified_2D_list(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] % 3 == 0:
                matrix[row][col] = "?"
    return matrix

m = create_2D_list()
print(modified_2D_list(m))

#3.3 Assign the result of the function from 3.2 to a variable 
#write a function that will iterate through the new 2D list variable and return the sum of all the elements that are not "?"

def sum_non_q_elements(table):
    total = 0
    for x in table:
        for element in x:
            if element != "?":
                total +=element
            else:
                total
    return total

n = sum_non_q_elements(m)
print(n)

