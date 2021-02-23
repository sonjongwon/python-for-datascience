f = open("yesterday.txt", "r")
yesterday_lyrics = ""

while True:
    line = f.readline()
    if not line:
        break
    yesterday_lyrics = yesterday_lyrics + line.strip() + "\n"
f.close()

n_title_of_Yesterday = yesterday_lyrics.count("Yesterday")
n_lower_of_yesterday = yesterday_lyrics.count("yesterday")

print("Number of a word 'YESTERDAY':", n_title_of_Yesterday)
print("Number of a word 'yesterday':", n_lower_of_yesterday)
