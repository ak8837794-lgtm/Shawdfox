 # Task 2(Intermediate Level)
#  1. Web Scraper: Extract data from websites using libraries like Beautiful Soup or Scrapy.

import requests
from bs4 import BeautifulSoup

# Step 1: Send a GET request to the website
url = 'https://example-blog.com'
response = requests.get(url)

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Extract data (e.g., article titles)
titles = soup.find_all('h2', class_='post-title')
for title in titles:
    print(title.text.strip())

# scrapy startproject quotes_scraper cd quotes_scraper/
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse) #crapy crawl quotes -o quotes.json


# 2. Hangman: Implement the wordguessing game with visual progress and hints.

import random

# Word list with hints
words_with_hints = [
    ("python", "A popular programming language"),
    ("elephant", "The largest land animal"),
    ("guitar", "A stringed musical instrument"),
    ("satellite", "Orbits planets and helps in communication"),
    ("pyramid", "Ancient Egyptian triangular structure")
]

# Hangman stages
stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

def play_hangman():
    word, hint = random.choice(words_with_hints)
    guessed = ["_"] * len(word)
    attempts = 0
    guessed_letters = set()

    print("🎯 Welcome to Hangman!")
    print(f"💡 Hint: {hint}")

    while attempts < len(stages) - 1 and "_" in guessed:
        print(stages[attempts])
        print("Word:", " ".join(guessed))
        print("Guessed letters:", ", ".join(sorted(guessed_letters)))
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Please enter a single alphabet.")
            continue

        if guess in guessed_letters:
            print("🔁 You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
            print("✅ Good guess!")
        else:
            attempts += 1
            print("❌ Wrong guess!")

    # Final state
    print(stages[attempts])
    if "_" not in guessed:
        print("🎉 Congratulations! You guessed the word:", word)
    else:
        print("💀 Game Over! The word was:", word)

# Run the game
if __name__ == "__main__":
    play_hangman()




