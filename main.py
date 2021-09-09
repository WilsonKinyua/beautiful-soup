from bs4 import BeautifulSoup
# with open('website.html') as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, 'html.parser')

# # print(soup.title)

# all_achor_tags = soup.find_all(name='p')

# # print(all_achor_tags)

# # for tags in all_achor_tags:
# #     print(tags.text)

# the_heading_with_id = soup.find_all(name='h1',id="heading")
# print(the_heading_with_id)


# # selecting a specific tag inside a tag

# company_url = soup.select_one(selector='p a ')



# ================ Getting data from a live site ========================
import requests

reponse = requests.get('https://news.ycombinator.com/newest')

the_website = reponse.text

soup = BeautifulSoup(the_website,"html.parser")

all_links_heading = soup.select(selector=".storylink")

for links in all_links_heading:
    print(links.text)