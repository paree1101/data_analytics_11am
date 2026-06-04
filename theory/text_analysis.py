#Step 1: Define a string
givenstring = "Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."
#Step 2: Define the class and its attributes
class TextAnalyser(object):
    def __init__(self, text):
        self.text = text
        # remove punctuation
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
        # make all words lowercase
        formattedText = formattedText.lower()

        self.fmtText = formattedText # store the formatted text as an attribute

        #Step 4: Implement a code to count the frequency of all unique words
    def freqAll(self):        
        # split text into words
        wordList = self.fmtText.split(' ')
        # create a dictionary to store word frequencies
        freqMap = {} #Creates an empty dictionary that will store each word as a key and its frequency as the value.
        for word in set(wordList): # set(wordList) removes duplicates, so the loop only iterates over unique words — avoiding redundant counting.
            freqMap[word] = wordList.count(word) # count the frequency of each unique word and store in dictionary
        
        return freqMap

        #Step 5: you have to implement the freqOf(word) method that takes a word argument Create a method and pass the word that needs to be found.
    def freqOf(self, word):
         # get frequency map
        freqDict = self.freqAll() # call the freqAll method to get the frequency dictionary of all words in the text. This allows us to look up the frequency of the specified word.
        
        if word in freqDict:
            return freqDict[word]
        else:
            return 0


#Test the class and its methods
analyzed = TextAnalyser(givenstring)
print("Formatted Text:", analyzed.fmtText)

# Get frequency of all unique words
freqMap = analyzed.freqAll()
print(freqMap)

# Call the function that counts the frequency of the word "lorem".
word = "lorem"
frequency = analyzed.freqOf(word)
print("The word",word,"appears",frequency,"times.")

