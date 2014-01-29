import random
import zulip
import string
import os
from itertools import izip
from collections import defaultdict

client=zulip.Client(os.environ['ZULIP_BOT_EMAIL'], os.environ['ZULIP_API_KEY'])

with open("inspirationalquotes.txt") as f:
    flines = [line for line in f]

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

def generate_start():
    parsed = string.split(split_on_punctuation(str(random.choice(flines))))
    return [parsed.pop(0), parsed.pop(0)]

def is_original(chain):
    return chain not in flines
    
def is_valid_chain(chain):
    sentence = join_on_punctuation(" ".join(chain))
    if (chain[-1] == "." and len(chain) > 8 and is_original(sentence)):
            return True
    elif (len(chain) > 45 and is_original(sentence)):
            return True
    else:
            return False

def create_sentence(chain):
    sentence = join_on_punctuation(" ".join(chain))
    if chain[-1] == ".":
        return sentence
    else:
        return sentence + "."

def make_chain(table):
    return make_chain_with_seed(table, generate_start())

def make_chain_with_seed(table, chain):
    if is_valid_chain(chain):
        return create_sentence(chain)

    entry = table[chain[-2], chain[-1]]
    if not entry:
            chain += generate_start()
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
