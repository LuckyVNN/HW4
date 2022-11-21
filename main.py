import matplotlib.pyplot as plt

FILE1 = "bai_hat_1.txt"
FILE2 = "bai_hat_2.txt"

# DEFINE SOME FUNCTIONS

def load_words(n):
    """
    Read the lyrics file
    Return a list of words appeared in the lyrics in lowercased , remove dots and commas
    """
    inFile = open(n,'r',encoding='utf-8')
    read = (inFile.read())
    read = str.lower(read)
    read = read.replace("."," ")
    read = read.replace(","," ")
    word_list = read.split()
    return word_list


# print(load_words(FILE1))
# print(load_words(FILE2))


def lyrics_to_freq(lyrics):
    """
    Input the wordlist (list) <from the load_words>
    Return a Dict with : 
        keys = words in the lyric
        values = word frequency
    """
    Dict = {}
    for word in lyrics:
        if word in Dict:
            Dict[word] += 1
        else :
            Dict[word] = 1
    return Dict

# print(lyrics_to_freq(a))

def most_common_words (freq):
    """
    Input the lyric frequency ( Dict )
    Return the most common word(s) in the lyrics and it's number of appearances
    """
    values = freq.values()
    best = max(values)
    words = []
    for i in freq:
        if freq[i] == best :
            words.append(i)
    return(words,best)



def least_common_words (freq) :
    """
    Input the lyric frequency ( Dict )
    Return the least common word(s) in the lyrics and it's number of appearances
    """
    values = freq.values()
    worst = min(values)
    words = []
    for i in freq:
        if freq[i] == worst :
            words.append(i)
    return(words,worst)

# END OF DEFINING


#ASSIGN VARIABLE 
a = load_words(FILE1)   #list
b = load_words(FILE2)   #list

# SPLIT THE LYRIC -> WORDS
print("Song 1:",a)
print("--------------------------")
print("Song 2:",b)
print("--------------------------")

# FIND THE MOST COMMON WORD(S) IN EACH SONG

most1 = most_common_words(lyrics_to_freq(a))
print("Most common word(s) in song 1 is :",most1[0],"with",most1[1],"times")
print("--------------------------")
most2 = most_common_words(lyrics_to_freq(b))
print("Most common word(s) in song 2 is :",most2[0],"with",most2[1],"times")

print("--------------------------")
# FIND THE LEAST COMMON WORD(S) IN EACH SONG

least1 = least_common_words(lyrics_to_freq(a))
print("Least common word(s) in song 1 is :",least1[0],"with",least1[1],"times")
print("--------------------------")
least2 = least_common_words(lyrics_to_freq(b))
print("Least common word(s) in song 2 is :",least2[0],"with",least2[1],"times")


# CREATE BAR PLOT FOR EACH SONG ( WORDS FREQ IN EACH SONG )

# SORTING THE DICT(word:freq) BY DESCENDING VALUES
c=lyrics_to_freq(a)
d=lyrics_to_freq(b)
#   https://docs.python.org/3/howto/sorting.html
c = sorted(c.items(), key=lambda x:x[1], reverse=True)
d = sorted(d.items(), key=lambda x:x[1], reverse=True)

c=dict(c)
d=dict(d)

# DRAW GRAPH 1
names = list(c.keys())
values = list(c.values())


plt.bar(range(len(c)), values, tick_label=names)
plt.xticks(rotation = 90)
plt.title("Frequency of words in Song 1", size=15)
plt.ylabel("Frequency", size=15)
plt.show()

# DRAW GRAPH 2
names2 = list(d.keys())
values2 = list(d.values())


plt.bar(range(len(d)), values2, tick_label=names2)
plt.xticks(rotation = 90)
plt.title("Frequency of words in Song 2", size=15)
plt.ylabel("Frequency", size=15)
plt.show()