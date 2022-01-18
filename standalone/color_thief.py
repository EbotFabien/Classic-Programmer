from colorthief import ColorThief
import requests as req
#requests.get('https://www.channelstv.com/wp-content/uploads/2020/05/Chinese_President_Xi.jpg')
url='https://www.channelstv.com/wp-content/uploads/2020/05/Chinese_President_Xi.jpg'
local_filename = url.split('/')[-1]

r = req.get(url, stream=True)

with open(local_filename, 'wb') as f:

    for chunk in r.iter_content(chunk_size=1024):

        f.write(chunk)
        
        
color_thief = ColorThief(local_filename)
# get the dominant color
dominant_color = color_thief.get_color(quality=1)
# build a color palette
palette = color_thief.get_palette(color_count=6)

print(dominant_color)
