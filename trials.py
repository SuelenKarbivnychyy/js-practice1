"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    """Print each item in the given array."""
    for item in items:
        print(item)

# output_all_items([1, 'hello', True])      


def get_all_evens(nums):    
    even_nums = []

    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)

    return even_nums   

# print(get_all_evens([7, 8, 10, 1, 2, 2]))     



def get_odd_indices(items):
    result = []

    for idx, item,in enumerate(items):        
        if idx % 2 != 0:            
            result.append(item)

    return result    

# print(get_odd_indices([1, 'hello', True, 500]))     


def print_as_numbered_list(items):
    i = 1

    for item in items:
        print(f" {i}. {item}")

        i += 1

# print_as_numbered_list([1, 'hello', True])    


def get_range(start, stop):
    nums = []

    numbers = range(start, stop)
    for num in numbers:
        nums.append(num)

    return nums

# print(get_range(1,3))     


def censor_vowels(word):
    """Given a string, return a string where vowels are replaced with '*' 
    
    Ex.: censorVowels('hello world')
    'h*ll* w*rld'

    """
    chars = []

    word_as_string = " "

    for letter in word:
        if letter in "aeiou":
            chars.append("*")
        else:
            chars.append(letter)
    
    return word_as_string.join(chars)

# print(censor_vowels('hello world'))             



def snake_to_camel(string):
    """Given a string in snake case, return a string in upper camel case.
    
    Ex.:
    snakeToCamel('hello_world');
    'HelloWorld'
    """

    camel_case = []

    words = string.split("_")

    for word in words:
        camel_case.append(word.title())

    camel_case_string = ""
    return camel_case_string.join(camel_case)

# print(snake_to_camel('hello_world'))    


def longest_word_length(words):
    """Return the length of the longest word in the given array of words.
    
    Ex.:
    longestWordLength(['hello', 'world']);
    5

    > longestWordLength(['jellyfish', 'zebra']);
    9
    """

    longest = len(words[0])

    for word in words:
        if len(word) > longest:
            longest = len(word)

    return longest

# print(longest_word_length(['hello', 'worldjhghfggfc']))        


def truncate(string):
    # Truncate repeating characters into one character.

    #  Ex.:
    #    > truncate('aaaabbbbcccca');
    #    'abca'

    #    > truncate('hi***!!!! wooow');
    #    'hi*! wow'

    result = []

    for char in string:
        if len(result) == 0 or char != result[len(result) -1]:
            result.append(char)
   
    return str("".join(result))

# print(truncate('hi***!!!! wooow'))  




def has_balanced_parens(string):
#    Return true if all parentheses in a given string are balanced.

#  Ex.:
#  > hasBalancedParens('()');
#  true

#  > hasBalancedParens('((This) (is) (good))');
#  true

#  > hasBalancedParens('(Oh no!)(');
#  false
    
    parens = 0

    for char in string:
        if char == "(":
            parens += 1
        elif char == ")":
            parens -= 1

        if parens < 0 :
            return False

    return parens == 0

print(has_balanced_parens('(Oh no!)()'))               


def compress(string):
#      Return a compressed version of the given string.

#  Ex.:
#    > compress('aabbaabb');
#    'a2b2a2b2'

#  If a character appears once, it shouldn't be followed by a number:
#    > compress('abc');
#    'abc'

#  The function should handle all types of characters:
#    > compress('Hello, world! Cows go moooo...');
#    'Hel2o, world! Cows go mo4.3'


    compressed = []

    curr_char = ""
    char_count = 0

    for char in string:
        if char != curr_char:
            compressed.append(curr_char)

            if char_count > 1:
                compressed.append(str(char_count))

            curr_char = char
            char_count = 0    

        char_count += 1

    compressed.append(curr_char)
    if char_count > 1:
        compressed.append(str(char_count))

    return str("".join(compressed))

# print(compress("aabbaabb"))