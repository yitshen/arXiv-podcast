import feedparser
import re
# import re
# from bs4 import BeautifulSoup

def parseRss(url='https://arxiv.org/rss/physics.optics'):
  d = feedparser.parse(url)
  d = d['entries'][:1]
  ans = []
  for article in d:
      temp = {}
      temp['abstract'] = str(article['summary'][3:][:-5]).replace('\n',' ')
      temp['articleID'] = str(article['id'][-10:])
      temp['url'] = article['id']
      temp['authors']=', '.join(re.findall(">([^<]+)</a>",str(article['authors'])))
      temp['title'] = article['title'].split(' (arXiv:')[0].title()
      ans.append(temp)
  return ans
