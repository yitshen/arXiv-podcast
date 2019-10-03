from arxivParser import parseRss
from textToAudioVisual import createAudioFiles, createWordCloudImages
from arxivFeedgen import generateRss
url = 'https://script.google.com/macros/s/AKfycbzwHEGtkooffMLdmarcwIQDIQs-m2Zrsf2IGqIT5qjaAS-NCSk5/exec?url=https://arxiv.org/rss/physics.optics'
# you can take care of the rest...
articlesList=parseRss(url = url)
# print(articlesList[0]['articleID'])
# generateRss(articlesList)

createAudioFiles(articlesList)
createWordCloudImages(articlesList)
generateRss(articlesList)
