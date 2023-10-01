import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_Regional_Transport_Office_districts_in_India'

# get contents from url
website_content = requests.get(url).content

soup = BeautifulSoup(website_content,'lxml')

# all_tables = soup.findAll('table')

# find all the references
ref_tags = soup.findAll('table', { 'class' : 'wikitable' })


sample_json = []

# Find all td inside the table
ite = 0
for i,ref_tag in enumerate(ref_tags):
    all_td_data = ref_tag.findAll('td')
    # my_string = ','.join(all_td_data.text)

    sample_json.append({'id': i+1, 'code': all_td_data[0].text.replace('\n', ''), 'area': all_td_data[1].text.replace('\n', ''), 'jurisdiction_area': all_td_data[2].text.replace('\n', '')})
    # print(f'i: {i}')
    print(f'data: {all_td_data}')
    ite += 1

print(sample_json)
    # for eachTD in all_td_data:
    #     print(f'eachTD- {eachTD}')

    # print(f'data: {my_string}')
    # print(f'ref_tag: {ref_tag}')

# td_tags = ref_tags.findAll('td')

# iterate through the ResultSet
# for i,ref_tag in enumerate(ref_tags):
#     print(f'i: {i}')
#     print(f'ref_tag: {ref_tag}')

    # print text only
    # print('[{0}] {1}'.format(i,ref_tag.text))

# print(all_tables)


# Countries = []
# for link in links:
#     Countries.append(link.get('title'))
#
# print(Countries)

# print(soup.prettify())
