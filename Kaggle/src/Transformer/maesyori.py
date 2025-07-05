import nltk
nltk.download("punkt")
nltk.download('averaged_perceptron_tagger_eng')
from nltk.tokenize import word_tokenize
from nltk import pos_tag

  
text = """In recent years, natural language processing has become an essential field in artificial intelligence. 
With the rise of powerful language models such as GPT and BERT, machines are now capable of understanding, 
generating, and even translating human language with remarkable accuracy. 
This rapid development has opened up new possibilities in areas such as customer service automation, 
real-time translation, and intelligent personal assistants."""
tokens = word_tokenize(text)
posTag = pos_tag(tokens)
print(tokens)
print(posTag)
