# Use a quotes API, e.g. https://zenquotes.io/api/random
# to fetch a random quote. Then use string manipulation to convert it to
# Doge speech (https://en.wikipedia.org/wiki/Doge_(meme))
# Create a tiny webpage that displays a doge image together
# with the altered quote. You can get an image URL from another API:
# https://dog.ceo/api/breed/shiba/images/random
# Write the code logic to make the API calls and assign the output to
# `doged_quote` and `doge_image_url` respectively.
# Then write the `html` string to a `.html` file and look at it in your browser.

import requests
import random
import webbrowser

# Doge-style prefixes
doge_prefixes = ["such", "very", "much", "so", "many", "wow"]

# Quote
quote_data = requests.get("https://zenquotes.io/api/random").json()
quote = quote_data[0]["q"]
author = quote_data[0]["a"]

# Doge-ify it
words = quote.split()
doge_words = [f"{random.choice(doge_prefixes)} {word.lower()}" for word in words[:6]]
doged_quote = "<br>".join(doge_words) + "<br>wow."

# Image
doge_image_url = requests.get("https://dog.ceo/api/breed/shiba/images/random").json()["message"]

html = f"""
<!DOCTYPE html>
<html>
<head><title>Doge Quote</title></head>
<body style="text-align:center;font-family:'Comic Sans MS';background:#fef9e7;">
    <img src="{doge_image_url}" style="max-width:400px;border-radius:20px;box-shadow:0 0 20px #aaa;">
    <div style="font-size:24px;color:#4a235a;margin-top:20px;">{doged_quote}</div>
    <p>– {author}</p>
</body>
</html>
"""

with open("doge_quote.html", "w", encoding="utf-8") as file:
    file.write(html)

# 6. Ask before opening
if input("Open in browser? (y/n): ").lower() == "y":
    webbrowser.open("doge_quote.html")

