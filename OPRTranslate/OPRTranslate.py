from OPRTranslate.Interface.TranslatorInterface import Translator
from OperaPowerRelay import opr
import os, importlib.util




def load_translators(specific_translator: str = None) -> Translator | dict[str, Translator]:
    translators_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Translators")

    translators = {}

    for fileName in os.listdir(translators_path):
        if not fileName.endswith(".py"):
            continue
        translator_name = fileName[:-3] # removes py
        translator_path = os.path.join(translators_path, fileName)

        spec = importlib.util.spec_from_file_location(translator_name, translator_path)    

        tra = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(tra)

        if specific_translator is not None and translator_name == specific_translator: 
                    return tra.get_translator()
        
        if hasattr(tra, "get_translator"):
            translators[translator_name] = tra.get_translator()

    return translators

def main() -> None:

    print("OPR Translate v1.0.0 demo")

    translators = load_translators()

    while True:
        opr.list_choices(translators.keys(), "Select a translator")

        index_translator = opr.input_from("OPR Translate", "Select a translator", 1)
        
        try:
            translator_name = list(translators.keys())[int(index_translator) - 1]
            translator = translators[translator_name]

            opr.print_from("OPR Translate", f"Selected translator: {translator.Name}")
            break

        except (KeyError, IndexError, ValueError):
            opr.print_from("OPR Translate", "Translator not found!")
            continue

    while True:
        opr.list_choices(translator.get_supported_languages(as_dict=True).keys(), "Select a source language")

        index_language = opr.input_from("OPR Translate", "Select a source language (or type your selected language)", 1).lower()
        
        try:

            if index_language in translator.get_supported_languages(as_dict=True).keys():
                source_language = translator.get_supported_languages(as_dict=True)[index_language]
                opr.print_from("OPR Translate", f"Selected source language: {source_language}")
                break

            source_language = translator.get_supported_languages()[int(index_language)-1]
            opr.print_from("OPR Translate", f"Selected source language: {source_language}")
            break

        except (KeyError, IndexError, ValueError):
            opr.print_from("OPR Translate", "Language not found!")
            continue

    while True:
        opr.list_choices(translator.get_supported_languages(as_dict=True).keys(), "Select a target language")

        index_language = opr.input_from("OPR Translate", "Select a target language (or type your selected language)", 1).lower()
        
        try:

            if index_language in translator.get_supported_languages(as_dict=True).keys():
                target_language = translator.get_supported_languages(as_dict=True)[index_language]
                
                break

            source_language = translator.get_supported_languages()[int(index_language)-1]
            break

        except (KeyError, IndexError, ValueError):
            opr.print_from("OPR Translate", "Language not found!")
            continue


    opr.print_from("OPR Translate", f"{source_language} -> {target_language}")
    translator.initialize(source_language, target_language)

    while True:
        text = opr.input_from("OPR Translate", "Enter the text you want to translate (type =exit= to exit)", 1)

        if text == "=exit=": break

        translated = translator.translate(text)

        if translated is not None:
            opr.print_from("OPR Translate", translated)

    opr.wipe()
    print("Goodbye!")