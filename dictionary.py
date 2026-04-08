import wikipedia
import re 
from typing import List


def tokenize(self, text: str) -> List[str]:
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
                if c.strip() != "":
                    tokens.append(str(c.strip()))

        if token != "":
            tokens.append(token.lower())
        return tokens

article = wikipedia.page("Artemis II", auto_suggest=False).content
tokens = article.tokenize
print(article)

freqs = []

for word in tokens:
     if word is freqs:
          freqs[word] += 1
     else:
          freqs[word] = 1

print(freqs)