#!/usr/bin/env python
# coding: utf-8

# In[3]:


import hashlib

def simhash(input, bit_size=8):
    # Split the input into a set of features (e.g., words)
    features = input.split()
    
    # Initialize a vector for simhash (assuming 8 bits for this case)
    v = [0] * bit_size
    
    # Hash each feature and update the vector
    for feature in features:
        # Generate a hash for the feature
        hash_value = int(hashlib.sha1(feature.encode('utf-8')).hexdigest(), 16)
        
        # Update the vector based on the hash bits (only for 8 bits)
        for i in range(bit_size):
            bitmask = 1 << i
            if hash_value & bitmask:
                v[i] += 1  # Feature contributes positively
            else:
                v[i] -= 1  # Feature contributes negatively
    
    # Generate the final SimHash from the vector
    simhash = 0
    simhash_bits = []
    
    for i in range(bit_size):
        if v[i] > 0:
            simhash |= 1 << i
            simhash_bits.append(1)
        else:
            simhash_bits.append(0)
    
    # Return the SimHash as an integer and its binary representation as a list
    return simhash, simhash_bits

def compare_simhashes(simhash1, simhash2):
    # Calculate the Hamming distance between the simhashes
    distance = bin(simhash1 ^ simhash2).count('1')
    return distance

# Calculate the simhash for two pieces of text using 8 bits
text1 = "The quick brown fox jumps over the lazy dog."
text2 = "The quick brown fox jumps over the lazy cat."
simhash1, simhash_bits1 = simhash(text1, bit_size=8)
simhash2, simhash_bits2 = simhash(text2, bit_size=8)

# Display the simhash values and their bit representations
print(f"Simhash 1: {simhash1}")
print(f"Simhash 1 bits: {''.join(map(str, simhash_bits1))}")

print(f"Simhash 2: {simhash2}")
print(f"Simhash 2 bits: {''.join(map(str, simhash_bits2))}")

# Compare the simhashes
distance = compare_simhashes(simhash1, simhash2)
print(f"Distance between simhashes: {distance}")

# Determine how similar the texts are based on the simhash distance
if distance < 2:
    print("Texts are very similar.")
elif distance < 4:
    print("Texts are somewhat similar.")
else:
    print("Texts are not similar.")


# In[ ]:




