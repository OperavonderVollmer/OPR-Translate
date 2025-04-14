from OPRTranslate.Interface.TranslatorInterface import Translator
from OperaPowerRelay import opr



class deepl_google(Translator):
    def __init__(self):
        super().__init__()

        self._name = "deepl_google"



    def initialize(self, source_language, target_language):
        super().initialize(source_language, target_language)
    
        from deep_translator import GoogleTranslator
        self._translator = GoogleTranslator(source=source_language, target=target_language)


    def get_supported_languages(self, as_dict=False) -> list[str] | dict[str, str]:
        from deep_translator import GoogleTranslator
        return GoogleTranslator().get_supported_languages(as_dict)


    def translate(self, text, source_language=None, target_language=None):
        super().translate(text, source_language, target_language)

        translated = self._translator.translate(text, source_language=source_language or self._source_language, target_language=target_language or self._target_language)

        return translated
    

    
    

def get_translator() -> Translator:
    return deepl_google()



