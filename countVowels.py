"""Write a program that counts the number of vowels in a sentence"""

from collections import Counter

def count_vowels_counter(sentence):
    vowels = "aeiou"
    char_counts = Counter(sentence.lower())
    return sum(char_counts[char] for char in vowels)

# Example usage
user_sentence = input("Please enter a sentence: ")
vowel_count = count_vowels_counter(user_sentence)
print(f"Total number of vowels in the sentence: {vowel_count}")
