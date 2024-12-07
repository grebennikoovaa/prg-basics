def num_of_words(text):
   words = text.split()
   return len(words)


def ordered(text):
   words = text.split()
   sorted_words = sorted(words, key=len, reverse=True)
   for i in sorted_words:
      i = str(i)
      print(i, end=" ")
   return i

   
def alphabetically(text):
   words = text.split()
   sorted_word = sorted(words)
   for i in sorted_word:
      i = str(i)
      print(i, end= " ")
   return i