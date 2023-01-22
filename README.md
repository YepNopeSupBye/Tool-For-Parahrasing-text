# Tool-For-Parahrasing-text
### Its a tool that paraphrase's simple sentences with using the module nltk
 A video of your program running (1min or less, no voiceover)


https://user-images.githubusercontent.com/89731394/213918050-cdba759f-7827-42b8-af5f-05f07e8f7472.MOV --- link to viedo


###* Summarize program's functionality (what does it do?) and purpose (why does it exist and/or who is it for?)
   - the function of my program is to parahrase simple sentences by changing some or one of the words into a different synomym of that word. Its meant for myself and my friends if we need to parahrase a sentence fast for a project, essay or quick homework.


###* A description, with code segments, of a "breakthrough moment" in which you solved a particularly difficult problem, learned to do something new, or independently overcame being stuck
    - a breakthrough moment I had was just finding the write code to use to parahrase the phrase, in the beginning i coudlnt figure out a way to change the word to a differnt synomym, and even after looking all over the web it was no where the be found, then eventually i tried combinng the different fucntions i had in preivous codes for my parahrser, and it ended up like working. the segament of code was to find a synonym. 
    
   - *for i, word in enumerate(words):*
 
   - *synonyms = wordnet.synsets(word)*


###* An explanation of data abstraction as it is used in your program.
  - Include code segments that show where data is being stored and where data is being retrived and accompanying explanation.
  - Identify what the abstracted data represents in your program
  - Explain how the selected abstraction manages complexity in your program code (why your program code could not be written, or how it would be written differently, if you did not abstract the data in the way you did)

My code uses the Natural Language Toolkit (nltk) library to modify a sentence by replacing each word with a synonym of that word, chosen at random.

Data is being stored in the sentence variable, which holds the sentence "the quick brown fox jumped". This sentence is tokenized into a list of words, which is stored in the words variable.

Data is being retrieved in the for loop, where each word in the words list is passed to the wordnet.synsets(word) function. This function retrieves a list of synonyms for the word, which is stored in the synonyms variable.

The abstracted data in this program represents the list of synonyms for each word in the input sentence.

By abstracting the data in this way, the code is able to manage complexity by not having to hardcode a list of synonyms for each word in the input sentence. Instead, it uses the wordnet module from the nltk library to retrieve the synonyms for each word, which allows for flexibility in handling different words without adding complexity to the code. If the data was not abstracted in this way, the program would need to have a separate list of synonyms for every word in the input sentence.



###* An explanation of procedural abstraction as it is used in your program.
  - Include a single code segment containing:
###* A procedure
  - with a parameter (i.e., takes an argument)
###* and includes an algorithm
  - that uses sequencing, selection, and iteration
###* and returns a value
  - that depends on the arguments given when the procedure is called
###* and is called from elsewhere in the program
  - Explain how the algorithm in the above code segment functions and why it is important for the purpose of your program

My code uses procedural abstraction to modify a sentence by replacing each word with a synonym of that word, chosen at random.

A procedure in this code is the for loop, which takes a single argument words a list of words which are tokenized from the sentence. The for loop uses an algorithm that uses sequencing, selection, and iteration. Specifically, it sequences through each word in the list of tokenized words, selects the synonyms for each word using the wordnet.synsets(word) function, and iterates over the list of synonyms to replace the current word with a random synonym. The procedure returns the modified list of words, which is later joined back into a sentence.

The algorithm in this code segment is important for the purpose of the program because it allows for the modification of the input sentence by replacing each word with a synonym chosen at random, which creates a new sentence with similar meaning.
 
 
###* Explain how the procedural abstraction helps to manage complexity in your program (be specific!)
Procedural abstraction helps to manage complexity in the program by breaking down the problem into smaller, manageable tasks. The for loop isolates the task of finding and replacing synonyms for each word into a separate procedure, which makes the code more organized and easier to understand. Additionally, by creating a procedure, the same task can be reused in other parts of the program, which makes the code more efficient and avoids repeating the same code multiple times.
