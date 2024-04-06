from bs4 import BeautifulSoup
import requests


url = 'https://dota2.fandom.com/wiki/Category:Hero_icons'
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
allBlocks = soup.findAll(class_='gallery mw-gallery-traditional')
#bg-main-block base-hero__wrap
#base-hero__block
blocks = []
heroes = []

for block in allBlocks:
    _allBlocks = block.findAll(class_='gallerybox')
    for blk in _allBlocks:
        blocks.append(blk)

for block in blocks:
    gallerytext = block.find(class_='galleryfilename galleryfilename-truncate')
    _heroName = gallerytext.text
    galleryimage = block.find(class_='image')
    _heroImg = galleryimage.get('href')

    heroes.append({"name":_heroName, "img":_heroImg})

#wikiUrl = 'https://dota2.fandom.com/Dota_2_Wiki?file='

for hero in heroes:
    #@_url = wikiUrl + hero['img']
    p = requests.get(hero['img'])
    _heroName = hero['name']
    #_heroName = _heroName.replace(".png", "")
    out = open(f"C://Users//1вин//Documents//projs//my1stProject//dotaheroes//{_heroName}", "wb")
    out.write(p.content)
    out.close()

    print(_heroName)
    
    