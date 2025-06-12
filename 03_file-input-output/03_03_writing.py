# Write a script that reads in the contents of `words.txt`
# and writes the contents in reverse to a new file `words_reverse.txt`.

from pathlib import Path

words = Path("C:/Users/escot/OneDrive/Escritorio/Codingnomads/python-201-main/03_file-input-output/words.txt")
reverse_words = Path("C:/Users/escot/OneDrive/Escritorio/Codingnomads/python-201-main/03_file-input-output/words_reverse.txt")

with open(words, "r", encoding="utf-8") as file_in, open(reverse_words, "w", encoding="utf-8") as file_out:
    lines = file_in.readlines()
    reverse_lines = lines[::-1]
    file_out.writelines(reverse_lines)


