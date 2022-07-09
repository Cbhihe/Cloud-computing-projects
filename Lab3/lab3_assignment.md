## Extracting and analyzing data from the Cloud


This Lab is a follow-up to the previous ones. In it we will extract interesting terms from a dataset made of tweets obtained by streaming. Tweets are about a particular event.

* Task 1: Streaming API of Twitter
* Task 2: Analyzing tweets - counting terms
* Task 3: Case study
* Task 4: Student proposal

### Task 1: Twitter’s [streaming API](https://dev.twitter.com/streaming/overview)
It give developers low-latency access to Twitter’s global stream of tweets. A proper implementation of a streaming client will receive notifications about tweets other events.  The Streaming API is one way of getting a large amounts of data without exceeding the Twitter rate limits. Connecting to it requires keeping a persistent open HTTP connection. This involves thinking about your application differently than if you were interacting with the REST API. The latter is appropriate if you intend to conduct singular searches, read user profile information, or post Tweets.

We need to extend the `StreamListener()` class to customize the way we process the incoming data. A good working example from [Marco Bonzanini](https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/)gathers all the new tweets with a reference to the "ArtificialIntelligence" tag.

```
import tweepy
from tweepy import OAuthHandler

consumer_key = 'YOUR-CONSUMER-KEY'
consumer_secret = 'YOUR-CONSUMER-SECRET'
access_token = 'YOUR-ACCESS-TOKEN'
access_secret = 'YOUR-ACCESS-SECRET'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
```
```
from tweepy import Stream
from tweepy.streaming import StreamListener
 
class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('tweets_on_ai.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as be:
            print("Error on_data: %s" % str(be))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['ArtificialIntelligence'])
```

The core of the streaming logic is implemented in the `CustomListener` class, which extends `StreamListener` and overrides two methods: `on_data()` and `on_error()`. These are handlers that are triggered when data is coming through and an error is given by the API. if the error is that we have been rate limited by the Twitter API, we need to wait before we can use the service again. The `on_data()` method is called when data is coming through. This function simply stores the data as it is received in the `tweets_on_ai.json` file. Each line of this file will then contain a single tweet, in the JSON format. You can use the command `wc -l ArtificialIntelligenceTweets.json` from a *nix shell to know how many tweets you’ve gathered.

Before continuing the hands-on, generate the `.json` file, then try doing it again with another tag or term of your choosing.

### Task 2:  Analizing tweets - Counting terms
- Perform is a simple word count. Observe which are the terms most commonly used in your corpus.
- Read the file with tweets
```
import json  
with open('tweets_on_ai.json','r') as json_file:
         for line in json_file:
             tweet = json.loads(line)
             print tweet["text"]
```
- tokenize the tweets
         

```
import json
 
with open('tweets_on_ai.json', 'r') as f:
    line = f.readline() 
    tweet = json.loads(line) 
    print(json.dumps(tweet, indent=4)) 
```
- Process all our tweets, previously saved on file

```
with open('tweets_on_ai.json', 'r') as f:
#import io
#f=io.open('data/stream_barcelona.json', 'r', encoding='utf8' )
     for line in f:
        tweet = json.loads(line)
        tokens = preprocess(tweet['text'])
        print(tokens)
```
In the above `preprocess` was defined in previously. It captures Twitter-specific aspects of the text, such as #hashtags, @-mentions and URLs.

```
import re

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs

    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]

tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)

def tokenize(s):
    return tokens_re.findall(s)

def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens
```
- Use `collections.Counter()` which internally is a dictionary with useful methods such as `most_common()`

```
import operator 
import json
from collections import Counter

infile = 'tweets_on_ai.json'
with open(infile, 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        # Create a list with all the terms
        terms_all = [term for term in preprocess(tweet['text'])]
        # Update the counter
        count_all.update(terms_all)
    print(count_all.most_common(5))
```
The above code yields many tokens that are stop-words. Given the nature of our data and our tokenisation, we should be careful about punctuation and terms such as `RT` (used for re-tweets) or `via` (used to mention the original author), which are not in the default stop-word list.

```
import nltk
from nltk.corpus import stopwords
nltk.download("stopwords")
import string

punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via', 'RT']

```

- Substitute the variable `terms_all` in the first example with something like:

```
import operator 
import json
from collections import Counter
 
fname = infile
with open(fname, 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        # Create list with all terms
        terms_stop = [term for term in preprocess(tweet['text']) if term not in stop]
        count_all.update(terms_stop)
    for word, index in count_all.most_common(5):
        print '%s : %s' % (word, index)
```

- Further customise the list of tokens of interest. For instance, if we want to count *hastags* only:
```
terms_hash = [token for token in preprocess(tweet['text']) 
              if token.startswith('#')]
```
- When only interested in counting terms (neither hashtags nor mentions):
```
terms_only = [token for token in preprocess(tweet['text']) 
              if (token not in stop and not token.startswith(('#', '@')))] 
```

Sometimes considering bigrams, i.e. n-grams with n=2, considers sequences of two terms is interesting. Carry out the same analysis with bigrams based on the same `.json` file generated in the previous task.

### Task 3:  Case study
Consider a small dataset with 1060 tweets downloaded from around 18:05 to 18:15 on January 13, 2017, where the word "Barcelona" was tracked using the `twitter_stream.filter` function.

- To get a rough idea of what people say in realtion to Barcelona, count and sort the most commonly used hastags:
```
import operator 
import json
from collections import Counter
 
infile = 'case_study.json'
with open(infile, 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        # Create list with all terms
        terms_hash = [token for token in preprocess(tweet['text']) if token.startswith('#') and token not in stop]        
        count_all.update(terms_hash)
# Print the first 10 most frequent words
print(count_all.most_common(15))

```
The output is:
`[(u'#Barcelona', 68), (u'#Messi', 30), (u'#FCBLive', 17), (u'#UDLasPalmas', 13), (u'#VamosUD', 13), (u'#barcelona', 10), (u'#CopaDelRey', 8), (u'#empleo', 6), (u'#BCN', 6), (u'#riesgoimpago', 6), (u'#news', 5), (u'#LaLiga', 5), (u'#SportsCenter', 4), (u'#LionelMessi', 4), (u'#Informe', 4)]`

- Visualize your findings with a plot. Use `matplotlib`, `ggplot`, etc.

```
%matplotlib inline
import matplotlib as mpl
mpl.rcParams['figure.figsize'] = (15,10)
import matplotlib.pyplot as plt

sorted_x, sorted_y = zip(*count_all.most_common(15))
#print(sorted_x, sorted_y)

plt.bar(range(len(sorted_x)), sorted_y, width=0.75, align='center');
plt.xticks(range(len(sorted_x)), sorted_x, rotation=80);
plt.axis('tight'); 

```
that uses the function `zip()`.

We can see that people were talking about football, more than other things! And it seems that they were mostly talking about the football [league match that was played the next day](http://www.fcbarcelonanoticias.com/Calendario-y-resultados-liga.php?IDR=184).

Create a "matplot" with your dataset generated by you in the previous task.

### Task 4:  Student proposal

- Create an example to find some interesting insight in a subject of your choice from Twitter, using realistic data captured by you.
