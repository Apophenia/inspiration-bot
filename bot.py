import random
import zulip

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

client.call_on_each_message(respond)
