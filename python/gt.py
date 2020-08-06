from googletrans import Translator
import sys

def translate(my_text):
    translator = Translator()
    res = translator.translate(my_text , src='en', dest='fa')
    print (res.text)


translate(sys.argv[1])


#while 1:
#    try:
#        my_text = str(input('enter word:  '))
#        if my_text == 'q':
#            print("Bye!")
#            sys.exit()
#        elif my_text == '':
#         pass
#        else:
#            translate()
#    except KeyboardInterrupt:
#        print("Bye!")
#        sys.exit()
