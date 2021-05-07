class Text:
    def __init__(self, text):
        self.text = text

    @classmethod
    def data_from_file():
        with open('the_stranger.txt', 'r') as f:
            data = f.read()
        return cls(data)
    
   

    def frequency_of_word(self, word):
        
        count = 0
        text_block = (self.text.split())
        for i in text_block:
            if i == word:
                count += 1
            
        if count > 0:
            print(f'"{word}" appears {count} times in this text block')
        else:
            print(f'the word {word} is not present')
    

    def most_common_word(self):
        
        text_block = (self.text.split())
        word_dict = dict((i, text_block.count(i)) for i in text_block)
        v = list(word_dict.values())
        k = list(word_dict.keys())
        max_occurence = (k[v.index(max(v))])
        print(f'The most common word here is " {max_occurence} "')

    def unique_words(self):
        text_block = (self.text.split())
        word_dict = dict((i, text_block.count(i)) for i in text_block)
        # v = list(word_dict.values())
        # k = list(word_dict.keys())
        for key in word_dict:
            if word_dict[key] == 1:
                print(f'{key} is a unique word')


sentence = Text("hello it it it it this this is world whaaaat")
print(sentence.text)
sentence.frequency_of_word('this')
sentence.most_common_word()
sentence.unique_words()

print(sentence.text.split())

class TextModification(Text):
    def __init__(self, text):
        super().__init__('text')

    def no_punctuation(self):
        text_block = (self.text.split())
        output = ' '.join(text_block)
        print(output)

    def no_stopwords():
        with open('99webtools.txt', 'r') as f:
            stop_words = f.read()
            print(stop_words)
        
        for line in stop_words:
            stripped_line = stop_words.strip()
            stopword_list = stripped_line.split()
        print(stopword_list)

        # if any(word in text_block for word in stopword_list):
        #     text_block.remove(word)
        # print(text_block)
        
    no_stopwords()







        


        
