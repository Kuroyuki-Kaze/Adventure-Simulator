# -*- coding: utf-8 -*-
# Release Version: beta_1.4
# 1.0: release
# 1.1: less cluttering
# 1.2: added random doujin
# 1.3: fetching reworked
# 1.4: fixed a few bugs such as: ascii/int32 exception and bad naming protocols lmao
import re
import nhentai

# Todo: add this obfuscation thing
# def ReplaceTags():
    # global doujintags
    
def printrDoujin():
    global rdoujin
    global rdoujintags
    global rdoujincategories
    global rdoujinpages
    # Add "#" before the command that you don't want to be executed.
    print("Seed number: " + str(rdoujin['id']) + '\n')
    print("Adventure Title: " + str(rdoujin['title']) + '\n')
    #print("Also known as: " + str(rdoujin['secondary_title']) + '\n')
    print("Guide(s): " + str(rdoujin['artists']) + '\n')
    print("List of things you've done: " + rdoujintags + '\n')
    #print("Journey's written language(s): " + str(rdoujin['languages']) + '\n')
    #print("Journey book's classification: " + rdoujincategories + '\n')
    #print("The number of pages of the Book: " + rdoujinpages + '\n')
    #print(doujin)

def printDoujin():
    global doujin
    global doujintags
    global doujincategories
    global doujinpages
    # Add "#" before the command that you don't want to be executed.
    #print("Seed number: " + str(doujin['id']) + '\n')
    print("Adventure Title: " + str(doujin['title']) + '\n')
    #print("Also known as: " + str(doujin['secondary_title']) + '\n')
    print("Guide(s): " + str(doujin['artists']) + '\n')
    print("List of things you've done: " + doujintags + '\n')
    #print("Journey's written language(s): " + str(doujin['languages']) + '\n')
    #print("Journey book's classification: " + doujincategories + '\n')
    #print("The number of pages of the Book: " + doujinpages + '\n')
    #print(doujin)

Nhentai = nhentai.NHentai()
print("Welcome to the adventure simulator! Type in a seed number to go explore!")
while True:
    searchID = input("Enter the seed number: ")
    try:
        if __name__ == '__main__':
            doujin: dict = Nhentai._get_doujin(id=int(searchID))
            doujintags = str(doujin['tags'])
            doujincategories = re.search(r"\[\'(.*?)\'\]", str(doujin['categories'])).group(1)
            doujinpages = re.search(r"\[\'(.*?)\'\]", str(doujin['pages'])).group(1)
            #ReplaceTags()
        try:
            printDoujin()
        except TypeError:
            print("You went for a walk and then died of exhaustion. Very uncool.")
    except ValueError:
        if(searchID == "quit"):
            break
        elif(searchID == "random"):
            Nhentai = nhentai.NHentai()
            rdoujin: dict = Nhentai.get_random()
            rdoujintags = str(rdoujin['tags'])
            rdoujincategories = re.search(r"\[\'(.*?)\'\]", str(rdoujin['categories'])).group(1)
            rdoujinpages = re.search(r"\[\'(.*?)\'\]", str(rdoujin['pages'])).group(1)
            printrDoujin()
        else:
            print("Bad input.")
            continue
