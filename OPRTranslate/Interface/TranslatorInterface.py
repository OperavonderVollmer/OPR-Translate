
from abc import ABC, abstractmethod
from OperaPowerRelay import opr

class Translator(ABC):

    """
    Abstract class for a translator that can translate text from one language to another.

    Parameters
    ----------
    source_language : str
        The source language to translate from.
    target_language : str
        The target language to translate to.

    Attributes
    ----------
    Name : str
        The name of the translator.
    source_language : str
        The source language to translate from.
    target_language : str
        The target language to translate to.
    translator : object
        The translator object that can be used to translate text.
    initialized : bool
        Whether the translator has been initialized or not.

    Methods
    -------
    translate(text : str) -> str
        Translates the given text from the source language to the target language.
    get_supported_languages(as_dict : bool = False) -> list[str] | dict[str, str]
        Returns a list of supported languages or a dictionary of supported languages
        with their corresponding language codes.
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




        
    def get_supported_languages(self, as_dict=False):
        """
        Returns a list of supported languages or a dictionary of supported languages
        with their corresponding language codes if as_dict is True.

        Parameters
        ----------
        as_dict : bool
            If True, returns a dictionary of supported languages with their
            corresponding language codes. If False, returns a list of supported
            languages.

        Returns
        -------
        list or dict
            A list of supported languages or a dictionary of supported languages
            with their corresponding language codes.
        """
        pass

    @abstractmethod
    def translate(self, text: str, source_language: str = None, target_language: str = None) -> str | None:

        """
        Translates the given text from the given source language to the given target language.

        If source_language and target_language are not provided, the source and target languages
        set during initialization are used.

        Parameters
        ----------
        text : str
            The text to translate.
        source_language : str, optional
            The source language of the text. Defaults to None.
        target_language : str, optional
            The target language of the text. Defaults to None.

        Returns
        -------
        str | None
            The translated text or None if the translator is not initialized.
        """

        if not self._initialized:
            opr.print_from(self.Name, "Translator not initialized!")
            return




    @property
    def Name(self):        
        return self._name
