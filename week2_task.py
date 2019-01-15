import numpy as np
import nltk
from collections import Counter
from scipy import spatial
np.set_printoptions(linewidth=256,threshold=10000)
def dictr(counts):
    dict = {}
    i = 0
    for sublist in counts:
        for word in sublist:
            if word not in dict:
                dict.update({word:i})
                i+=1
    return dict

def fill_shumatrix(shumlist, dict, dicts):
    shumatrix = np.zeros((22, 254))
    i = 0
    for line in shumlist:
        for word in line:
            shumatrix[i,dict.get(word)] = dicts[i].get(word)
        i += 1
    return shumatrix

with open('catsentances.txt') as f:
    shumlist = []
    dicts = []
    for line in f:
        counts = nltk.word_tokenize(line.lower())
        counts = [word for word in counts if word.isalpha()]
        shumlist.append(counts)
        appears = dict(Counter(counts))
        dicts.append(appears)
    shumatrix = fill_shumatrix(shumlist,dictr(shumlist),dicts)
    result = [spatial.distance.cosine(shumatrix[0],sent) for sent in shumatrix[1:]]
    print(sorted(result)[:2])
    for i in range(len(result)):
        if result[i] in sorted(result)[:2]:
            print(i)





