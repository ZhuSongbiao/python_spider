# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:33:47 2019
modified from
https://blog.csdn.net/u012735708/article/details/81532407
"""
# English wordcloud
from wordcloud import WordCloud
 
# Read the whole text.
text = open('constitution.txt').read()
 
# Generate a word cloud image
wordcloud = WordCloud().generate(text)
 
# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud)
plt.axis("off")
 
# lower max_font_size
wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

