
def word_count(file_name):
    try:
        with open(file_name) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print('File not found')
    else:
        words = contents.split()
        num_words = len(words)
        print( file_name + " has " + str(num_words) + " words")

file_names = ['cats.txt', 'dogs.txt']
for file_name in file_names:
    word_count(file_name)


def word_count(file_name):
    try:
        with open(file_name) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print( file_name + " has " + str(num_words) + " words")

file_names = ['cats.txt', 'dogs.txt']
for file_name in file_names:
    word_count(file_name)