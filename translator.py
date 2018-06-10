from mstranslator import Translator

translator=Translator('your_own_access_key')

def trans(word):
	return translator.translate(word, lang_from='en', lang_to='pl')
