'''
Class to read audio chunks from database
Author : Vasanthakumar N
Date   : 10 Mar 2018

Todo
Error handling, unit testing, verify return status
'''

from pymongo import MongoClient
import scipy.io.wavfile as wav
import numpy as nd
from bson.binary import Binary
import pickle

class ReadAudio:
    def __init__(self,db,collection,querylist):     #Constructor to initialize info requied for write operation
        self.con = MongoClient('localhost',27017)
        self.db = eval ('self.con.' + db)
        self.collection = collection
        self.querylist = querylist


    def read_data(self,audio):
        if self.querylist[0] == 0:                 # For individual queries
            query = 'self.db' + '.' + self.collection + '.' + self.querylist[1]
            return eval(query)
        # if self.querylist[0] == 1:               # For multiple queries to be executed by a single object


if __name__ == '__main__':
    obj = ReadAudio()
