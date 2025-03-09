lambda:
    
square = lambda x: x ** 2
print(square(5))
 
multiply = lambda x, y: x * y
print(multiply(3, 7))

def my_func(n):
    return lambda x: x * n

doubler = my_func(2)
print(doubler(5))

my_list = [1, 2, 3, 4, 5, 6]
odd_numbers = list(filter(lambda x: x % 2 != 0, my_list))
print(odd_numbers)

my_list = [("apple", 50), ("banana", 10), ("cherry", 30)]
sorted_list = sorted(my_list, key=lambda x: x[1])
print(sorted_list)

output:

25
21
10
[1, 3, 5]
[('banana', 10), ('cherry', 30), ('apple', 50)]

** Process exited - Return Code: 0 **
Press Enter to exit terminal

map:
    
s = ['1', '2', '3', '4']
res = map(int, s)
print(list(res))

a = [1, 2, 3, 4]
def double(val):
  return val*2

res = list(map(double, a))
print(res)


a = [1, 2, 3, 4]

res = list(map(lambda x: x * 3, a))
print(res)

a = [1, 2, 3]
b = [4, 5, 6]
res = map(lambda x, y: x + y, a, b)
print(list(res))

fruits = ['apple', 'banana', 'cherry']
res = map(str.upper, fruits)
print(list(res))

output:
    
[1, 2, 3, 4]
[2, 4, 6, 8]
[3, 6, 9, 12]
[5, 7, 9]
['APPLE', 'BANANA', 'CHERRY']

** Process exited - Return Code: 0 **
Press Enter to exit terminal

filter:

# Function to check if a number is even
def even(n):
    return n % 2 == 0

a = [1, 2, 3, 4, 5, 6]
b = filter(even, a)
print(list(b))  

a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x % 2 == 0, a)
print(list(b))  

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  

lists = [[1, 2], [3, 4, 5], [6], [7, 8, 9, 10]]
longer_lists = list(filter(lambda x: len(x) > 2, lists))
print(longer_lists) 

names = ["Alice", "Bob", "Andrew", "Charlie", "Anna"]
a_names = list(filter(lambda x: x.startswith("A"), names))
print(a_names)

output: 

[2, 4, 6]
[2, 4, 6]
[2, 4, 6, 8, 10]
[[3, 4, 5], [7, 8, 9, 10]]
['Alice', 'Andrew', 'Anna']

** Process exited - Return Code: 0 **
Press Enter to exit terminal
