# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 14:45:04 2020

@author: ASUS
"""


import json
from difflib import get_close_matches
data = json.load(open("data.json"));
def translate(word):
    word = word.lower();
    if word in data:
       return(data[word]);
    elif word.title() in data:
        return (data[word.title()]);
    elif word.upper() in data:
        return (data[word.upper()]);
    elif len(get_close_matches(word, data.keys()))>0:
        print("Did you mean %s instead" %get_close_matches(word, data.keys())[0]);
        decide = input("Press y for yes and n for no ")
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]];
        elif decide == "n":
            return ("You are typing wrong words");
        else:
            return ("You have entered wrong word please press y or n");
word =input("Enter the word you want to search: ");
output = translate(word);
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

                  
