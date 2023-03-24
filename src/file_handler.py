''' This module defines the FileHandler class '''

import json

from typing import List

class FileHandler:
    ''' FileHandler class '''

    def save_json_as_txt(self, json_input: List[dict]) -> None:
        ''' Store the JSON input as .txt file '''

        with open(f'../output/{json_input.id}-file.txt', 'w', encoding='utf-8') as txt_file:
            json.dump(json_input, txt_file, ensure_ascii=False, indent=4)

        print('JSON SAVED AS TXT', json_input)
