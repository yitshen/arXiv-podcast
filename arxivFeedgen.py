import os
from feedgen.feed import FeedGenerator


def generateRss(articlesList,publicFilesPath= 'public_files',baseUrl='https://yitshen.pythonanywhere.com/'):
    fg = FeedGenerator()
    fg.load_extension('podcast')
    fg.podcast.itunes_category('Science')
    fg.title('Arxiv Optics Podcast')
    fg.author( {'name':'Scott Shen','email':'t.scott.shen@gmail.com'} )
    fg.podcast.itunes_owner(name='Scott Shen',email='t.scott.shen@gmail.com' )
    fg.link( href=baseUrl+'rss', rel='self' )
    fg.language('en')
    fg.subtitle('test')
    fg.podcast.itunes_explicit('no')

    for article in articlesList:
        fe = fg.add_entry()
        mp3Filename=article['articleID']+'.mp3'
        pngFilename=article['articleID']+'.png'
        fe.podcast.itunes_image(baseUrl+'png?filename='+pngFilename)
        fe.podcast.itunes_explicit('no')
        #fe.podcast.itunes_duration(int(pydub.AudioSegment.from_mp3(os.path.join(publicFilesPath,mp3Filename)).duration_seconds))
        fe.id(baseUrl+'mp3?filename='+mp3Filename)
        fe.title(article['title'])
        fe.link(href=article['articleID'])
        fe.description(article['abstract'])
        fe.enclosure(baseUrl+'mp3?filename='+mp3Filename,0, 'audio/mpeg')

    fg.logo(baseUrl+'png?filename='+pngFilename)
    fg.rss_file(os.path.join(publicFilesPath,'podcast.xml'))

    print('Generated RSS Feed')
# generateRss()
