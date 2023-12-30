from bs4 import BeautifulSoup
import requests

## Save the HTML content into a variable in text form.
URL = "https://news.ycombinator.com/"
response = requests.get(url=URL).text 

## make soup
soup = BeautifulSoup(response)

## Look for all articles with the `find_all()` function.
## Save them to a list.
articles = soup.find_all(class_="titleline")

## Empty list to use as a container later on.
article_list = []

## Cleaning the data to extract what I'm interested in: the article and its link. 
##I'll access the upvote later.
for article in articles:
    new_idem = [{"article":article.getText(), 
                 "article link":article.find(name="a").get("href")}]
    article_list.append(new_idem)
#print(article_list)

## Find all article upvotes.
## Save them in a list.
article_upvote = soup.find_all(name="span", class_="score")

## Using list comprehension to iterate through the article upvotes list.
## Getting the text, splitting it because I want to extract only the number,
## then converting it into an 'int' type.
article_upvote_value = [int(upv.getText().split(" ")[0]) for upv in article_upvote]
#print(article_upvote_value)

# Explanation of the list comprehension for the 'article_upvote_value' list:
# Using list comprehension to iterate through the article upvotes list.
#article_upvote_value = [int(upvote.getText.split()[0]) for upv in article_upvote]
# - 'upvote.text': Accesses the text content of each upvote element.
# - 'split()': Splits the text into a list of substrings.
# - '[0]': Retrieves the first element of the split list, which contains the upvote number.
# - 'int()': Converts the extracted upvote number from string to integer.



# I need the article upvote index to point to the article in the articles list.
# I want to have the possibility of filtering the articles by relevance.
# So, I will try to resolve it in a simple way by sorting my upvote index list.
upv_list_sort = sorted(article_upvote_value, reverse=True)



# Now that I have my sorted list of upvotes, I can use it to iterate through my articles list
# and create a new list of articles ordered by the relevance of the upvotes.
article_sort_by_relevance = []
for indexing in upv_list_sort:
    upv_index = article_upvote_value.index(indexing)
    #print(f"INDEXING PRINT= {upv_index}")    
    new_order = {
        "article": article_list[upv_index][0]["article"],
         "article link":  article_list[upv_index][0]["article link"],
         "article upvote": indexing}
    article_sort_by_relevance.append(new_order)

## Print the articles sorted by relevance, from the first item to the end'[0:]'.
print(article_sort_by_relevance[0:])





