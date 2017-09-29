import collections
import math

from nltk import regexp_tokenize
from nltk.corpus import stopwords, words, movie_reviews
from nltk.stem import WordNetLemmatizer

stops = stopwords.words('english')
lemmatizer = WordNetLemmatizer()
vocabs = set(w.lower() for w in words.words())

categories = ['pos', 'neg']

for cate in categories:
    docs = movie_reviews.fileids(categories=cate)
    n = len(docs)  # n = number of documents

    trim_dict = {}
    for doc in docs:
        token = regexp_tokenize(movie_reviews.raw(fileids=doc), r'[a-zA-Z]+')
        no_stop = list(filter(lambda x: x not in stops, token))
        lemm = list(map(lambda x: lemmatizer.lemmatize(x), no_stop))
        trim = []
        for w in lemm:
            if w in vocabs and len(w) > 1:
                trim.append(w)
        trim_dict[doc] = trim

    indi_count = []
    for doc in docs:
        indi_count.append(collections.Counter(trim_dict[doc]))

    total_count = collections.Counter()
    for count in indi_count:
        total_count += count

    word_list = sorted(total_count.keys())

    ndt_dict = {}
    for word in word_list:
        word_count = []
        for count in indi_count:
            word_count.append(count[word])
        ndt_dict[word] = word_count

    nd_list = []
    for count in indi_count:
        nd_list.append(sum(count.values()))

    nt_dict = {}
    for word in word_list:
        doc_count = []
        detected = 0
        for count in indi_count:
            if count[word] > 0:
                detected += 1
            nt_dict[word] = detected

    ti_dict = {}
    for word in word_list:
        ti = 0
        for idx in range(len(indi_count)):
            ndt = ndt_dict[word][idx]
            nd = nd_list[idx]
            nt = nt_dict[word]
            ti += (math.log(1 + ndt / nd) * math.log(n / nt))
        ti_dict[word] = ti

    top = collections.Counter(ti_dict).most_common(15)
    print('\n---------- {} reviews ----------'.format(cate))
    for i in top:
        print(' {word:<13}{ti:>15}'.format(word=i[0], ti=i[1]))
