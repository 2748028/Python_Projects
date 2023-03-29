print 'Welcome to the Pig Latin Translator!'

pyg = 'ay'

original = raw_input("Enter a word: ")

word = original.lower()

if len(original) > 0 and original.isalpha():
        if word[0] == "a" and "e" and "i" and "o" and "u":
            new_word = word + pyg
            print new_word
            
        else: 
            new_word = word[1:] + word[0] + pyg
            print new_word
else:
    print 'empty'