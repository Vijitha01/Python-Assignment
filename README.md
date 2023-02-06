# Python-Assignment
the parameter to the function is the “keyword” for which to search. Your
program can also access two other variables that you will need to complete the program:
Computational Thinking For Problem Solving |Assignment 4.7 | Property of Penn Engineering
● Thesaurus, which is a list of Entry objects; each Entry object has a word attribute,
which is a string of characters; and an attribute called synonyms, which is a list of
strings
● Corpus, which is a list of lists of strings
For example, the Entry class and Thesaurus variable may be defined like this:

class Entry :
 def __init__(self, input_word, input_synonyms) :
 self.word = input_word
 self.synonyms = input_synonyms
e1 = Entry("dog", ["doggie", "puppy"])
e2 = Entry("cat", ["kitty"])
Thesaurus = [e1, e2]
Note that the first argument to the Entry constructor is the word in the thesaurus, and the
second is the list of words that are its synonyms. All words consist only of lowercase letters.
And the Corpus variable may be defined like this:
doc1 = [“this”, “is”, “a”, “single”, “document”]
doc2 = [“here”, “is”, “another”, “document”]
Corpus = [doc1, doc2]
Each document is represented as a list of words, which are all lowercase letters, and the
Corpus is a list containing those lists.
You can access the Thesaurus and Corpus variables in your program without having to define
them; they have already been defined and initialized with words and phrases describing a
person’s emotions -- happy, sad, angry, etc. -- in the setup of this activity. For your own testing
purposes, you can create your own Thesaurus and Corpus and populate them with your own
data, but please do so outside the function definition, and keep in mind that the correctness of
your function will be determined using the Thesaurus and Corpus that we have provided.
Your “search” function should implement the algorithm described by the pseudocode above by
using the Thesaurus to find the keyword’s synonyms, and then reporting the number of
occurrences of the keyword and its synonyms in all documents in the Corpus.
The output of your function should be a list of tuples, in which the first element of the tuple is the
word that was searched for (either the keyword or one of its synonyms) and the second is its
total number of occurrences.
For instance, if the keyword was “cat” and it occurred 120 times, and its synonym was “kitty” and
it occurred 84 times, the output should be:
[ (“cat”, 120), (“kitty”, 84) ]
Hint: You can create a tuple variable like this:
result = (“cat”, 120)
And then add it to a list using the list’s “append” function
