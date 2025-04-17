# OPR-Translate

**OPR-Translate** provides a simple, consistent, and predictable way for using different translation engines across different use cases.

## Installation

### Prerequisites

- Python 3.x
- Required dependencies (install using pip):
  ```sh
  pip install -r requirements.txt
  ```

### Manual Installation

1. Clone or download the repository.
2. Navigate to the directory containing `setup.py`:
   ```sh
   cd /path/to/OperaPowerRelay
   ```
3. Install the package in **editable mode**:
   ```sh
   pip install -e .
   ```

### Installing via pip
```sh
pip install git+https://github.com/OperavonderVollmer/OPR-Translate.git@main
```

## Usage

### Importing as a Module

Once installed, you can now select a translator amongst the installed translators via accessing [OPRTranslate](https://github.com/OperavonderVollmer/OPR-Translate/blob/main/OPRTranslate/OPRTranslate.py)'s load_translators function.

You could also access the translators directly, but using the other method is more programmatic and ensures scalability without having to program for every little change.

### Adding more translators

Using the abstract class [Translator](https://github.com/OperavonderVollmer/OPR-Translate/blob/main/OPRTranslate/Interface/TranslatorInterface.py), create a class and put it inside the [Translators](https://github.com/OperavonderVollmer/OPR-Translate/tree/main/OPRTranslate/Translators) folder.

Make sure that both the class and the filename are the same, since [OPRTranslate](https://github.com/OperavonderVollmer/OPR-Translate/blob/main/OPRTranslate/OPRTranslate.py)'s load_translators function relies on the class and file names to have the same name

Add a get_translator function that returns the created class inside the python file, as seen [here](https://github.com/OperavonderVollmer/OPR-Translate/blob/main/OPRTranslate/Translators/deepl_google.py).

## Current Options
- [DeepL (Google Translate)](https://github.com/DeepLcom/deepl-python)
