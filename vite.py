#!/bin/python3

from pytube import YouTube
import sys
if len(sys.argv)==2:
	try:
		url = sys.argv[1]
#		print(f'url : {url}')
#		print(sys.argv)
		video = YouTube(url)
		stream = video.streams.get_highest_resolution()
		print('Downloading...')
		stream.download()
	except KeyboardInterrupt:
		print('KeyboardInterrupt, exiting..')
	except:
		print(f'''********************
The link is broken.
url: {url}
*****************---''')
else:
	print('USAGE: python3 download01.py "url"')
	print('''Example:
 python3 downloader01.py https://youtu.be/C5nN7QDJ6-g

''')
