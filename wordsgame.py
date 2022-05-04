class BasicWord:
    def __init__(self, basic_word, subwords):
        self.basic_word = basic_word
        self.subwords = subwords

    def is_right(self, answer):
        return answer in self.subwords

    def subwords_count(self):
        return len(self.subwords)


class Player:
    def __init__(self, name):
        self.name = name
        self.used_words = []

    def add_word(self, word):
        self.used_words.append(word)

    def is_used(self, word):
        return word in self.used_words

    def used_words_count(self):
        return len(self.used_words)
