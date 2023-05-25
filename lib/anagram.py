class Anagram:
    def __init__(self, word):
        self.letters = sorted([letter for letter in word])
    
    def match(self, words):
        word_list = []
        for word in words:
            if sorted([letter for letter in word]) == self.letters:
                word_list.append(word)
        return word_list