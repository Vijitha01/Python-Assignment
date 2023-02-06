def search(keyword) :
   L1=list()
   L1.append(keyword)
   for i in Thesaurus:
      if i.word==keyword:
         L1=L1+i.synonyms
   result=list()
   for word in L1:
      c=0
      for i in Corpus:
         c=c+i.count(word)
      result.append((word,c))

   return result 

input = "happy"
output = search(input) # invoke the method using a test input
print(output) # prints the output of the function
# do not remove this line!