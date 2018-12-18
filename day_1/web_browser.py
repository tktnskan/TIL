import webbrowser

keywords = [
    'python',
    'drama',
    'game of throne',
    'imperial college london'
]

for keyword in keywords:
    url = 'https://google.com/search?q=' + keyword
    webbrowser.open_new(url)

