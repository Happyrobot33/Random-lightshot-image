import webbrowser
import random

#generate a random page from prnt.sc
lettersList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
randomLetter1 = random.choice(lettersList)
randomLetter2 = random.choice(lettersList)
randomNumber1 = random.randint(1, 9)
randomNumber2 = random.randint(1, 9)
randomNumber3 = random.randint(1, 9)
randomNumber4 = random.randint(1, 9)

finalUrl = 'https://prnt.sc/' + randomLetter1 + randomLetter2 + str(randomNumber1) + str(randomNumber2) + str(randomNumber3) + str(randomNumber4)

webbrowser.open(finalUrl)