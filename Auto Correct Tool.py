#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np

# Function to calculate Levenshtein distance
def levenshtein_distance(s1, s2):
    m = len(s1)
    n = len(s2)
    
    # Create a matrix of size (m+1)x(n+1) and initialize with 0
    matrix = np.zeros((m+1, n+1))
    
    # Initialize the first row and column
    for i in range(m+1):
        matrix[i][0] = i
    for j in range(n+1):
        matrix[0][j] = j
    
    # Calculate the minimum edit distance
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                matrix[i][j] = min(
                    matrix[i-1][j] + 1,          # Deletion
                    matrix[i][j-1] + 1,          # Insertion
                    matrix[i-1][j-1] + 1         # Substitution
                )
    
    return int(matrix[m][n])

# Function to find the closest word
def find_closest_word(word, word_list):
    min_distance = float('inf')
    closest_word = None
    
    for candidate in word_list:
        distance = levenshtein_distance(word, candidate)
        if distance < min_distance:
            min_distance = distance
            closest_word = candidate
    
    return closest_word

# List of words for testing
word_list = ['apple', 'banana', 'orange', 'peach', 'kiwi', 'grape']

# Test word
word = 'banan'

# Find closest word
closest_word = find_closest_word(word, word_list)

print(f"Input Word: {word}")
print(f"Closest Word: {closest_word}")


# In[11]:


# List of words for testing
word_list = ['apple', 'banana', 'orange', 'peach', 'kiwi', 'grape']

# Test word
word = 'oran'

# Find closest word
closest_word = find_closest_word(word, word_list)

print(f"Input Word: {word}")
print(f"Closest Word: {closest_word}")


# In[12]:


# List of words for testing
word_list = ['apple', 'banana', 'orange', 'peach', 'kiwi', 'grape']

# Test word
word = 'kiw'

# Find closest word
closest_word = find_closest_word(word, word_list)

print(f"Input Word: {word}")
print(f"Closest Word: {closest_word}")


# In[13]:


# List of words for testing
word_list = ['apple', 'banana', 'orange', 'peach', 'kiwi', 'grape']

# Test word
word = 'peac'

# Find closest word
closest_word = find_closest_word(word, word_list)

print(f"Input Word: {word}")
print(f"Closest Word: {closest_word}")


# In[14]:


# List of words for testing
word_list = ['apple', 'banana', 'orange', 'peach', 'kiwi', 'grape']

# Test word
word = 'grap'

# Find closest word
closest_word = find_closest_word(word, word_list)

print(f"Input Word: {word}")
print(f"Closest Word: {closest_word}")


# #  thank you 
