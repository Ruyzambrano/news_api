import requests
import json
import webbrowser
import tabulate as tb

api_key = input("Enter your news api key: ")

topic = input("What topic are you looking for? ")
if not topic:
    topic = "e"

response = requests.get(f"https://newsapi.org/v2/everything?q=+\"{topic}\"&language=en&sortBy=popularity&pagesize=20&apiKey={api_key}", timeout=10)


if response.status_code == 200:
    data = response.json()
    ticker = {}
    if data["articles"]:
        for count, article in enumerate(data["articles"], 1):
            ticker[count] = article["title"]
        print()
        print(tb.tabulate(ticker.items(), headers=['Articles'], tablefmt="grid", maxcolwidths=(60)))
        choice = input("\nEnter the number of the article you want to read, type 0 to exit: ")
        if choice == "0":
            quit()
        url = data["articles"][int(choice)-1]["url"]

        webbrowser.open(url)
    else:
        print("No articles found.")

else:
    error_message = json.loads(response.text)
    print(f"Error {response.status_code}: "
          f"{error_message.get('message').capitalize()}")
