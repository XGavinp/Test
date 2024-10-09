import sys

# Assuming the BloomFilter class is already defined as above

def load_dictionary(bloom_filter, dictionary_file):
    """
    Load words from a dictionary file into the Bloom filter.

    :param bloom_filter: Instance of BloomFilter.
    :param dictionary_file: Path to the dictionary file.
    """
    with open(dictionary_file, 'r') as f:
        for line in f:
            word = line.strip().lower()
            if word:
                bloom_filter.add(word)

def spell_check(bloom_filter, word):
    """
    Check if a word is possibly spelled correctly.

    :param bloom_filter: Instance of BloomFilter.
    :param word: Word to check.
    :return: True if possibly correct, False if definitely incorrect.
    """
    return word.lower() in bloom_filter

if __name__ == "__main__":
    # Parameters for the Bloom filter
    BLOOM_SIZE = 1000000  # Adjust based on dictionary size
    HASH_COUNT = 7        # Number of hash functions

    # Initialize Bloom filter
    bloom = BloomFilter(size=BLOOM_SIZE, hash_count=HASH_COUNT)

    # Load dictionary (e.g., a file with one word per line)
    dictionary_path = 'english_dictionary.txt'  # Replace with your dictionary file path
    print("Loading dictionary into Bloom filter...")
    load_dictionary(bloom, dictionary_path)
    print("Dictionary loaded.")

    # Example spell checks
    test_words = ['example', 'speling', 'correct', 'wrng']
    for word in test_words:
        if spell_check(bloom, word):
            print(f"'{word}': Possibly spelled correctly.")
        else:
            print(f"'{word}': Definitely misspelled.")
