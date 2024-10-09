import sys

# Assuming the BloomFilter class is already defined as above

def load_spam_signatures(bloom_filter, spam_file):
    """
    Load spam signatures from a file into the Bloom filter.

    :param bloom_filter: Instance of BloomFilter.
    :param spam_file: Path to the spam signatures file.
    """
    with open(spam_file, 'r') as f:
        for line in f:
            signature = line.strip().lower()
            if signature:
                bloom_filter.add(signature)

def is_spam(bloom_filter, email_content):
    """
    Check if an email is potentially spam based on its content.

    :param bloom_filter: Instance of BloomFilter.
    :param email_content: Content of the email to check.
    :return: True if potentially spam, False otherwise.
    """
    words = email_content.lower().split()
    for word in words:
        if word in bloom_filter:
            return True  # Potential spam detected
    return False

if __name__ == "__main__":
    # Parameters for the Bloom filter
    BLOOM_SIZE = 1000000  # Adjust based on number of spam signatures
    HASH_COUNT = 7         # Number of hash functions

    # Initialize Bloom filter
    bloom = BloomFilter(size=BLOOM_SIZE, hash_count=HASH_COUNT)

    # Load spam signatures (e.g., a file with one spam keyword per line)
    spam_signatures_path = 'spam_signatures.txt'  # Replace with your spam signatures file path
    print("Loading spam signatures into Bloom filter...")
    load_spam_signatures(bloom, spam_signatures_path)
    print("Spam signatures loaded.")

    # Example email contents
    emails = [
        "Congratulations! You've won a free lottery. Click here to claim.",
        "Hi John, can we schedule a meeting for tomorrow?",
        "Limited time offer! Buy now and save 50%.",
        "Don't forget to submit your report by EOD."
    ]

    for idx, email in enumerate(emails, 1):
        if is_spam(bloom, email):
            print(f"Email {idx}: Potential Spam Detected.")
        else:
            print(f"Email {idx}: Clean.")
