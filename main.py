
from random import randrange
import tweepy
import nltk
import json
import keys


TAG_PATH = 'neo_tags.json'
WORD_PATH = "english_words.txt"


def load_nltk_libs():
   nltk.download('punkt')
   nltk.download('wordnet')
   nltk.download('words')
   nltk.download('cess_esp')
   nltk.download('udhr')
   nltk.download('averaged_perceptron_tagger')


def load_neo_tags_and_words():
  with open(TAG_PATH, 'r') as f:
    neo_tags = json.load(f)

  with open(WORD_PATH, 'r') as f:
    english_words = [line.strip(' \n') for line in f.readlines()]
  
  return neo_tags, english_words


def generate_neologism(neo_tags, eng_words):
    """
    Generates a neologism based on the tags of a randomly selected neologism from Ulysses
    :param neo_tags: dictionary with neologism tags
    :param eng_words: list of english words
    :return: neologism
    """
    
    eng_words = [w for w in eng_words if len(w) > 3]    
    r_neo = randrange(len(neo_tags.keys()))
    neo = list(neo_tags.keys())[r_neo]
    r_neo_tags = neo_tags[list(neo_tags.keys())[r_neo]]
    while r_neo_tags[0] == 'None':                     
        r_neo = randrange(len(neo_tags.keys()))
        neo = list(neo_tags.keys())[r_neo]
        r_neo_tags = neo_tags[list(neo_tags.keys())[r_neo]]
 
    gen_neo = []    
    for i, tag in enumerate(r_neo_tags):
        neo_part = get_tag_part(eng_words, tag)
        if i != 0:
          # if the last part ends in a vowel, the next part should start with a consonant
          while double_vowels(gen_neo[-1], neo_part):
            neo_part = get_tag_part(eng_words, tag)
       
        gen_neo.append(neo_part)
    
    return ''.join(gen_neo)


def double_vowels(first: str, second: str) -> bool:
  vowels = {'a', 'e', 'i', 'o', 'u'}
  return (first[-1] in vowels) and (second[0] in vowels)


def get_tag_part(eng_words, tag):
  r_eng = randrange(len(eng_words))
  r_eng_tag = [tag for (word, tag) in nltk.pos_tag(eng_words[r_eng].split())][0]
  while(r_eng_tag != tag or eng_words[r_eng][0].isupper()):
      r_eng = randrange(len(eng_words))
      r_eng_tag = [tag for (word, tag) in nltk.pos_tag(eng_words[r_eng].split())][0]
  return eng_words[r_eng]


def get_neologism() -> str:
    #load_nltk_libs()
    neo_tags, eng_words = load_neo_tags_and_words()
    return generate_neologism(neo_tags, eng_words)


def gen_tweet():
  neologism = get_neologism()
  print(f"{neologism=}")
  client = tweepy.Client(
    consumer_key=keys.api_key, consumer_secret=keys.api_secret_key,
    access_token=keys.access_token, access_token_secret=keys.access_secret_token    
   )
  
  client.create_tweet(
    text=neologism
  )


if __name__ == '__main__':
  gen_tweet()



