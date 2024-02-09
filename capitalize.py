"""Write a program that accepts a string as input, capitalizes the first letter of each word in the
string, and then returns the result string."""

def capitalize_words(input_string):
    
    words = input_string.split()

    
    capitalized_words = [word.capitalize() for word in words]


    result_string = ' '.join(capitalized_words)
    return result_string

# Example usage
user_input = "hello world! this is a test string."
capitalized_result = capitalize_words(user_input)
print(capitalized_result)
