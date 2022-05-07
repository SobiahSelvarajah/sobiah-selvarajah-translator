from translate import Translator

try:
    with open('./data.txt', mode='r') as my_file:
        text = my_file.read()
        translator = Translator(to_lang='it')
        translation = translator.translate(text)
        print(translation)
        with open('./test-it.txt', mode='w') as my_file2:
            my_file2.write(translation)
except FileNotFoundError as err:
    print('file does not exist')
    raise err
except IOError as err:
    print('IO error')
    raise err
