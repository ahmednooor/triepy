class Trie:

    @staticmethod
    def _struct():
        struct = {'_iW': False}
        return struct

    def _make(self, words_list):
        list_len = len(words_list)
        tmp_s = self._trie
        self._trie = tmp_s

        for i in range(list_len):
            for char in words_list[i]:
                if char not in tmp_s:
                    tmp_s[char] = self._struct()
                tmp_s = tmp_s[char]

            tmp_s['_iW'] = True
            tmp_s = self._trie

        self._trie['_iW'] = False

    def __init__(self, words_list=None):
        if words_list is None:
            words_list = ['']

        self._trie = self._struct()
        self._make(words_list)

    def add(self, words_list):
        self._make(words_list)

    def find(self, word):
        tmp_s = self._trie
        found_word = False

        for char in word:
            if char in tmp_s:
                tmp_s = tmp_s[char]
                if tmp_s['_iW'] == True:
                    found_word = True
                else:
                    found_word = False
            else:
                found_word = False
                break

        return found_word

    def remove(self, words_list):

        def remover(word, iW_switch):
            tmp_s = self._trie
            self._trie = tmp_s

            for char in word:
                if char in tmp_s:
                    if (
                            char == word[-1] and
                            len(tmp_s[char]) == 1 and
                            tmp_s[char]['_iW'] == iW_switch
                    ):
                        iW_switch = False
                        del tmp_s[char]
                        word = list(word)
                        word.pop()
                        word = ''.join(word)
                        remover(word, iW_switch)
                    elif (
                            char == word[-1] and
                            tmp_s[char]['_iW'] == iW_switch and
                            iW_switch == True
                    ):
                        iW_switch = False
                        tmp_s[char]['_iW'] = False
                        tmp_s = tmp_s[char]
                    else:
                        tmp_s = tmp_s[char]
                else:
                    break

        for word in words_list:
            remover(word, True)

    def trie(self):
        return self._trie
