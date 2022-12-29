import json, re

results = []

file_type = input("Depending on file type -> Enter '0' for Twitter OR '1' for Instagram: ")

if file_type =="1": file = './files/instagram.json'
else:
    file = './files/twitter.json'


with open('word_bank.txt') as text_file: 
    text = text_file.read()


word_bank = text.split(" ")
word_bank = set(word_bank)    #O(n)

with open(file, encoding="utf-8") as json_file: 
    jason = json.load(json_file)

if file_type == "1":
    #Instagram
    messages = jason['messages']
    for i in range(len(messages)):
        message = messages[i]["content"]
        clean_message = re.sub(r'[^\w\s]', '', message)   #delete punctuation
        for word in clean_message.split(' '):
            if word in word_bank:
                results.append(message)
else:
    #Twitter
    for i in range(len(jason)):
        tweet = jason[i]["tweet"]["full_text"]
        clean_tweet = re.sub(r'[^\w\s]', '', tweet)   #delete punctuation
        for word in clean_tweet.split(' '):
            if word in word_bank:
                results.append(tweet)

with open('./files/results.txt', 'w+') as txt_file:
    for line in results:
        txt_file.write(line + '\n')


print("Complete!")