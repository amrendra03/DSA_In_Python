# Python program to generate WordCloud

# importing all necessary modules
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

# Reads 'Youtube04-Eminem.csv' file
df = ['hello','amrendra','my','name']
df = pd.DataFrame(df)

comment_words = ''
stopwords = set(STOPWORDS)

# iterate through the csv file
s=''
for i in df[0]:
    s+=str(i)

comment_words=s
print(type(comment_words))
wordcloud = WordCloud(width=400, height=100,min_font_size=10,background_color='white').generate(comment_words)

# plot the WordCloud image
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

plt.show()
