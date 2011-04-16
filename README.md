What is LargeQuoteTwitterBot?
=
LargeQuoteTwitterBot is, at the moment, 2 python scripts that use the Twitter api, through the library Tweepy which is availiable [here](https://github.com/joshthecoder/tweepy).

[quoteDeck.py](https://github.com/MikeNaylor/LargeQuoteTwitterBot/blob/master/quoteDeck.py) is a script that, when run, takes a random line from a .txt file and tweets it. If the quote is too big for twitter, it will tweet it in however many tweets necessary, in reverse order as to preserve readability. For example the following quote:

>This quote is far too long for a tweet, far too long. The verbose nature of the afformentioned quote renders it unable to conform to the Twitter character limit of 140. Alas, this shall quote shall take up 2 tweets.

Will be tweeted as tweet 1:

>Twitter character limit of 140. Alas, this shall quote shall take up 2 tweets.

Tweet 2:

>This quote is far too long for a tweet, far too long. The verbose nature of the afformentioned quote renders it unable to conform to the...

Thus, this will appear on the twitter feed as:

>This quote is far too long for a tweet, far too long. The verbose nature of the afformentioned quote renders it unable to conform to the...

>Twitter character limit of 140. Alas, this shall quote shall take up 2 tweets.

[botSay.py](https://github.com/MikeNaylor/LargeQuoteTwitterBot/blob/master/quoteDeck.py) is a script that when run with a string argument, will tweet the argument. For example, the command line command:

> $ python botSay.py 'This is a tweet, to be tweeted'

Will tweet:

>This is a tweet, to be tweeted

Multi-tweet capabilities for 140+ character string arguments is not yet implemented.

##Setup

To-do:

-Install tweepy and dependancies

-Register application with Twitter Aps to get the relevant keys

##To-Do

-Multi-line capabilities for botSay

-Perhaps introduce a module that, when the bot is run, follows all unfollowed people that follow the bot

-Perhaps incorporate botSay into quoteDeck as a parameter passed when running the script
