import wikipedia
import re, time
from typing import List


def tokenize(text: str) -> List[str]:
        """Splits given text into a list of the individual tokens in order

        Args:
            text - text to tokenize

        Returns:
            tokens of given text in order
        """
        tokens = []
        token = ""
        for c in text:
            if (
                re.match("[a-zA-Z0-9]", str(c)) != None
                or c == "'"
                or c == "_"
                or c == "-"
            ):
                token += c
            else:
                if token != "":
                    tokens.append(token.lower())
                    token = ""
                # if c.strip() != "":
                #     tokens.append(str(c.strip()))

        if token != "":
            tokens.append(token.lower())
        return tokens


article = wikipedia.page("Artemis II", auto_suggest=False).content
#print(article)
words = tokenize(article)
#print(words)

with open("sorted_stoplist.txt", "r", encoding="utf8") as f:
     stoplist = f.read()
tokenized_stoplist = tokenize(stoplist)


# with open("sorted_stoplist.txt", "r", encoding='utf8') as f:
#      stoplist = f.read()

freqs = {}

for word in words:
    if word not in tokenized_stoplist: 
        if word is freqs:
            freqs[word] += 1
        else:
            freqs[word] = 1

#print(freqs)

#Print total unique words and total number of words
unique_words = len(freqs)
print(f"Unique words: {unique_words}")

total_num_words = sum(freqs.values())
print(f"Total words: {total_num_words}")

#Print top 20 words
# top_words = sorted(freqs.items(), key=lambda x: x[1], reverse = True)
# print("Top 20 words: ")
# for word, count in top_words[:20]:
#     print(f"{word} {count}")
