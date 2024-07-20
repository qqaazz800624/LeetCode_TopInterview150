#%%

def roman_to_int(s):
    
    roman_integer_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                         'C': 100, 'D': 500, 'M': 1000}
    total, previous = 0, 0

    for char in reversed(s):
        value = roman_integer_map[char]
        if value < previous:
            total = total - value
        else:
            total = total + value
        previous = value

    return total

# Test the function
print(roman_to_int("III"))    # Output: 3
print(roman_to_int("IV"))     # Output: 4
print(roman_to_int("IX"))     # Output: 9
print(roman_to_int("LVIII"))  # Output: 58
print(roman_to_int("MCMXCIV"))# Output: 1994


#%%
        
class Solution:
    def roman_to_int(self, s: str) -> int:
        roman_integer_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                         'C': 100, 'D': 500, 'M': 1000}
        total = 0

        replace_map = {"IV": "IIII", "XL": "XXXX", "CD": "CCCC",
                       "IX": "VIIII", "XC": "LXXXX", "CM": "DCCCC"}
        weired_spelling = ["IV", "XL", "CD", "IX", "XC", "CM"]

        for spelling in weired_spelling:
            s = s.replace(spelling, replace_map[spelling])
        
        for char in reversed(s):
            total = total + roman_integer_map[char]
        return total

# Test the function
print(roman_to_int("III"))    # Output: 3
print(roman_to_int("IV"))     # Output: 4
print(roman_to_int("IX"))     # Output: 9
print(roman_to_int("LVIII"))  # Output: 58
print(roman_to_int("MCMXCIV"))# Output: 1994

#%%

s = 'MCMXCIV'
[char for char in s]


#%%