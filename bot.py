import random
import zulip
import string
import os
from itertools import izip
from collections import defaultdict

client=zulip.Client(os.environ['ZULIP_BOT_EMAIL'], os.environ['ZULIP_API_KEY'])

with open("inspirationalquotes.txt") as f:
    fstring = f.read()

flines = [line for line in fstring.split('\n')]

def main():
    table = make_table(split_on_punctuation(fstring))
    client.call_on_each_message(lambda message: respond(message, table))

def split_on_punctuation(text):
    return text.replace("."," . ").replace(","," ,")

def join_on_punctuation(text):
    return text.replace(" .",".").replace(" ,",",")

def make_table(text):
    parsed = string.split(text)
    table = defaultdict(list)
    for a, b, c in izip(parsed, parsed[1:], parsed[2:]):
        table[(a,b)].append(c)
    return table

def initialize():
    parsed = string.split(split_on_punctuation(str(random.choice(flines))))
    return [parsed.pop(0), parsed.pop(0)]

def is_original(chain):
    for i in flines:
        if (chain == i):
            return False
    return True

def make_chain(table):
    return make_chain_with_seed(table, initialize())

def make_chain_with_seed(table, chain):
    if (chain[-1] == "." and len(chain) > 8 and is_original(join_on_punctuation(" ".join(chain)))):
        return join_on_punctuation(" ".join(chain))
    elif ((len(chain) > 45) and (is_original(join_on_punctuation(" ".join(chain)) + "."))):
        return join_on_punctuation(" ".join(chain)) + "."
    else:
        entry = table[chain[-2], chain[-1]]
        if entry == []:
            return make_chain_with_seed(table, chain + initialize())
        else:
            chain.append(random.choice(entry))
            return make_chain_with_seed(table, chain)

def respond(message, table):
    if message['type'] == 'private' and message['sender_email'] != os.environ['ZULIP_BOT_EMAIL']:
            client.send_message({
                'type':'private',
                'to': message['sender_email'],
                'content': 'Dear ' + message['sender_full_name'] + ',\r\n' + unicode(make_chain(table), encoding='utf-8')
            })

if __name__ == "__main__":
    main()
