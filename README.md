Inspiration Bot
=========

Inspiration Bot is a bot designed for use on the workplace chat app [Zulip]. It currently resides on the Hacker School network, and will spew a nonsensical inspirational quote via private message at anyone who sends it a private message. It could certainly be fed different input text for a different effect.

Version
----

1.0

Input text
----
Included in the repository is "inspirationalquotes.txt," which is a newline-delimited file consisting of quotes from Ralph Waldo Emerson's "Self-Reliance." This text results in output that is neither consistently inspirational nor particularly quotable, but it provides a reasonable example of what your input text might look like. 


Ingredients
-----------

* [Zulip API] - Zulip's Python bindings

Installation
--------------
If you'd like to run your own Inspiration Bot, you'll need to:
* Clone this repository
* Manually install the [Zulip API] (as of writing this, the Zulip components cannot be pip-installed)
* Set environment variables 'ZULIP_BOT_EMAIL' and 'ZULIP_API_KEY' to your Zulip bot's email/API key.
* Run bot.py using the Zulip virtual environment.

Thanks
------
Inspiration Bot was my first foray into Python! Many thanks to [Stephen] for inspiring this project, and to [Julia] and other Hacker Schoolers for helping me navigate the tricky parts. 

License
----
MIT

[Zulip]:http://zulip.com/hello
[Zulip API]:http://zulip.com/api
[Stephen]:https://github.com/phsteve
[Julia]:https://github.com/jvns
