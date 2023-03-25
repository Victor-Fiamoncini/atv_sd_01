''' This module defines the FileHandler class '''

from os.path import join

import json

from paths import Paths

class FileHandler:
    ''' FileHandler class '''

    def save_json_as_txt(self, json_input: dict) -> str:
        ''' Store the JSON input as .txt file '''

        new_txt_filename = f"post-{json_input.get('id')}.txt"
        txt_filepath = join(Paths.OUTPUT_DIRPATH, new_txt_filename)

        with open(txt_filepath, 'w', encoding='utf-8') as txt_file:
            json.dump(json_input, txt_file, indent=2)

            return txt_filepath
