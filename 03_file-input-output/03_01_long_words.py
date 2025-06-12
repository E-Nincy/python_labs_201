# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).

file_out =open("long_word.txt", "w")
file_out.write("elephant. Today was a really nice day, supercalifragilisticexpialidocious, codingnomads, extraordinarilylongwordthatmakesnosense, python")
file_out.close()

file_in = open("long_word.txt", "r")
contents = file_in.read()
for word in contents.split():
    if len(word) > 20:
        print(word)
file_in.close()
