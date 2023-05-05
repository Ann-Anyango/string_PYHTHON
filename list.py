
# Write a Python program to get a single string
# from two given strings, separated by a space, and swap
# the first two characters of each string
def stream_strings(str1, str2):
    work_str1 = str2[2:] + str1[:2]
    work_str2 = str1[2:] + str2[:2]
    result = work_str1 + ' ' + work_str2
    return result
str1 = 'Ann'
str2 = 'Anyango'
result = stream_strings(str1, str2)
print(result)
#  Write a Python function that takes a list of words
# and returns the longest word and the length
# # of the longest one
def longest_words(words):
    longest_word = ''
    longest_length = 0
    for word in words:
        if len(word) > longest_length:
            longest_word = word
            longest_length = len(word)
    return longest_word, longest_length
words = ['apple', 'banana', 'cherry', 'durian']
longest_word, length = longest_words(words)
print(longest_word)
print(length)
# # Write a Python program that accepts a comma-separated
# sequence of words as input and prints the distinct
# words in sorted form (alphanumerically).
# words = input("Enter a comma-separated sequence of words: ")
# words_list = words.split(',')
# distinct_words = set(words_list)
# sorted_words = sorted(distinct_words)
# print("Distinct words in sorted order:", ', '.join(sorted_words))
# # Write a Python function that takes two lists and returns True if they have at least one common member.
def common_member(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
result = common_member(list1, list2)
print(result)
# # Write a Python program to convert a list to a list of dictionaries.
# # Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
keys = ["color_name", "color_code"]
values = [["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]]
result = []
for i in range(len(values[0])):
    dict = {}
    for j in range(len(keys)):
        dict[keys[j]] = values[j][i]
    result.append(dict)
print(result)
# [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'},{'color_name': 'Maroon', 'color_code': '#800000'},{'color_name': 'Yellow', 'color_code': '#FFFF00'}]
# # Write a Python program to check whether all dictionaries in a list are empty or not
def empty_dic(dict_list):
    for dictionary in dict_list:
        if bool(dictionary):
            return False
    return True
dict_list1 = [{}, {}, {}]
dict_list2 = [{}, {"name": "Alice"}, {}]
print(empty_dic(dict_list1))
print(empty_dic(dict_list2))
# #  Given a list of numbers, use list comprehension to remove all odd numbers from the list:
# numbers = [3, 5, 45, 97, 32, 22, 10, 19, 39, 43]
# evens = [x for x in numbers if x % 2 == 0]
# print(evens)
# #  Find the common numbers in two lists (without using a tuple or set)
list_a = 1, 2, 3, 4,
list_b = 2, 3, 4, 5
con_numbers = []
for number in list_a:
    if number in list_b and number not in con_numbers:
        con_numbers.append(number)
print(con_numbers)
# # Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit besides
# divisible_numbers = [num for num in range(1, 1001) if any(num % digit == 0 and digit != 1 and digit != num for digit in range(2, 10))]
# print(divisible_numbers)
# #  Write a Python function to remove all vowels in a string
def rew_vowels(string):
    vowels = "AEIOUaeiou"
    result = ""
    for chara in string:
        if chara not in vowels:
            result += chara
    return result
my_string = "Hello,poeple!"
new_string = rew_vowels(my_string)
print(new_string)





    