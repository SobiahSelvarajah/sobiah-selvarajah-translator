from translate import Translator

try:
    with open('./data.txt', mode='r') as my_file:
        # print(my_file.read())
        text = my_file.read()
        translator = Translator(to_lang='it')
        translation = translator.translate(text)
        print(translation)
except FileNotFoundError as err:
    print('file does not exist')
    raise err
except IOError as err:
    print('IO error')
    raise err
