from pprint import pprint

from googletrans import Translator, constants

# init the Google API translator
translator = Translator()

# translate a spanish text to english text (by default)
translation = translator.translate("wie gehts es gut")
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

# translate = boto3.client('translate')
# result = translate.translate_text(Text="", SourceLanguageCode="en", TargetLanguageCode="de")