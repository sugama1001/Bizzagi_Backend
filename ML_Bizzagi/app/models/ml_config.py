import torch
import string
import logging
import re
import numpy as np
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("tokenizer")
model_ABSA = torch.load('model_ABSA.pth')

def lowercase(review_text):
  low = review_text.lower()
  return low

def remove_punctuation(review_text, default_text=" "):
  list_punct = string.punctuation
  delete_punct = str.maketrans(list_punct,' '*len(list_punct))
  new_review = ' '.join(review_text.translate(delete_punct).split())

  return new_review

def remove_non_clear_symbols(word):
    # Ekspresi reguler untuk mencocokkan simbol-simbol yang tidak jelas
    pattern = r'[^\w\s]'  # Mengabaikan karakter alfanumerik
    cleaned_word = re.sub(pattern, '', word)
    return cleaned_word

def word_repetition(review_text):
  review = re.sub(r'(.)\1+', r'\1\1', review_text)
  return review

def repetition(review_text):
  repeat = re.sub(r'\b(\w+)(?:\W\1\b)+', r'\1',review_text, flags=re.IGNORECASE)
  return repeat

def remove_extra_whitespaces(review_text):
  review = re.sub(r'\s+',' ', review_text)
  return review

def RemoveBannedWords(toPrint):
    global re_banned_words
    return re_banned_words.sub("", toPrint)

#Banned words
bannedword = ['wkwk', 'wkwkw','wkwkwk','hihi','hihihii','hihihi','hehehe','hehehehe','hehe',
         'huhu','huhuu','ancok','guak','cokcok','hhmm','annya','huftt', 'nya', 'kiw', 'kiww', ' mmmmuah yummie']
re_banned_words = re.compile(r"\b(" + "|".join(bannedword) + ")\\W", re.I)
def RemoveBannedWords(toPrint):
    global re_banned_words
    return re_banned_words.sub("", toPrint)



