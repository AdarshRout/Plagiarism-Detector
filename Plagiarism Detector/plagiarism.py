from difflib import SequenceMatcher

with open('demo.txt') as one_file, open('againdemo.txt') as two_file:
    data_file = one_file.read()
    data_myfile = two_file.read()

    matches = SequenceMatcher(None, data_file, data_myfile).ratio()
    print(f" The Plagiarised content is {matches*100}% ")