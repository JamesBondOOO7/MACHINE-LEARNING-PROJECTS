#   SET UP A NLP PIPELINE
#1. Load input file and read review
#2. Tokenize
#3. Stopwords Removal
#4. Stemming


# NLTK OBJECTS
# Tokenizer
from nltk.tokenize import RegexpTokenizer
# Stopwords
from nltk.corpus import stopwords
# Stemmer
from nltk.stem.porter import PorterStemmer

# Initializing the objects
tokenizer = RegexpTokenizer(r'\w+')
eng_stopwords = set(stopwords.words('english'))
ps = PorterStemmer()

# total filtering of a review
def stemmed_review(review):
    # Step 1 : uniformity + removing <br> tags
    review = review.lower()
    review = review.replace("<br /><br />"," ")
    
    # Step 2 : tokenize
    tok_review = tokenizer.tokenize(review)
    
    # Step 3 : Stopword removal
    swr_review = [word for word in tok_review if word not in eng_stopwords]
    
    # Step 4 : Stemming
    stem_review = [ps.stem(word) for word in swr_review]
    
    # Step 5 : Retuening Cleaned review (Unordered)
    cleaned_review = ' '.join(stem_review)
    
    return cleaned_review

# filtering the whole document
# Given an input file of reviews : Filter all the reviews and save it in an output file

def getStemmedDoc(inputfile,outputfile):
    
    out_file = open(outputfile,'w',encoding='utf8')
    
    with open(inputfile,encoding='utf8') as f:
        reviews = f.readlines()
        
    for review in reviews:
        cleaned_review = stemmed_review(review)
        
        print((cleaned_review),file=out_file)
        
    out_file.close()
    
    
# This file will run on CMD, therefore while working with Cmd line arguments import sys module
import sys

# Input and Output files will be provided on CMD

input_file = sys.argv[1]
output_file = sys.argv[2]

getStemmedDoc(input_file,output_file)
    
    
