''' This module defines the FileHandler class '''

import os
import json

class FileHandler:
    ''' FileHandler class '''

    def save_json_as_txt(self, json_input: dict) -> str:
        ''' Store the JSON input as .txt file '''

        txt_file_path = f"{os.path.dirname(__file__)}/../output/post-{json_input.get('id')}.txt"

        with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
            json.dump(json_input, txt_file, ensure_ascii=False, indent=2)

            return txt_file_path
