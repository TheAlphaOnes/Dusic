import scrapetube


def search_youtube(topic):
    reply = scrapetube.get_search(topic + " song")
    temp = []
    h = 0
    for info in reply:
        h = h+1
        temp.append(info)
        if h > 11:
            break
    infos = temp[:10]
    data = []
    for info in infos:
        title = info['title']['runs'][0]['text']
        title = str(title).split(" ")
        if len(title) > 11:
            title = title[:11]
        title = " ".join(title)
        author = info['longBylineText']['runs'][0]['text']
        id = info['videoId']
        thumb = info['thumbnail']['thumbnails'][0]['url']
        req = f"s={id}&a={author}"
        dat = {'id': id, 'title': title, 'author': author, 'thumb': thumb,
               "chlink": f"https://www.youtube.com/results?search_query={author}","req":req }
        data.append(dat)
    return data
