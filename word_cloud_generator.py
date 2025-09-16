from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = input("enter ur text here: ")


wordcloud = WordCloud(
    width=800,
    height=400,
    background_color='black',
    colormap='rainbow',
    min_font_size=10
).generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')  
plt.axis("off")
plt.show()

