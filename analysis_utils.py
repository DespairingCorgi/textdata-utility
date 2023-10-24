import re

class tokenizer():
    def __init__(self, tokenizer):
        pass
    def tokenize(text):
        pass
    def getwords(text):
        pass


def charactercount(text, include_space=False):
    return len(text.replace(' ')) if include_space else len(text)

def tokencount(text, use_space=True, **kwargs):
    if use_space:
        text_tokenized=text.spilt()
    else:
        try:
            text_tokenized=kwargs["tokenizer"].tokenize(text)
        except:
            raise Exception("proper kwargs 'model' required")
        
    return len(text_tokenized)
        
def wordcount(text, use_space=True, **kwargs):
    if use_space:
        text_tokenized=text.split()
    else:
        try:
            text_tokenized=kwargs["tokenizer"].getwords(text)
        except:
            raise Exception("proper kwargs 'model' required")
    
    return len(text_tokenized)

def