from nltk import ngrams

sentence = 'this is a foo bar sentences and i want to ngramize it'

n = 6
Unigrams = ngrams(sentence.split(), 1)
Bigrams = ngrams(sentence.split(), 2)
Threegrams = ngrams(sentence.split(), 3)


for grams in Unigrams:
  print(grams) 

for grams in Bigrams:
  print(grams)

for grams in Threegrams:
  print(grams)