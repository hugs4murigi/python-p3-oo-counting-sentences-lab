#!/usr/bin/env python3
import re
class MyString:
    def __init__(self, value=""):
        self.value = value
    
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, words):
        if isinstance(words, str):
            self.__value = words
        else:
            print("The value must be a string.")

    def is_sentence(self):
        dot = "."
        if self.__value.endswith(dot):
            return True
        else:
            return False
    def is_question(self):
        question_mark = "?"
        if self.__value.endswith(question_mark):
            return True
        else:
            return False
    def is_exclamation(self):
        exclamation_mark = "!"

        if self.__value.endswith(exclamation_mark):
            return True
        else:
            return False

    def count_sentences(self):
        sentences = re.split(r'[!?.]+', self.__value)

        sentences = [s for s in sentences if s]

        return len(sentences)
