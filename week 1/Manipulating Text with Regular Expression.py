import re

text = "This is a good day. This iiisss car. The biiiiiig car"
print(re.search('good', text) is not None)
print(re.split('This', text))
print(re.findall('This', text))
print("Starts from T: ", re.match('^T', text) is not None)
# set operator []
print("Find all [is]: ", re.findall("[is]", text))
print("Find all is: ", re.findall("is", text))
print("Find all [a-i][a-z]: ", re.findall("[a-i][a-z]", text))
print("Find all hi|he: ", re.findall("hi|he", text))
print("Find all [^i]: ", re.findall("[^i]", text))
print("Find all ^[^i]: ", re.findall("^[^i]", text))
# quantifiers
print("Find all i{2,5}: ", re.findall("i{2,5}", text))
print("Find all i{2,5}s{1,3}: ", re.findall("i{2,5}s{1,3}", text))
print("Find all i{2,5}s{1,3}: ", re.findall("i{2,5}s{*}", text))

# Progress, Lisp, Xbox
with open('ferpa.txt', "r") as ferpa:
    ferpa_txt = ferpa.read()
print("Find all string.[number]:", re.findall("[a-zA-Z]{1,100}[.]\[[0-9]+\]", ferpa_txt))
print("Find all string[number]:", re.findall("[a-zA-Z]{1,100}\[[0-9]+\]", ferpa_txt))

print("Find all [edit]\n: ", re.findall("[a-zA-Z]{1,100}\[edit\]", ferpa_txt))
print("Find all [edit]\n: ", re.findall("[\w]{1,100}\[edit\]", ferpa_txt))
print("Find all [edit]\n: ", re.findall("[\w]+\[edit\]", ferpa_txt))
print("Find all [edit]\n: ", re.findall("[\w\s]+\[edit\]", ferpa_txt))

for title in re.findall("[\w\s]+\[edit\]", ferpa_txt):
    print(re.split("\[edit\]", title)[0])


import numpy as np
a = np.array([[1, 2.8, 1.6], [2, 3, 4]])



indx = np.find(2)
