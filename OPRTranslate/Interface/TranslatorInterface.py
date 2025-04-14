
from abc import ABC, abstractmethod
from OperaPowerRelay import opr

class Translator(ABC):

    """
    Translates the given text from the source language to the target language.

    Parameters
    ----------
    text : str
        The text to be translated.
    source_language : str, optional
        The source language of the text. If not provided, defaults to the translator's source language.
    target_language : str, optional
        The target language for translation. If not provided, defaults to the translator's target language.

    Returns
    -------
    str or None
        The translated text if successful, or None if translation fails.
        
    Notes
    -----
    Each subclass that implements this interface is responsible for setting the translator's name.
    """


    def __init__(self):

        self._name = None 
        self._source_language = None
        self._target_language = None
        self._translator = None
        self._initialized = False
    
    def initialize(self, source_language: str, target_language: str):

        """
        Initializes the translator with the given source and target languages.

        Parameters
        ----------
        source_language : str
            The source language of the text.
        target_language : str
            The target language of the text.
        """

        self._source_language = source_language
        self._target_language = target_language
        self._initialized = True

    @abstractmethod
    def get_supported_languages(self, as_dict=False):
        pass

    @abstractmethod
    def translate(self, text: str, source_language: str = None, target_language: str = None) -> str | None:
        if not self._initialized:
            opr.print_from(self.Name, "Translator not initialized!")
            return

        pass

    @property
    def Name(self):
        
        return self._name
