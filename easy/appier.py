#%%

from collections import Counter
import re

def most_frequent_word(text, target = 'appier'):
    if isinstance(text, list):
        text = ''.join(text)
    words = re.findall(r'\b\w+\b', text.lower())
    filtered_words = [word for word in words if any(char in target for char in word)]
    word_counts = Counter(filtered_words)
    most_common2 = word_counts.most_common(2)
    if most_common2[0][1] > most_common2[1][1]:
        return most_common2[0][0] 
    else:
        return None

# Test the function
print(most_frequent_word("The happier people are happier with apples"))  # Output: 'happier'
print(most_frequent_word("The sadder dogs are sadder with oranges"))  # Output: 'sadder'
print(most_frequent_word(['T', 'h', 'e', ' ', 'a', 'p', 'p', 'l', 'e', ' ', 'i', 's', ' ', 'r', 'i', 'p', 'e']))  # Output: 'the'


#%%

# from collections import Counter
# import re

# test cases:
# text = ['T', 'h', 'e', ' ', 'a', 'p', 'p', 'l', 'e', ' ', 'i', 's', ' ', 'r', 'i', 'p', 'e']
# text = "The happier people are happier with apples"
# if isinstance(text, list):
#     text = ''.join(text)

# words = re.findall(r'\b\w+\b', text.lower())
# words

# target = 'appier'
# filtered_words = [word for word in words if any(char in target for char in word)]
# word_counts = Counter(filtered_words)
# most_common2 = word_counts.most_common(2)
# most_common2[0][1]


#%%



