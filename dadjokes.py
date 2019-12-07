import requests
from termcolor import colored
import pyfiglet
from random import randint

#title of program is formatted and printed
title_string = 'Dad Jokes ! !'

text = pyfiglet.figlet_format(title_string)

title = colored(text, color='cyan', on_color='on_white', attrs=['blink'])
print(text)

#prompt to get topic from user
topic = input('Want to here a joke? Give me a topic: ')

url = "https://icanhazdadjoke.com/search"

#gets response from dad joke api
response = requests.get(
    url,
    headers={"Accept":"application/json"},
    params={"term": topic})

#converts json data to python dictionary
data = response.json()

#grabs number of jokes in query
num_jokes = data['total_jokes']

if num_jokes == 0:
    print("There are no jokes about {}".format(topic))
else:
    #index of joke chosen
    random_num = randint(0, num_jokes)
    if num_jokes == 1:
        print("I've got one joke about {}. Here it is: \n{}".format(topic, data['results'][0]['joke']))
    else:
        print("I've got {} jokes about {}. Here's one: \n{}".format(num_jokes, topic, data['results'][random_num]['joke']))


