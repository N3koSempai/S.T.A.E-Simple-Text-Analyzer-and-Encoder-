# -*- coding: utf-8 -*-

#@author: N3koSempai

from modules.frequency import allfrequency
from string import ascii_lowercase, ascii_uppercase, ascii_letters
import os


class Main():

    def __init__(self, file):
        self.file = file

    def openfile(self, file: str):
        with open(file, 'r') as f:
            #test the size of the file for prevent overbuffering
            size = os.stat(file).st_size
            # converting to a MBytes number
            size = size / 10000
            #set the maximun posible
            if size < 500:
                print(f)
                buffer = f.read()

                return buffer
            else:
                return None
    


    def analyze(self):
        buffer = self.openfile(self.file)
        print(buffer)
        count_space = allfrequency(buffer)
        print(count_space)


main = Main('LICENSE')

main.analyze()