import re
import webbrowser
import random
import cloudscraper

def scrapeRandomImage():
    #generate a random page from prnt.sc
    lettersList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    randomLetter1 = random.choice(lettersList)
    randomLetter2 = random.choice(lettersList)
    randomNumber1 = random.randint(1, 9)
    randomNumber2 = random.randint(1, 9)
    randomNumber3 = random.randint(1, 9)
    randomNumber4 = random.randint(1, 9)

    finalUrl = 'https://prnt.sc/' + randomLetter1 + randomLetter2 + str(randomNumber1) + str(randomNumber2) + str(randomNumber3) + str(randomNumber4)

    #webbrowser.open(finalUrl)

    #get the image from the page
    scraper = cloudscraper.create_scraper()
    page = scraper.get(finalUrl)
    content = page.text

    #get all the images from the page
    #looking for <img class="no-click screenshot-image" src="https://image.prntscr.com/image/XG0qZy2_RnKPG_53AjeIVA.png"
    imageRegex = re.compile(r'<img class="no-click screenshot-image" src="(.*?)"')
    imageList = imageRegex.findall(content)

    #print(content)
    #print (imageList)

    #get the first image from the list
    imageUrl = imageList[0]

    #open the image in a browser
    webbrowser.open(imageUrl)

def main():
    scrapeRandomImage()

main()