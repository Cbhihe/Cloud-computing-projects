## Lab 2: APIs as gateways to the Cloud

In this Lab we will discuss the overall structure of a tweet and discuss how to pre-process the text before we can get into some more interesting analysis in the next Lab. In particular, we will see how tokenisation, despite being a well-understood problem, can get tricky with Twitter data. Prior to this, we will  install a special Python development environment.

* Pre-lab Tasks
   * PL task 1: Install Anaconda
   * [PL task 2: Register your App on Twitter
* Lab Tasks
   * Task 1: Get Started with NLTK
   * Task 2: Getting Started with `tweepy`
   * Task 3: Tweet pre-processing

An API provides a way for computer systems to interact with each other. There are many types of APIs. Every programming language has a built-in API that it used to write programs. Operating systems themselves have APIs used by programs to open files or draw text on the screen. Many APIs are built with web technologies, e.g. HTTP, in mind. . We will refer to this type of API as web API, an interface to either a web server or a web browser. These APIs are used extensively for the development of web applications and work often in the Cloud, at either the server end or the client end. 

Web APIs are a key component to be able to access Cloud platforms programmatically. Many Cloud applications provide an API that allows developers to integrate their own code with these applications, taking advantage of the services' functionality in their own apps.  The Twitter API, for instance, permits access to the tweets sent by any specific user, those containing a specific keyword or even a combination of KWs, those sent on a specific topic, within a particular time window, etc.

In order to access Twitter data programmatically, we will create an account and then a small app that will interact with the Twitter API.  A preliminary step is to implement OAuth (Open Authorization) as its standard authentication mechanism.  We need four primary identifiers for an OAuth workflow:

* consumer key, 
* consumer secret, 
* access token, and 
* access token secret. 
**Warning**: These are application settings that should always be kept private.

Luckily, the Python ecosystem has already well-established libraries for most social media platforms, that come with an implementation of those platform’s authentication processes.

The first step in this homework is therefore the registration of your app. In particular, you need to point your browser to `http://apps.twitter.com`, log-in to Twitter and register a new application. You will receive a **Consumer Key** and a **Consumer secret**. From the configuration page "Keys and Access Token" of your App, you can also obtain the **Access Token** and a **Access Token Secret**. Save this information so you can keep up with your lab tasks.<BR>
Note that you will need a Twitter account in order to login, create an app, and get these credentials.

###  Pre-lab
#### PL task 1: Install Anaconda
Download and install Anaconda in your local host following Tutorial 4 ([Python Development Environment Quick Start](https://github.com/jorditorresBCN/Quick-Start/blob/master/Python-Development-Environment-Quick-Start.md)). Start a Jupyter notebook on your terminal and create a notebook that contains your previous [`guess_nbr.py`](https://github.com/jorditorresBCN/Assignments-2017/blob/master/Lab01.md) code including some explanation of your steps using `markdown` cells. Save your notebook as `guess_nbr.ipynb` and add it to your remote Git repo.

#### PL-task 2: Register your App on Twitter  
Cloud applications are characterized by an increased focus on user participation and content creation. There are also interactions and interconnections between applications sharing content from different types of services.  In order to show how to integrate multiple systems together, we focus on a few “Application Programming Interfaces” (API).

### Lab Tasks

#### Task 1: Get Started with NLTK
One of the most popular packages in Python for NLP is the Natural Language ToolKit ([NLTK](http://www.nltk.org)). The toolkit provides a friendly interface for many of the common NLP tasks, as well as lexical resources and linguistic data.

Tokenization is one of the most basic, yet most important, steps in text analysis required in the following task. The purpose of tokenization is to split a stream of text into smaller units called tokens, usually made up of words. For this purpose, we will use NLTK.

```
import nltk
```
A difference between NLTK and many other packages is that this framework also comes with linguistic data for specific tasks. Given their size, such data is not included in the default installation, but has to be downloaded separately. For this reason, after importing NLTK, we need download NLTK Data which include a lot of corpora, grammars, models, etc. You can find the complete nltk data list [here](http://nltk.org/nltk_data/). You can downloaded all nltk resources by `nltk.download('all')` but it takes ~3.5G. For english text we could use `nltk.download('punkt')` to download the NLTK data package that includes a pre-trained tokenizer for English.

Let’s see the example using the NLTK to tokenize the book [First Contact with TensorFlow](http://www.jorditorres.org/Tensorflow)(`FirstContactWithTensorFlow.txt`could be downloaded from this github) and outputs the 10 most common words in the book.
```
import nltk
nltk.download('punkt') 
import string

from collections import Counter

def get_tokens():
   with open('FirstContactWithTensorFlow.txt', 'r') as tf:
    text = tf.read()
    tokens = nltk.word_tokenize(text)
    return tokens

tokens = get_tokens()
count = Counter(tokens)
print count.most_common(10)
```
##### Task 1.1: Word Count 1
Create a notebook with the name `Lab2.WordCountWithNLTK.ipynb`, that computes and prints the 10 most common words in the book.

##### Task 1.2: Word Count 2
Add a new code cell into the same notebook with the code that computes and prints the total number of word of this book.   


##### Task 1.3: Remove puntuation
We can see that punctiation are many of the most common words. We can remove the punctuation using the character deletion step of translate method as:

```
    lowers = text.lower()
    no_punctuation = lowers.translate(None, string.punctuation)
    tokens = nltk.word_tokenize(no_punctuation)
```
Add a new code cell to the same notebook with the code (and the comments with markdown cells if you consider interesting) that computes and prints the 10 most common words without punctuation characters. 
    
##### Task 1.4: Stop Words
Is not "Tensorflow" the most commond word? Why? What are Stop Words? Include your answer in a markdown cells in the same notebook.

When we are working with text mining applications, we often hear of the term “Stop Word Removal". We can do it using the same `nltk` package: 
```
from nltk.corpus import stopwords
tokens = get_tokens()
filtered = [w for w in tokens if not w in stopwords.words('english')]
count = Counter(filtered)
```
Add a new code cell to the same notebook with the code (and the comments with markdown cells if you consider interesting)  that computes and prints the 10 most common word after removing the stop words.  Now it make more sense, right? "TensorFlow" is the most common word!

#### Task 2: Getting Started with `tweepy`

In this task we will use `tweepy` package as a tool to access Twitter data in a fairly easy way with Python. There are different types of data we can collect, however we will focus on the “tweet” object.

##### Task 2.1: The Twitter API
We already registered our App on Twitter in order to access Twitter data. However, the Twitter API limits access to applications. You can find more detail in [the official documentation](https://dev.twitter.com/rest/public/rate-limiting). Generally different APIs have different [rate limits](https://dev.twitter.com/rest/public/rate-limiting). The implications of hitting the API limits is that Twitter will return an error message rather than the data for which we ask. Ignoring such an error message and performing more requests to the API, may lengthen the time required to obtain a renewed regular access.  Twitter may also flag you as a potential abuser.  If your application needs many API requests pace it the best you can, e.g. with the `time` library and its (`time.sleep()` method. 

There are two types of Twitter APIs: a **REST API** and a **Streaming API**. 
- The Twitter REST API only allows you to go back in time and to mine tweets that have already been published. The API may limit the amount of tweets you can retrieve, not just in terms of rate limits as mentioned, but also in terms of time span. In fact, it's usually only possible to go back in time up to approximately one week on Twitter. The REST API offer no guarantee when you need to mine Twitter exhaustively.   A REST API is generally useful when we want to search for tweets authored by a specific user or when we need to access our own timeline.

- Streaming APIs looks into the future. They retrieve any tweet  as they are published, as long as they match your criteria.  They are useful when we want to filter a particular keyword and download a massive amount of tweets about it.

##### Task 2.2: Accessing your twitter account information 

In order to interact with the Twitter APIs, we need a Python client that implements the different calls to the API itself. There are several options as we can see from the [official documentation](https://dev.twitter.com/resources/twitter-libraries). We will chose for this lab [Tweepy](http://tweepy.readthedocs.io/en/v3.5.0/).
The easiest way to install the latest version is by using pip/easy_install to pull it from [PyPI](https://pypi.python.org/pypi) to your local directory:

```
torres@vm:~$  pip install tweepy
```
You may also use Git to clone the repository from Github and install it manually:


```
torres@vm:~$  git clone https://github.com/tweepy/tweepy.git
torres@vm:~$  cd tweepy
torres@vm:~$  python setup.py install
```
Create a notebook with the name `Lab2.TweepyAPI.ipynb` to keep track of all your work.

In order to authorise our app to access Twitter on our behalf, we need to use the OAuth interface:

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
The `api` variable is now our entry point for most of the operations with Twitter. 

Tweepy provides access to the well documented Twitter API. With tweepy, it's possible to get any object and use any method that the official Twitter API offers. For example, a User object has its documentation at https://dev.twitter.com/docs/platform-objects/users and following those guidelines, tweepy can get the appropriate information.

Main Model classes in the Twitter API are: `Tweets`, `Users`, `Entities` and `Places`. 

in order to be sure that everything is correctly installed print the main information of your Twitter account. After create the user object, the `me()` method returns the user whose authentication keys were used:
```
user = api.me()
 
print('Name: ' + user.name)
print('Location: ' + user.location)
print('Friends: ' + str(user.followers_count))
print('Created: ' + str(user.created_at))
print('Description: ' + str(user.description))
```
Is the data printed correctly? Is it yours? 

##### Task 2.3: Accessing Tweets
Tweepy provides the convenient Cursor interface to iterate through different types of objects. For example, we can read our own Twitter home timeline with (we are using 1 to limit the number of tweets we are reading and only reading the `text` of the tweet):

```
for status in tweepy.Cursor(api.home_timeline).items(1):
    print(status.text) 
```
The `status` variable is an instance of the `Status()` class, a nice wrapper to access the data. The JSON response from the Twitter API is available in the attribute _json (with a leading underscore), which is not the raw JSON string, but a dictionary.
```
import json

for status in tweepy.Cursor(api.home_timeline).items(1):
    print(json.dumps(status._json, indent=2))
    
```
What if we want to have a list of 10 of our friends? 
```
for friend in tweepy.Cursor(api.friends).items(1):
    print(json.dumps(friend._json, indent=2))

```
And how about a list of some of our tweets?

```
for tweet in tweepy.Cursor(api.user_timeline).items(1):
    print(json.dumps(tweet._json, indent=2))
```    
As a conclusion, you can notice that with `tweepy` we can easily collect all the information and store them in the original JSON format, fairly easy to convert into different data models (many storage systems provide import feature).

Use the previous API presented for obtaining information about your tweets.  Keep track of your executions and comments in the   `Lab2.TweepyAPI.ipynb` notebook.

<a name="preproc"/>

## Task 2.3:  Tweet pre-processing
In these tasks we’ll enter in more detail to the overall structure of a tweet and discuss how to pre-process its text before we can get into some more interesting analysis in the next Lab. In particular, we will seen how tokenisation, despite being a well-understood problem, can get tricky with Twitter data. After that we’ll discuss the analysis of term frequencies to extract meaningful terms from our tweets. 

The code used in this Lab is using part of the work done by [Marco Bonzanini](https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/)). As Marco indicates, it is far from perfect but it’s a good starting point to become aware of the complexity of the problem, and fairly easy to extend.

Let’s have a look at the structure of the previous tweet that you printed.
The main attributes are the following:

* text: the text of the tweet itself
* created_at: the date of creation
* favorite_count, retweet_count: the number of favourites and retweets
* favorited, retweeted: boolean stating whether the authenticated user (you) have favourited or retweeted this tweet
* lang: acronym for the language (e.g. “en” for english)
* id: the tweet identifier
* place, coordinates, geo: geo-location information if available
* user: the author’s full profile
* entities: list of entities like URLs, @-mentions, hashtags and symbols
* in_reply_to_user_id: user identifier if the tweet is a reply to a specific user
* in_reply_to_status_id: status identifier id the tweet is a reply to a specific status
* \_json: This is a dictionary with the JSON response of the status
* author: The tweet author

As you can see there is a lot of information we can play with. All the \*_id fields also have a \*_id_str counterpart, where the same information is stored as a string rather than a big int (to avoid overflow problems). 

We will focus our task looking for the text of a tweet, breaking it down into words. While tokenisation is a well understood problem with several out-of-the-box solutions from popular libraries, Twitter data pose some challenges because of the nature of the language.
Let’s see the example using the NLTK package previously used to tokenise a fictitious tweet:


```
from nltk.tokenize import word_tokenize

tweet = 'RT @JordiTorresBCN: just an example! :D http://JordiTorres.Barcelona #masterMEI'

print(word_tokenize(tweet))
```
You will notice some peculiarities of twitter that are not captured by a general-purpose English tokeniser like the one from NLTK: @-mentions, emoticons, URLs and #hash-tags are not recognised as single tokens. Right?

Using some code borrowed from [Marco Bonzanini](https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/) we could consider these aspects of the language.

```python
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
 
tweet = 'RT @JordiTorresBCN: just an example! :D http://JordiTorres.Barcelona #masterMEI'
print(preprocess(tweet))
```

As you can see, @-mentions, URLs and #hash-tags are now preserved as individual tokens. This tokeniser gives you the general idea of how you can do it for twitter text based on regular expressions (regexp), which is a common choice for this type of problem. 

With the previous basic tokenizer code, some particular types of tokens will not be captured, and will be probably broken into several tokens. To overcome this problem you can improve the regular expressions, or employ more sophisticated techniques like [*Named Entity Recognition*](https://en.wikipedia.org/wiki/Named-entity_recognition).

In this example, the regular expressions are compiled with the flags re.VERBOSE, to allow spaces in the regexp to be ignored (see the multi-line emoticons regexp), and re.IGNORECASE to catch both upper and lowercases. The tokenize() function simply catches all the tokens in a string and returns them as a list. This function is used within preprocess(), which is used as a pre-processing chain: in this case we simply add a lowercasing feature for all the tokens that are not emoticons (e.g. :D doesn’t become :d).

Keep track of your executions with different fictitious tweets and comments in the `Lab2.TokenizeTweetText.ipynb` notebook.

Now, we are ready for next Lab, where we will mining streaming twitter data.
