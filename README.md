Inspiration Bot
=========

Inspiration Bot is a bot designed for use on the workplace chat app [Zulip]. It currently resides on the Hacker School network, and will spew a nonsensical inspirational quote via private message at anyone who sends it a private message. It could certainly be fed different input text for a different effect.

Version
----

1.0

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


License
----
MIT

[Zulip]:http://zulip.com/hello
[Zulip API]:http://zulip.com/api
