
# Longest Compound and Secong Longest Compound Word Finder


This project provides a Python solution to identify the two longest compound words in a list, where each compound word is formed by combining shorter words from the same list. The program reads a list of lowercase words from a file (Input_01.txt), processes them, and outputs the longest and second-longest compound words along with the time taken to complete the search.




## Code Overview: 
The code is structured into four main components:

read_words(filename) - which reads the words from a file and returns a list while skipping any empty lines;

is_compound(word, word_set) - a function that recursively checks if a word can be formed from other words in the list;

find_longest_compounds(words) - which finds the two longest compound words by sorting the words by length and testing each in turn;

main() - which coordinates the functions, handles file input, and displays results. This modular structure ensures clarity and maintainability, allowing each function to focus on a specific task.

## Design Decisions: 
The solution prioritizes straightforward logic over complex data structures. To achieve efficient lookup without sacrificing simplicity, the code uses Python’s set data structure, allowing for O(1) average-time complexity in checking whether a prefix or suffix exists within the list. By sorting words in descending order of length, we quickly identify the longest compound words, stopping the search as soon as the top two are found to save processing time.

## Approach and Justification:
By sorting the list in descending order of word length, we ensure that the longest compound words are processed first, allowing us to exit the search early once we have identified the two longest compounds. While advanced structures like Tries might improve performance in some cases, a set-based solution is well-suited to typical input sizes for this problem, avoiding unnecessary complexity. Each function in this solution has a single, clear purpose, making the code modular and easier to debug or expand. This makes the program accessible to developers looking for a practical and effective solution to the longest compound word problem.

## Getting Started:
To use the program, ensure Python 3.x is installed. Place your word list in Input_01.txt in the same directory as the script or update the filename in the main() function. Run the script with:

python longest_compound_word_finder.py
## Usage

```python
python longest_compound_word_finder.py


```

