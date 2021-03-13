# -*- coding: utf-8 -*-
# Release Version: 1.0
# beta_1.0: release
# beta_1.1: less cluttering
# beta_1.2: added random doujin
# beta_1.3: fetching reworked
# beta_1.4: fixed a few bugs such as: ascii/int32 exception and bad naming protocols lmao
# 1.0: rewrote the entire doujin variable accessing due to the switch from using dictionary to dataclass in the fetching module and some minor changes

import nhentai

Nhentai = nhentai.NHentai()

# Todo: add this obfuscation thing
# def ReplaceTags():
    # global doujintags
    
def printrDoujin():
    global rdoujin
    # Add "#" before the command that you don't want to be executed.
    print("")
    #print("Seed number: " + str(doujin.id), end="\n")
    #print("Adventure Title: " + str(doujin.title), end="\n")
    #print("Also known as (might not display properly): " + str(doujin.secondary_title), end="\n")
    #print("Guide(s): " + str(doujin.artists), end="\n")
    #print("List of things you've done: " + str(doujin.tags), end="\n")
    #print("Journey's written language(s): " + str(doujin.languages), end="\n")
    #print("Journey book's classification: " + str(doujin.categories), end="\n")
    #print("Guild: " + str(doujin.groups), end="\n")
    #print("Party members: " + str(doujin.characters), end="\n")
    #print("Adventure parody: " + str(doujin.parodies), end="\n")
    #print("The number of pages of the book: " + str(doujin.total_pages), end="\n")
    print(doujin)
    print("")

def printDoujin():
    global doujin
    if doujin != None:
        # Add "#" before the command that you don't want to be executed.
        print("")
        #print("Seed number: " + str(doujin.id), end="\n")
        print("Adventure Title: " + str(doujin.title), end="\n")
        #print("Also known as (might not display properly): " + str(doujin.secondary_title), end="\n")
        print("Guide(s): " + str(doujin.artists), end="\n")
        print("List of things you've done: " + str(doujin.tags), end="\n")
        print("Journey's written language(s): " + str(doujin.languages), end="\n")
        #print("Journey book's classification: " + str(doujin.categories), end="\n")
        print("Guild: " + str(doujin.groups), end="\n")
        print("Party members: " + str(doujin.characters), end="\n")
        print("Adventure parody: " + str(doujin.parodies), end="\n")
        print("The number of pages of the book: " + str(doujin.total_pages), end="\n")
        #print(doujin)
        print("")
    else:
        print("You went adventuring and you found... absolutely nothing. Try again with a better seed, nub.")


print("Welcome to the adventure simulator! Type in a seed number to go explore!")
print("Type 'quit' to quit the program!")
print("Type 'random' to use a random seed!")
while True:
    searchID = input("Enter the seed number: ")
    try:
        if __name__ == '__main__':
            doujin: dict = Nhentai._get_doujin(id=int(searchID))
            #ReplaceTags()
            printDoujin()
    except ValueError:
        if(searchID == "quit"):
            break
        elif(searchID == "random"):
            doujin: dict = Nhentai.get_random()
            printrDoujin()
        else:
            print("Bad input.")
            continue















# lmao actually reading until the end? you're cool.