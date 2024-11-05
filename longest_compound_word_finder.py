import time

def read_words(filename="Input_01.txt"):
    words = []
    try:
        with open('Input_01.txt', 'r') as file:
            for line in file:
                word = line.strip()
                if word:  
                    words.append(word)
    except FileNotFoundError:
        print(f"Error: File '{'Input_02.txt'}' not found.")
    return words

def is_compound(word, word_set):
    for i in range(1, len(word)):
        prefix = word[:i]
        suffix = word[i:]
        if prefix in word_set and (suffix in word_set or is_compound(suffix, word_set)):
            return True
    return False

def find_longest_compounds(words):
    word_set = set(words)  
    compounds = []

    words = sorted(words, key=len, reverse=True)

    for word in words:
        if is_compound(word, word_set):
            compounds.append(word)
            if len(compounds) == 2: 
                break

    return compounds[0] if compounds else None, compounds[1] if len(compounds) > 1 else None

def main():
    filename = "Input_01.txt" 
    words = read_words('Input_01.txt')

    if not words:
        print("No words to process.")
        return

    start_time = time.time()
    longest, second_longest = find_longest_compounds(words)
    end_time = time.time()

    print("Longest compound word:", longest if longest else "None found")
    print("Second longest compound word:", second_longest if second_longest else "None found")
    print("Time taken:", round(end_time - start_time, 4), "seconds")

if __name__ == "__main__":
    main()
