def ExtractLinks(soup):
    LinkList = []
    for link in soup.find_all('a'):
        LinkString = str(link.get('href'))

        if LinkString[:6]=='/wiki/':
            if LinkString[:11]!='/wiki/File:':
                if LinkString[:16]!='/wiki/Wikipedia:':
                    if LinkString[:14]!='/wiki/Special:':
                        if LinkString[:11]!='/wiki/Help:':
                            if LinkString[:15]!='/wiki/Category:':
                                if LinkString[:13]!='/wiki/Portal:':
                                    LinkList.append(link.get('href'))
    return LinkList
