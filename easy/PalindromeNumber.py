#%%

def is_palindrome(x):
    if x < 0:
        return False
    
    if x % 10 == 0 and x != 0:
        return False

    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10

    if x == reversed_half or x == reversed_half // 10:
        return True
    else:
        return False


#%%
    
def is_palindrome(x):
    return str(x) == str(x)[::-1]

# Test the function
print(is_palindrome(121))  # Output: True
print(is_palindrome(-121)) # Output: False
print(is_palindrome(10))   # Output: False



#%%

x = 1331
reversed_half = 0

while x > reversed_half:
    reversed_half = reversed_half * 10 + x % 10
    print('reversed_half: ',reversed_half)
    x //= 10
    print('x: ',x)


#%%

x = 16162
str(x)[::-1]

str(x) == str(x)[::-1]


#%%