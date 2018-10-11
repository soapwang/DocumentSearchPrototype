import pickle
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import TreebankWordTokenizer
import glob
import os
import codecs

path = ".\\documents"

invert_index = dict()
def build(path):
    for filename in glob.glob(os.path.join(path, '*.txt')):
        with codecs.open(filename, 'r', 'utf-8') as f:
            for line in f:
                s = line.lower().strip('\n')
                # tokenizer = RegexpTokenizer('[a-z]\w+')
                tokenizer = TreebankWordTokenizer()
                tokens = tokenizer.tokenize(s)
                for t in tokens:
                    if t in invert_index:
                        files = invert_index[t]
                        # Update the word count by 1
                        if filename in files:
                            files[filename] += 1
                        # A new file contains this word
                        else:
                            invert_index[t][filename] = 1
                    else:
                        invert_index[t] = {filename: 1}

    pickle.dump(invert_index, open("invert_index.p", "wb"))
    #print(invert_index)


if __name__ == "__main__":
    build(path)