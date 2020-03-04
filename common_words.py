#The common_words.py program reads the book Uncle Tom's Cabin
#After reading the text files of the book, it will count 
#The number of instances of a particular word

filename = 'UncleTom.txt'

try:
    with open(filename, encoding='utf-8') as book:
        contents = book.read()

except FileNotFoundError:
    print(f"Sorry Uncle {filename} does not exist.")

else:
    total = contents.lower()
    total2 = total.split()
    overall = total2.count('the ')
    print(f"The total number of the instance 'the ' is: {overall}") 
