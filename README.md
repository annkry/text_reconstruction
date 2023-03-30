# text_reconstruction
In this program, a function will be created that takes a set of words S (located in the polish_words.txt file) and a text without spaces (t) as input, and outputs the text with added spaces to separate words. The function should follow these rules:

After removing spaces, the resulting text should be the same as the original text. Each word (a sequence of characters surrounded by spaces) should belong to the set S. Among all possible divisions of the text into words, the one that maximizes the sum of squared word lengths should be chosen (meaning that longer words are preferred). The program will read input from the zad2_input.txt file (encoded in UTF-8) line by line, and outputs the optimal word divisions for each line to the zad2_output.txt file.

To run a test: python validator.py zad2 python main.py
