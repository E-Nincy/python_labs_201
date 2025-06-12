# Refactor your file counter script to use `pathlib` also for
# reading and writing to your CSV file. Make sure to handle the
# path in a way so that you can run the script from anywhere.

from pathlib import Path
 
base_dir = Path(__file__).parent.resolve()

file_path = base_dir / "words.txt"
output_file_path = base_dir / "new_words.txt"

with file_path.open("r", encoding="utf-8") as file_in:
    contents = file_in.read()

with output_file_path.open("w", encoding="utf-8") as file_out:
    file_out.write(contents)
    print(contents)
