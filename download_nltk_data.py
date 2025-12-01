#!/usr/bin/env python3
"""
Download required NLTK data packages.
Run this script once to download all necessary NLTK resources.
"""

import nltk

print("Downloading NLTK data packages...")
print("-" * 50)

# Download punkt tokenizer (required for older NLTK versions)
print("Downloading punkt...")
nltk.download('punkt')

# Download punkt_tab tokenizer (required for newer NLTK versions)
print("Downloading punkt_tab...")
nltk.download('punkt_tab')

# Download other commonly used NLTK data
print("\nDownloading additional useful packages...")
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

print("-" * 50)
print("✓ All NLTK data packages downloaded successfully!")
print("You can now run your NLP code without errors.")
