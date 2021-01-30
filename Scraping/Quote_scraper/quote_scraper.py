import requests
from bs4 import BeautifulSoup
import random

# ====================================================================================
# ================ Classes ===========================================================
# ************************************************************************************
class Quote:
    def __init__(self, author, text, url):
        self.author = author
        self.text = text
        self.url = url

    def __repr__(self):
        return f'{self.author} said: {self.text} URL: {self.url}'

    def hint(self, guess_num):
        hint_response = requests.get(f'http://quotes.toscrape.com{self.url}')
        hint_soup = BeautifulSoup(hint_response.text, 'html.parser')
        hint_born_date = hint_soup.find(class_="author-born-date").get_text()
        hint_born_location = hint_soup.find(class_="author-born-location").get_text()
        hint_description = hint_soup.find(class_="author-description").get_text()
        hint_split_name = self.author.split(' ')
        if guess_num == 1:
            # print(f"This author was born on {hint_born_date} in {hint_born_location}")
            return f"Here's a hint: This author was born on {hint_born_date} in {hint_born_location}\n"
        elif guess_num == 2:
            initials = []
            for name in hint_split_name:
                initials += name[0]
            if len(initials) <= 2:
                return f"Here's a hint: The author's initials are: {initials[0]} {initials[1]}\n"
            elif len(initials) > 2:
                return f"Here's a hint: The author's initials are: {initials[0]} {initials[1]} {initials[2]}\n"
        elif guess_num == 3:
            d = hint_description.replace(self.author, 'xxxxxxxxx')
            d2 = d.replace(hint_split_name[0], 'xxxxxx')
            d3 = d2.replace(hint_split_name[1], 'xxxxxx')
            description = d3[slice(1,500)]
            return f"Here's an exerpt from the authors bio.\n\nTheir name will be replaced with xxxxxx:\n\n{description}....\n\n"
# ************************************************************************************
# ================ END Classes =======================================================
# ====================================================================================



# ====================================================================================
# ================ Scrape script =====================================================
# ************************************************************************************
page_num = 1
data = []
while page_num <= 10:
    response = requests.get(f'http://quotes.toscrape.com/page/{page_num}/')
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.select('.quote')
    for quote in quotes:
        quote_author = quote.find(class_="author").get_text()
        quote_text = quote.find(class_="text").get_text()
        quote_url = quote.find('a')['href']
        # print(quote_author, quote_text, quote_url)
        # print('')
        quote_group = Quote(quote_author, quote_text, quote_url)
        data.append(quote_group)
    page_num += 1
# ************************************************************************************
# ================ END Scrape script =================================================
# ====================================================================================

# ====================================================================================
# ================ Game script =======================================================
# ************************************************************************************
guess_num = 1

while True:
    random_index = random.randint(0, len(data) - 1)
    random_quote = data[random_index]
    print(random_quote.author)
    while guess_num <= 4:
        # print(f"guess_num = {guess_num}")
        if guess_num == 0:
            print("Who said this shit??\n")
        # else:
        #     random_quote.hint(guess_num)
        guess = input(f'{random_quote.text}\n\nType your guess here: ')
        if guess.lower() == random_quote.author.lower():
            print('You did it!')
            break
        elif guess.lower() != random_quote.author.lower() and guess_num < 3:
            print("\nNope! Try again\n")
            print(random_quote.hint(guess_num))
            guess_num += 1
            # continue
        elif guess.lower() != random_quote.author.lower() and guess_num >= 3:
            if guess_num < 4:
                print("\nNope! One last guess!\n\n")
                print(random_quote.hint(guess_num))
                guess_num += 1
            else:
                print("Wanna play again?")
                play_again = input("Type: y or n\n")
                if play_again == 'y':
                    guess_num = 1
                else:
                    print('K bye')
                    exit()
# ************************************************************************************
# ================ END Game script ===================================================
# ====================================================================================

