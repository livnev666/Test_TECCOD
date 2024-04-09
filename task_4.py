# task 4

def list_of_lines(text):

    print(sorted([len(letter.replace(' ', '').lower()) for letter in text]))
    print(sorted([len(letter.replace(' ', '').lower()) for letter in text], reverse=True))


list_of_lines(['qwerty qwdffgvbvbnnb', 'asdfg hgghyuw', 'zxcfgfgyuyu', 'qwertyyuuiioppaSSDFDFD'])