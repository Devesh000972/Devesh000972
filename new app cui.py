import requests

url = "https://newsapi.org/v2/top-headlines"
params = {"country": "us", "apiKey": "014d6c87d703491983e3b6da76401ff8"}

response = requests.get(url, params=params)
data = response.json()

# Print the total number of articles found
total_results = data["totalResults"]
print(f"Total results: {total_results}")

# Ask the user which article they want to read
article_num = int(input(f"Enter the article number you want to read (1-{total_results}): "))

# Make sure the article number is valid
if article_num < 1 or article_num > total_results:
    print("Invalid article number")
else:
    # Print the title and description of the selected article
    article = data["articles"][article_num - 1]
    print(f"Title: {article['title']}")
    print(f"Description: {article['description']}")
