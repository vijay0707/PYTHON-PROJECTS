# WIkipedia Scraper

import wikipedia as wiki

word = input("Enter the word to search:")
print(wiki.search(word))
print(wiki.suggest(word))  #type only some alphabets of its spelling 
print(wiki.summary(word))  #summary of an article on Wikipedia

p = wiki.page(word) #scrape all the information
print(p.title) #To get the Title
print(p.url) #To get the url of the article
print(p.content) #To scrape the full article
print(p.images) #To get all the images in the article
print(p.links)  #To get all the referals used by Wikipedia in the article

# do comment the print statements and run each commands separately to see how it works