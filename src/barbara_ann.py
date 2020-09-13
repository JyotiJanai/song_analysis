from matplotlib import pyplot as plt

lyrics = "Ah, Ba Ba Ba Ba Barbara Ann Ba Ba Ba Ba Barbara Ann Oh Barbara Ann Take My Hand Barbara Ann You Got Me Rockin' And A-Rollin' Rockin' And A-Reelin' Barbara Ann Ba Ba Ba Barbara Ann ...More Lyrics... Ba Ba Ba Ba Barbara Ann Ba Ba Ba Ba Barbara Ann"
list_of_lyrics = lyrics.split(' ')
print(len(list_of_lyrics))
unique_words = set(list_of_lyrics)
print(len(unique_words))
word_histogram = dict.fromkeys(unique_words, 0)
for word in list_of_lyrics:
    word_histogram[word] = word_histogram[word]+ 1 
print(word_histogram)

print(list(unique_words))
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(list(unique_words),list(word_histogram.values()))
plt.bar(list(unique_words), list(word_histogram.values()), color ='maroon',  
        width = 0.4)
plt.xlabel("Unique song words")
plt.ylabel("No. of words")
plt.title("Barbara ann song repeated words graph")
plt.show()