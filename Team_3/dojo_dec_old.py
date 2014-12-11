f_in = open('corpus.txt', 'r')
rows_in = f_in.readlines()
f_in.close()

all_words = list()
word_couplings = dict()

for row in rows_in:
    sentence = row.split(' ')
    #print sentence
    for word in sentence:
        word = word.lower()
        all_words.append(word)
        #print word
        word_couplings[word] = list()

for word in word_couplings.keys():
    for row in rows_in:
        sentence = row.split(' ')
        for i in range(0, len(sentence)-1):
            if sentence[i].lower() == word:
                word_couplings[word].append(sentence[i+1].lower())

print 'The length of the file is ', len(rows_in), 'senteces'
print 'The total num of words is ', len(all_words)

#print word_couplings['the']

word_couplings_max = dict()
for word in word_couplings.keys():
    word_couplings_max[word] = list()

for word in word_couplings.keys():
    #print 'word ', word
    couplings_occurrences = dict()
    for coupled_word in word_couplings[word]:
        couplings_occurrences[coupled_word] = word_couplings[word].count(coupled_word)
    #print couplings_occurrences
    if couplings_occurrences != {}:
        max_occurrence = max(couplings_occurrences.values())
        for key in couplings_occurrences.keys():
            if couplings_occurrences[key] == max_occurrence:
                word_couplings_max[word].append(key)

#print word_couplings_max['he']

while True:
    your_word = raw_input('Please feed me with a word: ')
    your_word = your_word.lower()

    if your_word in word_couplings_max.keys():
        print 'Suggested couples:'
        for coupled_word in word_couplings_max[your_word]:
            print your_word, coupled_word
        break
    else:
        print 'Sorry, your word is not in my corpus!'

