import click
from pywinauto import Application
from pystreamapi import Stream
# from deep_translator import GoogleTranslator

###########

import argostranslate.package
import argostranslate.translate

from_code = "en"
to_code = "zt"
# To enable GPU support, you need to set the ARGOS_DEVICE_TYPE env variable to cuda or auto.

# Download and install Argos Translate package
# argostranslate.package.update_package_index()
# available_packages = argostranslate.package.get_available_packages()
# package_to_install = next(
#     filter(
#         lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
#     )
# )
# argostranslate.package.install_from_path(package_to_install.download())

# Translate
translatedText = argostranslate.translate.translate("Hello World", from_code, to_code)
print(translatedText)

###########

app = Application(backend="uia").connect(title="即時字幕")
last_caption_text = ''
while True:
    caption_text = ''.join(Stream.of(app.top_window().descendants())
                           .filter(lambda x: x.friendly_class_name() == 'Static')
                           .map(lambda x: x.window_text())
                           .to_list())
    if caption_text == last_caption_text:
        continue
    last_caption_text = caption_text
    translatedText = argostranslate.translate.translate(caption_text, from_code, to_code)
    # translatedText = GoogleTranslator(source='auto', target='zh-TW').translate(caption_text)
    click.clear()
    print(translatedText)
    print(caption_text)
