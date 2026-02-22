"""
Find the Longest Word in a List
Problem: Create a function named `find_longest_word` that takes a list of strings as input.
The function should find and return the longest word in the list. 
If there's a tie, it can return any of the longest words.

"""

def find_longest_words(words):
    max_len = max(len(word) for word in words)
    return [word for word in words if len(word) == max_len]

print(find_longest_words(["apple", "banana", "kiwi", "grapefruit", "blueberry"])) 