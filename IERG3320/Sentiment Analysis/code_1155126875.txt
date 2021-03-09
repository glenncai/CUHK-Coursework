# Cai Long Hua
# 1155126875

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer 
import nltk.stem as ns


# collect the stop word from NLTK
stopwords = set(stopwords.words('english'))


# method for read text
def readTxt(filename):
  with open(filename, 'r', encoding='utf-8') as f:
    text = f.read()
    return text


# count the total number words of my comments
def countNumber_comments(filename):
  text = readTxt(filename)
  totalNumber_word = len(text.split())
  return totalNumber_word


# participle and delete stop words
def deleteStopWords(text):
  comments = readTxt(text)
  splitWords = word_tokenize(comments)
  newCommentBox = []
  
  for word in splitWords:
    if word not in stopwords:
      newCommentBox.append(word)
  print("Finsih deleting stop word...\n")
  return newCommentBox


# reduction for the adjectives
def comment_TypeReduction(text):
  comments = deleteStopWords(text)
  lemmatizer = ns.WordNetLemmatizer()
  CommentBox_AfterReduction = []
  for word in comments:
    noun_word = lemmatizer.lemmatize(word, pos='a')
    CommentBox_AfterReduction.append(noun_word)
  print("Finish reduction...\n")
  return CommentBox_AfterReduction


# delete unnecessary characters
def delete_Characters(text):
  comments = comment_TypeReduction(text)
  characterList1 = str.maketrans("","",".,")
  characterList2 = str.maketrans("","","δΔ")
  characterList3 = str.maketrans("","","><")
  characterList4 = str.maketrans("","","?!")
  characterList5 = str.maketrans("","",")(")
  characterList6 = str.maketrans("","","=-")
  characterList7 = str.maketrans("","","}{")
  characterList8 = str.maketrans("","","△/")
  characterList9 = str.maketrans("","","12")
  characterList10 = str.maketrans("","","34")
  characterList11 = str.maketrans("","","56")
  characterList12 = str.maketrans("","","78")
  characterList13 = str.maketrans("","","910")
  characterList14 = str.maketrans("","","0Q")
  characterList15 = str.maketrans("","","XY")
  characterList16 = str.maketrans("","","HI")
  characterList17 = str.maketrans("","","AB")
  characterList18 = str.maketrans("","","–&")
  characterList19 = str.maketrans("","","ut")
  comments = [s.translate(characterList1) for s in comments]
  comments = [s.translate(characterList2) for s in comments]
  comments = [s.translate(characterList3) for s in comments]
  comments = [s.translate(characterList4) for s in comments]
  comments = [s.translate(characterList5) for s in comments]
  comments = [s.translate(characterList6) for s in comments]
  comments = [s.translate(characterList7) for s in comments]
  comments = [s.translate(characterList8) for s in comments]
  comments = [s.translate(characterList9) for s in comments]
  comments = [s.translate(characterList10) for s in comments]
  comments = [s.translate(characterList11) for s in comments]
  comments = [s.translate(characterList12) for s in comments]
  comments = [s.translate(characterList13) for s in comments]
  comments = [s.translate(characterList14) for s in comments]
  comments = [s.translate(characterList15) for s in comments]
  comments = [s.translate(characterList16) for s in comments]
  comments = [s.translate(characterList17) for s in comments]
  comments = [s.translate(characterList18) for s in comments]
  comments = [s.translate(characterList19) for s in comments]
  
  # remove all the spaces
  for i in comments:
    if '' in comments:
      comments.remove('')
      
  print("Finish deleting unwanted characters...\n")
  return comments
  
  
# tag for ajective and verb
def tagclassification_comments(text):
  comments = delete_Characters(text)
  postags = pos_tag(comments)
  index = 0
  newCommentBox = []
  newComments = []
  for postag in postags:
    # judge the pass of speech
    if postag[1].startswith("JJ") or postag[1].startswith("VB") or postag[1].startswith("NN"):
      newCommentBox.append(postag)
  
  # change to be list
  for word in newCommentBox:
    newComments.append(word[index])
    
  print("Finish tag...\n")
  return newComments


# find positive word in positive-word.txt
def compare_postive(filename):
  compare_postive = tagclassification_comments('1155126875.txt')
  num_positiveWord_match = 0
  
  # change to be list
  positive_word = readTxt(filename)
  positive_word = positive_word.split()
  
  # ignore 1 to 35 lines
  positive_word = positive_word[213:]
  
  for word in compare_postive:
    if word in positive_word:
      print('\''+ word + '\' is positive word')
      num_positiveWord_match = num_positiveWord_match + 1
    else:
      print('\''+ word + '\' is not exist in positive-word.txt')
  print("\n")    
  return num_positiveWord_match
  

# find negative word in negative-word.txt
def compare_negative(filename):
  compare_negative = tagclassification_comments('1155126875.txt')
  num_negativeWord_match = 0
  
  # change to be list
  negative_word = readTxt(filename)
  negative_word = negative_word.split()
  
  # ignore 1 to 35 lines
  negative_word = negative_word[213:]
  
  for word in compare_negative:
    if word in negative_word:
      print('\''+ word + '\' is negative word')
      num_negativeWord_match = num_negativeWord_match + 1
    else:
      print('\''+ word + '\' is not exist in negative-word.txt')
  print("\n")    
  return num_negativeWord_match
  


  
# main function

totalNumber_word = countNumber_comments('1155126875.txt')
effective_comments = tagclassification_comments('1155126875.txt')
countElective_comments = len(effective_comments)
num_positive = compare_postive('positive-word.txt')
num_negative = compare_negative('negative-word.txt')

print("The total words of comments: ", totalNumber_word, "\n")
print("Total effective words: ",countElective_comments, "\n")
print("Total of positive words in comments: " + str(num_positive) + "\n")
print("Total of negative words in comments: " + str(num_negative) + "\n")

num_negative = -(num_negative)
polarity_data = num_positive + num_negative

print("The polarity score: ", str(polarity_data), "\n")

# calculate the score
sentiment_score = polarity_data / totalNumber_word
if sentiment_score > 0:
  print("My comment sentiment score is: ", sentiment_score, "thus overall evaluation is positive\n")
  
else:
  print("My comment score is: ", sentiment_score, "thus overall evaluation is negative\n")

  