class AnagramChecker:

    def __init__(self):
        with open('anagrams.txt', 'r') as f:
            self.load_file = f.read().split('\n')
        
    def is_valid_word(self, word):
        self.word = word
        for choice in self.load_file:
            if choice == word:
              return True
        return False

    def get_anagrams(self,word):
        self.word = word
        anagram_list = []
        for text in self.load_file:
            if sorted(word) == sorted(text):
                anagram_list.append(text)
        return anagram_list


#AnagramChecker()
# print(anag.is_valid_word('AA'))
# print(anag.get_anagrams('MEAT'))