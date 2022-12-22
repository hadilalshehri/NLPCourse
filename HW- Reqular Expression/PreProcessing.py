import re 

# Read Text file
# Corpus Link
# https://www.kaggle.com/datasets/rtatman/fraudulent-email-corpus

with open('fradulent_emails.txt') as f:
    lines = f.readlines()
mystring = str(lines)

# Regular Expression for remove and count the Tags <>
TagsRegex = '<[^>]*>'
TagsMatch = re.findall(TagsRegex, mystring) # Find Symble
mystring = re.sub(TagsRegex, '', mystring)

# Regular Expression for Find and count the Emails
EmailRegex = '\S+@\S+'
Emails = re.findall(EmailRegex, mystring) 
mystring = re.sub(EmailRegex, '', mystring)

# Regular Expression for remove and count the Puncutation(. ? !) 
PuncutaionRegex = '[^\w\s]'
PuncutaionMatch = re.findall(PuncutaionRegex, mystring) # Find Symble
mystring = re.sub(PuncutaionRegex, '', mystring)

# Regular Expression for Find and count the Emails
ionRegex = '\S+ion\s'
ionWords = re.findall(ionRegex, mystring) 
mystring = re.sub(ionRegex, '', mystring)

# show Result 
print('Number of Tags', len(TagsMatch))
print('Number of Puncutaion', len(PuncutaionMatch))
print('Number of Emails', len(Emails))
print('Number of words end by ion', len(ionWords))
print('Puncutaions',[*set(PuncutaionMatch)])
print("Number of words Left", len(mystring.split()))
print('list of Puncutaions with Number ', {i:PuncutaionMatch.count(i) for i in PuncutaionMatch})
print('List of Emails ',Emails)


# ********** HELP **********

# https://www.geeksforgeeks.org/regular-expression-python-examples-set-1/
# Few other regex patterns that can remove special characters from a string in python are,

# /[^\w\s]/gi


# caret(^) symbol. For example, 

# [^0-3] means any number except 0, 1, 2, or 3