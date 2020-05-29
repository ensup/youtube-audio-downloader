import os
url = input('Type URL: ')
print(url)
os.system("youtube-dl -f 140 "+url)