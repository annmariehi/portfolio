from random import randint
import time
from quote_list import quotes #importing list of quotes

#can add or remove quote from quote_list without disrupting program
min = 0
max = len(quotes) - 1

#prints a new quote in random order from quote_list to quote.txt every second
while True:
    randNum = randint(min, max)
    randQuote = quotes[randNum]
    file1 = open("quote.txt", "w", encoding="utf-8")
    file1.write(randQuote)
    file1.close
    time.sleep(1)


