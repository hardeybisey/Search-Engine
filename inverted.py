import json
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
# nltk.download('stopwords')
# nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize
import string
ps = PorterStemmer()
sw = stopwords.words('english')


def word_processor(tokens):
    """ function to clean the documents in the database (files stored by the crawler)
    """
    stem_sentence = []
    text = str(tokens).lower() # converts all words to lower case  
    text = text.translate(str.maketrans('','', string.punctuation)) # removes punctuations
    token_words= word_tokenize(text) #tokennize each word
    for word in token_words:
        if word not in sw:   
            word = ps.stem(word)
            stem_sentence.append(word)          
            
    return stem_sentence


def inverted_index(data):
    """ 
    this function builds the inverted index for each documents present in the data base
    """
    inv_index = {} # stores inverted 
    for document in data:
        for key,value in document.items():
            if 'http' in value: #ignoring urls
                continue
            if type(value) is list: #profile links were saved in a list so we ignorne them 
                continue
            doc_token = word_processor(value)  #applying preprocessing on all words in the data base
            doc_index = data.index(document) #creating the index for each token
            for word in doc_token:
                if word in inv_index:
                    inv_index[word].append(doc_index)
                else:
                    inv_index[word] = [doc_index]
    # grouping the DocID of each document by the number of times they occur
    for word in inv_index:
        w = (inv_index[word])
        inv_index[word] = [(i, w.count(i)) for i in set(w)] 
    with open("data/inv_index.json", "w") as jsonfile:
        json.dump(inv_index, jsonfile)