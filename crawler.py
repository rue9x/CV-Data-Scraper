# 2021 Rue Lazzaro
# Deixadilson Castlevania data scraper.
# Made for Castlevania MUD. Nobody else had the STR/DEF stats. :(

from urllib.request import urlopen
import os
import sys
import html2text

def savePage(url, pagefilename='page'):
    text_maker = html2text.HTML2Text()
    text_maker.ignore_links = True
    text_maker.ignore_images = True
    page = urlopen(url)
    html = page.read()
    text = text_maker.handle(str(html, encoding = "utf-8"))
    text = text.split("* * *")
    text = text[1]
    file = open(pagefilename, 'w')
    file.write(text)
    file.close()
if __name__ == "__main__":
    pagelist= [
        "https://www.deixadilson.com/enemies/Dracula",
        "https://www.deixadilson.com/enemies/Blood-Skeleton",
        "https://www.deixadilson.com/enemies/Bat",
        "https://www.deixadilson.com/enemies/Stone-Skull",
        "https://www.deixadilson.com/enemies/Zombie",
        "https://www.deixadilson.com/enemies/Merman2",
        "https://www.deixadilson.com/enemies/Skeleton",
        "https://www.deixadilson.com/enemies/Warg",
        "https://www.deixadilson.com/enemies/Bone-Scimitar",
        "https://www.deixadilson.com/enemies/Merman3",
        "https://www.deixadilson.com/enemies/Spittle-Bone",
        "https://www.deixadilson.com/enemies/Axe-Knight4",
        "https://www.deixadilson.com/enemies/Bloody-Zombie",
        "https://www.deixadilson.com/enemies/Slinger",
        "https://www.deixadilson.com/enemies/Ouija-Table",
        "https://www.deixadilson.com/enemies/Skelerang",
        "https://www.deixadilson.com/enemies/Thornweed",
        "https://www.deixadilson.com/enemies/Gaibon",
        "https://www.deixadilson.com/enemies/Ghost",
        "https://www.deixadilson.com/enemies/Marionette",
        "https://www.deixadilson.com/enemies/Slogra",
        "https://www.deixadilson.com/enemies/Diplocephalus",
        "https://www.deixadilson.com/enemies/Flea-Man",
        "https://www.deixadilson.com/enemies/Medusa-Head7",
        "https://www.deixadilson.com/enemies/Blade-Soldier",
        "https://www.deixadilson.com/enemies/Bone-Musket",
        "https://www.deixadilson.com/enemies/Medusa-Head8",
        "https://www.deixadilson.com/enemies/Plate-Lord",
        "https://www.deixadilson.com/enemies/Stone-Rose",
        "https://www.deixadilson.com/enemies/Axe-Knight9",
        "https://www.deixadilson.com/enemies/Ctulhu",
        "https://www.deixadilson.com/enemies/Bone-Archer",
        "https://www.deixadilson.com/enemies/Bone-Pillar",
        "https://www.deixadilson.com/enemies/Doppleganger10",
        "https://www.deixadilson.com/enemies/Owl",
        "https://www.deixadilson.com/enemies/Phantom-Skull",
        "https://www.deixadilson.com/enemies/Scylla-wyrm",
        "https://www.deixadilson.com/enemies/Skeleton-Ape",
        "https://www.deixadilson.com/enemies/Spear-Guard",
        "https://www.deixadilson.com/enemies/Spellbook",
        "https://www.deixadilson.com/enemies/Winged-Guard",
        "https://www.deixadilson.com/enemies/Ectoplasm",
        "https://www.deixadilson.com/enemies/Sword-Lord",
        "https://www.deixadilson.com/enemies/Toad",
        "https://www.deixadilson.com/enemies/Armor-Lord",
        "https://www.deixadilson.com/enemies/Corner-Guard",
        "https://www.deixadilson.com/enemies/Dhuron",
        "https://www.deixadilson.com/enemies/Frog",
        "https://www.deixadilson.com/enemies/Frozen-Shade",
        "https://www.deixadilson.com/enemies/Magic-Tome",
        "https://www.deixadilson.com/enemies/Skull-Lord",
        "https://www.deixadilson.com/enemies/Black-Crow",
        "https://www.deixadilson.com/enemies/Blue-Raven",
        "https://www.deixadilson.com/enemies/Corpseweed",
        "https://www.deixadilson.com/enemies/Flail-Guard",
        "https://www.deixadilson.com/enemies/Flea-Rider",
        "https://www.deixadilson.com/enemies/Spectral-Sword13",
        "https://www.deixadilson.com/enemies/Bone-Halberd",
        "https://www.deixadilson.com/enemies/Scylla",
        "https://www.deixadilson.com/enemies/Hunting-Girl",
        "https://www.deixadilson.com/enemies/Mudman",
        "https://www.deixadilson.com/enemies/Owl-Knight",
        "https://www.deixadilson.com/enemies/Spectral-Sword15",
        "https://www.deixadilson.com/enemies/Vandal-Sword",
        "https://www.deixadilson.com/enemies/Flea-Armor",
        "https://www.deixadilson.com/enemies/Hippogryph",
        "https://www.deixadilson.com/enemies/Paranthropus",
        "https://www.deixadilson.com/enemies/Slime",
        "https://www.deixadilson.com/enemies/Blade-Master",
        "https://www.deixadilson.com/enemies/Wereskeleton",
        "https://www.deixadilson.com/enemies/Grave-Keeper",
        "https://www.deixadilson.com/enemies/Gremlin",
        "https://www.deixadilson.com/enemies/Harpy",
        "https://www.deixadilson.com/enemies/Minotaurus",
        "https://www.deixadilson.com/enemies/Werewolf18",
        "https://www.deixadilson.com/enemies/Bone-Ark",
        "https://www.deixadilson.com/enemies/Valhalla-Knight",
        "https://www.deixadilson.com/enemies/Cloaked-Knight",
        "https://www.deixadilson.com/enemies/Fishhead",
        "https://www.deixadilson.com/enemies/Lesser-Demon",
        "https://www.deixadilson.com/enemies/Lossoth",
        "https://www.deixadilson.com/enemies/Salem-Witch",
        "https://www.deixadilson.com/enemies/Blade",
        "https://www.deixadilson.com/enemies/Gurkha",
        "https://www.deixadilson.com/enemies/Hammer",
        "https://www.deixadilson.com/enemies/Discus-Lord",
        "https://www.deixadilson.com/enemies/Karasuman",
        "https://www.deixadilson.com/enemies/Large-Slime",
        "https://www.deixadilson.com/enemies/Hellfire-Beast",
        "https://www.deixadilson.com/enemies/Cerberos",
        "https://www.deixadilson.com/enemies/Killer-Fish",
        "https://www.deixadilson.com/enemies/Olrox",
        "https://www.deixadilson.com/enemies/Succubus",
        "https://www.deixadilson.com/enemies/Tombstone",
        "https://www.deixadilson.com/enemies/Venus-Weed",
        "https://www.deixadilson.com/enemies/Lion",
        "https://www.deixadilson.com/enemies/Scarecrow",
        "https://www.deixadilson.com/enemies/Granfaloon",
        "https://www.deixadilson.com/enemies/Schmoo",
        "https://www.deixadilson.com/enemies/Tin-man",
        "https://www.deixadilson.com/enemies/Balloon-pod",
        "https://www.deixadilson.com/enemies/Yorick",
        "https://www.deixadilson.com/enemies/Bomb-Knight",
        "https://www.deixadilson.com/enemies/Flying-Zombie",
        "https://www.deixadilson.com/enemies/Bitterfly",
        "https://www.deixadilson.com/enemies/Jack-O'Bones",
        "https://www.deixadilson.com/enemies/Archer",
        "https://www.deixadilson.com/enemies/Werewolf34",
        "https://www.deixadilson.com/enemies/Black-Panther",
        "https://www.deixadilson.com/enemies/Darkwing-Bat",
        "https://www.deixadilson.com/enemies/Dragon-Rider",
        "https://www.deixadilson.com/enemies/Minotaur",
        "https://www.deixadilson.com/enemies/Nova-Skeleton",
        "https://www.deixadilson.com/enemies/Orobourous",
        "https://www.deixadilson.com/enemies/White-Dragon",
        "https://www.deixadilson.com/enemies/Fire-Warg",
        "https://www.deixadilson.com/enemies/Rock-Knight",
        "https://www.deixadilson.com/enemies/Sniper-Of-Goth",
        "https://www.deixadilson.com/enemies/Spectral-Sword36",
        "https://www.deixadilson.com/enemies/Ghost-Dancer",
        "https://www.deixadilson.com/enemies/Warg-Rider",
        "https://www.deixadilson.com/enemies/Cave-Troll",
        "https://www.deixadilson.com/enemies/Dark-Octopus",
        "https://www.deixadilson.com/enemies/Fire-Demon",
        "https://www.deixadilson.com/enemies/Gorgon",
        "https://www.deixadilson.com/enemies/Malachi",
        "https://www.deixadilson.com/enemies/Akmodan-II",
        "https://www.deixadilson.com/enemies/Blue-Venus-Weed",
        "https://www.deixadilson.com/enemies/Doppleganger40",
        "https://www.deixadilson.com/enemies/Medusa",
        "https://www.deixadilson.com/enemies/The-Creature",
        "https://www.deixadilson.com/enemies/Fake-Grant",
        "https://www.deixadilson.com/enemies/Fake-Trevor",
        "https://www.deixadilson.com/enemies/Imp",
        "https://www.deixadilson.com/enemies/Fake-Sypha",
        "https://www.deixadilson.com/enemies/Beezelbub",
        "https://www.deixadilson.com/enemies/Azaghal",
        "https://www.deixadilson.com/enemies/Frozen-Half",
        "https://www.deixadilson.com/enemies/Salome",
        "https://www.deixadilson.com/enemies/Richter-Belmont",
        "https://www.deixadilson.com/enemies/Dodo-Bird",
        "https://www.deixadilson.com/enemies/Galamoth",
        "https://www.deixadilson.com/enemies/Guardian",
        "https://www.deixadilson.com/enemies/Death",
        "https://www.deixadilson.com/enemies/Shaft",
        "https://www.deixadilson.com/enemies/Lord-Dracula"
    ]
    for eachURL in pagelist:
        fn = eachURL
        fn = fn.split("/")
        fn = fn[-1]
        fn = "c:\\code\\"+fn + ".txt"
        try:
            savePage(eachURL,fn)
            print ("Saved "+fn)
        except Exception as ExMsg:
            print (ExMsg)
            print ("Failed to save "+fn)
