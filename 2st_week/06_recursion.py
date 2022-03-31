from tkinter.tix import Tree


def count_down(number):
    if number < 0:
        return
    print(number)
    count_down(number-1)

count_down(5)
#####################
def factorial(n):

    if n==1:
        return 1
    return n * factorial(n-1)

print(factorial(6))

#####################
input = "abcba"

# def is_palindrome(string):
#     n=len(string)
#     for i in range(n):
#         if string[i] != string[n-i-1]:
#             return False
#     return True
def is_palindrome(string):
    if len(string) <=1:
        return True
    if string[0] != string[-1]:
        return False
    return is_palindrome(string[1:-1])

print(is_palindrome(input))