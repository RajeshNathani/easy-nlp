import spacy
from spacy import displacy
nlp = spacy.load("en_core_web_sm")

class extract:
    def POS(str):
        parts = nlp(str)
        sent = dict()
        for token in parts:
            sent[token.text] = token.pos_
        return(sent)
    def base(str):
        parts = nlp(str)
        bas = dict()
        for token in parts:
            bas[token.text] = token.lemma_
        return(bas)
    def token(str):
        doc = nlp(str)
        return [token.text for token in doc]

    def names(str):
        doc = nlp(str)
        return [(ent.text , ent.label_) for ent in doc.ents]

class display:
    def show(str):
        doc = nlp(str)
        return displacy.serve(doc , style='ent')

class sentence:
    def split(str):
        text = nlp(str)
        sentences =[]
        for sent in text.sents:
            sentences.append(sent)
        return sentences
 
