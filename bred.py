
def make_bigrams(list_of_words_and_sentences):
    bigrams = {}
    for sent in list_of_words_and_sentences:
        for word in range(len(sent) - 1):
            next_word = word + 1
            if sent[word].lower() in bigrams.keys():
                if sent[next_word].lower() in bigrams[sent[word].lower()]:
                    bigrams[sent[word].lower()][sent[next_word].lower()] += 1
                else:
                    bigrams[sent[word].lower()][sent[next_word].lower()] = 1
            else:
                new_dict = {sent[next_word].lower(): 1}
                bigrams[sent[word].lower()] = new_dict
    return bigrams
