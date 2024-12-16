import re

def find_elements_with_word(word_list, input_word):
    pattern = re.compile(input_word)
    
    matching_elements = []
    
    for element in word_list:
        if pattern.search(element):
            matching_elements.append(element)
    
    return matching_elements

