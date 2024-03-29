"""Generate Markov text from tweets."""

from random import choice
from twitter import get_tweets

#TODO::::: Clean up the tweet text to remove any links

def create_tweet_string(tweets):
    """Converts list of tweets to a single string"""
    
    tweet_string = ' '.join(tweets)

    return tweet_string


def make_chains(tweet_string):
    """Take input text as string; return dictionary of Markov chains.
    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.
    """
    
    chains = {}

    words_list = tweet_string.split()
    
    for word in words_list:
        if 'https' in word or '&' in word:
            words_list.remove(word)



    for word in range(0,len(words_list)-2):
        bi_word = (words_list[word], words_list[word+1])

        chains[bi_word] = chains.get(bi_word,[])+ [words_list[word+2]]
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    beginning_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sentence_end = ".!?;!!!!!"


    base_bi_word = choice(list(chains.keys()))
    while base_bi_word[0][0] not in beginning_letters:
        base_bi_word = choice(list(chains.keys()))
        
    words.append(base_bi_word[0]) #unpack the tuple
    words.append(base_bi_word[1])
    next_word = choice(chains[base_bi_word])

    
    while next_word[-1] not in sentence_end:
        words.append(next_word)
        base_bi_word = (words[-2],words[-1])
        next_word = choice(chains[base_bi_word])

    words.append(next_word)
    return(" ".join(words))


#Get Tweets from twitter API for Kevin Hart and Dwayne Johnson
tweets = get_tweets("Kevin Hart", "Dwayne Johnson")

#Convert list to string
tweet_string = create_tweet_string(tweets)

# Get a Markov chain
chains = make_chains(tweet_string)


# Produce random text
random_text = make_text(chains)

print(random_text)