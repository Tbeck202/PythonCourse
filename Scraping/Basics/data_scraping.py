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

d = soup.select('.special') #[<li class="special super-special">This list item is special</li>, <li class="special">This list item is also special</li>]
el= soup.select('.special')[0] #<li class="special super-special">This list item is special</li>
h = soup.find('div')['id'] #first

print(d)
print(el)
print(h)
# for e in d:
#     print(e.name)
#     print(e.attrs['class'])
#     print(e.get_text())
# print(el.get_text())