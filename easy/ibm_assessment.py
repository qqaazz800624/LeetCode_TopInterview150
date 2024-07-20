#%%

def getWho(s):
    # Write your code here
    # Check the number of strings constraint
    if not 1 <= len(s) <= 100:
        raise ValueError("The number of strings must be between 1 and 100.")
    
    vowels = set('aeiou')
    results = []

    for code in s:
        if not 1 <= len(code) <= 10**5:
            raise ValueError("The length of each string must be between 1 and 100000.")
        
        if not code.isalpha() or not code.islower():
            raise ValueError("All strings must consist of lowercase English letters only.")
        
        vowel_count = 0
        for char in code:
            if char in vowels:
                vowel_count += 1

        if vowel_count % 2 == 0:
            results.append("Chris")
        else:
            results.append("Alex")

    return results

s = ['ljis', 'lhr', 'gms']
getWho(s)

#%%

s = ['lgzpc', 'lchxlo', 'xrwzg']
getWho(s)


#%%

s = ['cim']
getWho(s)





#%%


def count_vowels(s):
    return sum(char in 'aeiou' for char in s)

def getWho(s):
    # Check the number of strings constraint
    if not 1 <= len(s) <= 100:
        raise ValueError("The number of strings must be between 1 and 100.")
    
    winners = []
    for string in s:
        # Check the length of each string constraint
        if not 1 <= len(string) <= 10**5:
            raise ValueError("The length of each string must be between 1 and 100000.")
        
        # Check if all characters are lowercase English letters
        if not string.isalpha() or not string.islower():
            raise ValueError("All strings must consist of lowercase English letters only.")
        
        vowel_count = count_vowels(string)
        if vowel_count % 2 == 0:  # Even number of vowels
            winners.append('Chris')
        else:  # Odd number of vowels
            winners.append('Alex')
    return winners

# Test the function with a valid input
if __name__ == '__main__':
    strings = ['ljis', 'lhr', 'gms']
    print(getWho(strings))

# Test the function with an invalid input (uncomment to test)
# print(getWho(['ThisIsInvalidBecauseItsTooLong' * 10000]))






#%%

txt = "CompanyX"

x = txt.isalpha()

print(x)




#%%







#%%









#%%






#%%







#%%