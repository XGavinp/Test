import sys
import hashlib
from typing import List


class BloomFilter:
    def __init__(self, size: int, num_hashes: int):
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = [0] * size

    def _hashes(self, item: str) -> List[int]:
        """Generate hash values for the item."""
        hash_values = []
        for i in range(self.num_hashes):
            hash_value = int(hashlib.sha256((item + str(i)).encode()).hexdigest(), 16) % self.size
            hash_values.append(hash_value)
        return hash_values

    def add(self, item: str) -> None:
        """Add an item to the Bloom filter."""
        for hash_value in self._hashes(item):
            self.bit_array[hash_value] = 1

    def check(self, item: str) -> bool:
        """Check if an item is in the Bloom filter."""
        return all(self.bit_array[hash_value] for hash_value in self._hashes(item))


def load_words_from_file(file_path: str) -> List[str]:
    """Load words from a given file."""
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]


def spellcheck(dictionary_file: str, words_to_check_file: str) -> None:
    """Perform spell checking."""
    print("Loading dictionary into Bloom filter...")
    dictionary = load_words_from_file(dictionary_file)
    bloom_filter = BloomFilter(size=1000, num_hashes=5)

    for word in dictionary:
        bloom_filter.add(word)
    print("Dictionary loaded.")

    # Load words to check
    words_to_check = load_words_from_file(words_to_check_file)

    for word in words_to_check:
        if bloom_filter.check(word):
            print(f"'{word}': Possibly spelled correctly.")
        else:
            print(f"'{word}': Definitely misspelled.")


def spam_detection(spam_file: str, emails_to_check_file: str) -> None:
    """Detect spam in emails."""
    print("Loading spam signatures into Bloom filter...")
    spam_signatures = load_words_from_file(spam_file)
    bloom_filter = BloomFilter(size=1000, num_hashes=5)

    for signature in spam_signatures:
        bloom_filter.add(signature)
    print("Spam signatures loaded.")

    # Load emails to check
    emails_to_check = load_words_from_file(emails_to_check_file)

    for email in emails_to_check:
        if any(bloom_filter.check(word) for word in email.split()):
            print("Potential Spam Detected.")
        else:
            print("Clean.")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage:")
        print("For spell checking: python bloom_app.py spellcheck <dictionary_file> <words_to_check_file>")
        print("For spam detection: python bloom_app.py spam <spam_file> <emails_to_check_file>")
        sys.exit(1)

    mode = sys.argv[1]
    if mode == "spellcheck":
        spellcheck(sys.argv[2], sys.argv[3])
    elif mode == "spam":
        spam_detection(sys.argv[2], sys.argv[3])
    else:
        print("Invalid mode. Use 'spellcheck' or 'spam'.")
