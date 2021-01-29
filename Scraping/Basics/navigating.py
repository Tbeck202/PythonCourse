from bs4 import BeautifulSoup

html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div id="first">
        <h3 data-example="yes">hi</h3>
        <p>more text.</p>
    </div>
    <ol>
        <li class="special super-special">This list item is special</li>
        <li class="special">This list item is also special</li>
        <li>This list item is not special</li>
    </ol>
    <div>bye</div>
</body>
</html>
'''

soup = BeautifulSoup(html, "html.parser")

data = soup.body.contents
data2 = soup.body.contents[1].next_sibling.next_sibling
data3 = soup.find(class_="super-special").find_next_sibling()
data4 = soup.find(id="first").find_next_sibling()
data5 = soup.select("[data-example]")

# for d in data:
#     print(d)
# print(data2)
# print(data3)
# print(data4)
print(data5)