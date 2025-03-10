import requests
from bs4 import BeautifulSoup
import pprint

# Path to your custom CA bundle file
ca_bundle_path = r"C:\Users\TobarrP\cacert.pem"

url = "https://news.ycombinator.com/news"  # API endpoint URL

# Make a GET request to the API endpoint with headers
res = requests.get(url, verify=ca_bundle_path)

print()

# print(res)
# print()
# print(res.text)

# Parse the HTML content
soup = BeautifulSoup(res.text, "html.parser")

# find the link to the next page
next_link = soup.find("a", class_="morelink")
if next_link:
    next_page_url = next_link["href"]
    url2 = f"https://news.ycombinator.com/{next_page_url}"
    res2 = requests.get(url2, verify=ca_bundle_path)
    page_2_soup = BeautifulSoup(res2.text, "html.parser")    
else:
    print("No link to the next page found")

# print(soup)

# print(soup.body)

# print(soup.body.contents) # Returns a list of all the children of the body tag in a list

# print(soup.find_all("div")) # Returns a list of all the div tags in the HTML content in a list

# print(
#     soup.find_all("a")
# )  # Returns a list of all the anchor tags in the HTML content in a list - all the links in the page 'a' tags

# print(soup.title)  # Returns the title tag in the HTML content

# print(soup.a) # Returns the first anchor tag in the HTML content

# print(soup.find("a")) # Returns the first anchor tag in the HTML content

# print(soup.find(id="score_42330055")) # Returns the element with the id

"""
Heads up! In the next video we will learn about selectors and we are going to use the Hackernews website to select some stories. 
Hackernews now uses the .titleline class instead of the .storylink class so you just need to make sure you enter .titleline in the next video 
when you see me use .storylink

Finally, in the code attached I use .titleline > a because the link is now inside the first <a> tag under the titleline element. 
"""

# CSS Selectors - to select different complicated nested elements in the HTML content

# print(soup.select('a')) # Returns a list of all the anchor tags in the HTML content in a list - all the links in the page 'a' tags

# print(soup.select(".score")) # Returns a list of all the elements with the class score in the HTML content in a list

# print(soup.select("#score_42330055")) # Returns the element with the id

# print(soup.select(".titleline")) # Returns a list of all the elements with the class storylink in the HTML content in a list

# print(
#     soup.select(".titleline")[0]
# ) # Returns the first element with the class storylink in the HTML content

page_1_links = soup.select(".titleline")  # Returns a list of all the elements with the class storylink in the HTML content in a list
page_2_soup_links = page_2_soup.select(".titleline")  # Returns a list of all the elements with the class storylink in the HTML content in a list
links = page_1_links + page_2_soup_links

# votes = soup.select(".score")  # Returns a list of all the elements with the class score in the HTML content in a list
page_1_subtext = soup.select(".subtext")  # Returns a list of all the elements with the class subtext in the HTML content in a list
page_2_soup_subtext = page_2_soup.select(".subtext")  # Returns a list of all the elements with the class subtext in the HTML content in a list
subtext = page_1_subtext + page_2_soup_subtext

# print(votes[0])  # Returns the first element with the class score in the HTML content

# print(votes[0].get("id"))  # Returns the id attribute of the first element with the class score

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k["votes"], reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()  # Get the text of the link
        # title = item.getText()

        href = (
            links[idx].find("a").get("href", None)
            # item.find("a").get("href", None)
        )  # Get the href attribute of the link

        votes = subtext[idx].select(".score")
        if len(votes):
            points = int(votes[0].getText().replace(" points", ""))            

        if points > 99:
            hn.append({"title": title, "link": href, "votes": points})
    # return hn
    return sort_stories_by_votes(hn)

# print(create_custom_hn(links, subtext))
pprint.pprint(create_custom_hn(links, subtext))

# print(int(votes[0].getText().replace(" points", "")))

print()
