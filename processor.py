import math
import json
from inverted import word_processor


def query_processor(data,query,index):
    """ 
    this function retrieves the relevant document matching the user query in a ranked order 
    (i.e it uses the tf-idf score of the query as the reference for ranking when doing the retrieval)
    """
    doc_len = len(data)
    processed_query = word_processor(query)
    retrieved_id = [] #stores a ranked list of documents that matches query in descending order 
    score_list = []   # a list of all (docID , tf_idf_score)
    score_dict = {}  # a dictionary containing  (docID , [tf_idf_score])
    for word in processed_query:       
        if word in index.keys():
            for i in range(0, len(index[word])):
                tf = math.log10(1 + index[word][i][1])
                idf = math.log10(1 + doc_len/(len(index[word])))
                tf_idf = round((tf*idf), 2)           
                score_list.append([index[word][i][0], tf_idf])

    for score in score_list:
        if score[0] in score_dict:
            score_dict[score[0]].append(score[1])
        else:
            score_dict[score[0]] = []
            score_dict[score[0]].append(score[1])               
        # taking the sum of all the scores in the list of the score_dict values
    weighted_score = {key: round(sum(score_dict[key]),2) for key in score_dict}
    sort_dict = dict(sorted(weighted_score.items(), key=lambda item: item[1], reverse=True)) # sorts the score_dict in descending order
    for key,value in sort_dict.items():
        retrieved_id.append(key)  
    
    return retrieved_id