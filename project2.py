#!/usr/bin/env python
# coding: utf-8

# # Input Handling and User Interface
# 

#  COUNT THE NUMBER OF WORDS IN A SENTENCE OR A PARA GRAPH

# In[8]:


def count_words(sentence):
    if not sentence:
        return 0
    words = sentence.split()
    return len(words)

def main():
    user_input = input("Please enter a sentence or paragraph: ")
    word_count = count_words(user_input)
    
    if word_count == 0:
        print("Error: Empty input. Please enter a valid sentence.")
    else:
        print('\n')
        
        print(f"Word count: {word_count}")

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:





# In[ ]:




