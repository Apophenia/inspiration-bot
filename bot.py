import random
import zulip
import string
from itertools import izip
from collections import defaultdict

client=zulip.Client()

f = open("inspirationalquotes.txt")
flines = f.readlines()

def respond(message):
    if message['type'] == 'private' and message['sender_email'] != 'bot@bot-email':
        client.send_message({
            'type':'private',
            'to': message['sender_email'],
            'content': 'Dear ' + message['sender_full_name'] + ',\r\n' + str(random.choice(flines))
        })

def make_table(text):
    parsed = string.split(text)
    table = defaultdict(list)
    for a, b, c in izip(parsed, parsed[1:], parsed[2:]):
        table[(a,b)].append(c)
    return table

print make_table("i love pairing with zach and also mary and also alan!")
client.call_on_each_message(respond)
