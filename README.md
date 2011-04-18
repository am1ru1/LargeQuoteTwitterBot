What is LargeQuoteTwitterBot?
=
LargeQuoteTwitterBot is, at the moment, 2 python scripts that use the Twitter api, through the library Tweepy which is availiable [here](https://github.com/joshthecoder/tweepy).

[quoteDeck.py](https://github.com/MikeNaylor/LargeQuoteTwitterBot/blob/master/quoteDeck.py) is a script that, when run, takes a random line from a .txt file and tweets it. If the quote is too big for twitter, it will tweet it in however many tweets necessary, in reverse order as to preserve readability. For example the following quote:

>This quote is far too long for a tweet, far too long. The verbose nature of the aforementioned quote renders it unable to conform to the Twitter character limit of 140. Alas, this shall quote shall take up 2 tweets.

Will be tweeted as tweet 1:

>Twitter character limit of 140. Alas, this shall quote shall take up 2 tweets.

Tweet 2:

>This quote is far too long for a tweet, far too long. The verbose nature of the aforementioned quote renders it unable to conform to the...

Thus, this will appear on the twitter feed as:

>This quote is far too long for a tweet, far too long. The verbose nature of the aforementioned quote renders it unable to conform to the...

>Twitter character limit of 140. Alas, this shall quote shall take up 2 tweets.

[botSay.py](https://github.com/MikeNaylor/LargeQuoteTwitterBot/blob/master/quoteDeck.py) is a script that when run with a string argument, will tweet the argument. For example, the command line command:

> $ python botSay.py 'This is a tweet, to be tweeted'

Will tweet:

>This is a tweet, to be tweeted

Multi-tweet capabilities for 140+ character string arguments is not yet implemented.

##Setup

###Installing Tweepy:

- easy_install tweepy

or source code from Git

1. git clone git://github.com/joshthecoder/tweepy.git
2. cd tweepy
3. python setup.py install

###Registering With Twitter Dev To Get Keys:

Firstly, go to the [Twitter Dev new application form](https://dev.twitter.com/apps/new) and register your application. Fill in the fields how you wish (note that your application name determines what your tweets will come from. e.g 2 minutes ago via QuoteDeck). Ensure that the application type is Client and that it has Read & Write access.

You will be presented with this page:

![Your application keys](http://i.imgur.com/lvGri.jpg)

Take your Consumer Key and Consumer Secret code and run the accessKeys.py script, passing your keys as below:

> $ python accessKeys.py 'Your Consumer Key' 'Your Consumer Secret'

> Authorization url: http://api.twitter.com/oauth/authorize?oauth_token=kU29aUKmBhpgMSXk7T20wYPlEMg063n3TdP7pwvHhw

> Verification PIN:

Go to the authorization url the script returns and you will be presented with this page:

![Authorization page](http://i.imgur.com/v1zlM.jpg)

Sign into the twitter account you wish the bot to use, and click Allow. You will be presented with this page:

![Your PIN number](http://i.imgur.com/f50Cs.jpg)

Simply enter the PIN that is returned into the script, as below:

> Verification PIN: YourPIN

> Your ACCESS_KEY = 'Your Access Key'

> Your ACCESS_SECRET = 'Your Access Secret'

Make a note of these 2 keys. Open up quoteDeck.py in a prefered text editor and fill in the CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY and ACCESS_SECRET with ther relevant information. Your bot is now set up to tweet to the linked account, using a .txt file of quotes (1 quote per line). Fill in the FILE_TO_USE field with the location of your quotes file. Your bot is now set up. To run it, simply run:

> $ python quoteDeck.py

##To-Do

- Multi-line capabilities for botSay

- Perhaps introduce a module that, when the bot is run, follows all unfollowed people that follow the bot

- Perhaps incorporate botSay into quoteDeck as a parameter passed when running the script

- For better user friendliness and flexibility use a config file for keys instead of having the user alter the script code itself.

- Move quotes from a text file to a SQLite3 database and use the package sqlite3 in the standard library to manipulate them. This would improve scalability and allow for relational databases, such that a database of used quotes could be kept (using foreign keys), and wiped at certain time periods (perhaps once a week) in order to reduce potential quote repetition.

- Ensure all code meets PEP 8 standards.
