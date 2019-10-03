import os
from gtts import gTTS
from wordcloud import WordCloud
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
# article_list = arxivParser.parseRss()
save_directory='public_files'

# def createAudioFiles(articlesList=article_list, directoryPath=save_directory):
def createAudioFiles(articlesList, directoryPath=save_directory):
# def createAudioFiles(directoryPath=exampleDirectory):
    for article in articlesList:
        mp3Filename = article['articleID']+'.mp3'
        if mp3Filename not in os.listdir(directoryPath):
            tts=gTTS(text=' '.join([article['title'],'. By',article['authors'],'Abstract.',article['abstract']]))
            tts.save(os.path.join(directoryPath,mp3Filename))

def createWordCloudImages(articlesList, directoryPath=save_directory):
    for article in articlesList:
        text=article['abstract']
        wordcloud = WordCloud().generate(text)
        fileName=article['articleID']+'.png';
        # path=os.path.join(currentDirectory, directoryPath,fileName);
        path=os.path.join(directoryPath,fileName);
        fig, ax = plt.subplots()
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("equal")
        ax.axis('off')
        plt.savefig(path, bbox_inches='tight')
# createAudioFiles()
# createWordCloudImages()
