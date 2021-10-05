from sklearn.datasets import fetch_20newsgroups
data = news.data*10
def clean_word(word):
    return re.sub(r'[^\w\s]','',word).lower()
def word_not_in_stopwords(word):
    return word not in ENGLISH_STOP_WORDS and word and word.isalpha()
    
    
def find_top_words(data):
    cnt = Counter()
    for text in data:
        tokens_in_text = text.split()
        tokens_in_text = map(clean_word, tokens_in_text)
        tokens_in_text = filter(word_not_in_stopwords, tokens_in_text)
        cnt.update(tokens_in_text)
        
    return cnt.most_common(10)

  
%time find_top_words(data)
 
  
def mapper(text):
    tokens_in_text = text.split()
    tokens_in_text = map(clean_word, tokens_in_text)
    tokens_in_text = filter(word_not_in_stopwords, tokens_in_text)
    return Counter(tokens_in_text)
def reducer(cnt1, cnt2):
    cnt1.update(cnt2)
    return cnt1
def chunk_mapper(chunk):
    mapped = map(mapper, chunk)
    reduced = reduce(reducer, mapped)
    return reduced
%%time
data_chunks = chunkify(data, number_of_chunks=36)
#step 1:
mapped = pool.map(chunk_mapper, data_chunks)
#step 2:
reduced = reduce(reducer, mapped)
print(reduced.most_common(10))
