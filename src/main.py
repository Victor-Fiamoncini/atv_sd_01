''' Main program module '''

from os import listdir, remove
from os.path import join

import json

from decorators import benchmark
from file_handler import FileHandler
from mappers import map_post_dict_to_post_dto
from paths import Paths
from post_to_txt_thread_executor import PostToTxtThreadExecutor

def remove_all_txt_files_from_output() -> None:
    ''' Removes all .txt files from output directory '''

    output_files = listdir(Paths.OUTPUT_DIRPATH)
    output_txt_files = filter(lambda file: file.endswith('.txt'), output_files)

    for txt_file in list(output_txt_files):
        path_to_file = join(Paths.OUTPUT_DIRPATH, txt_file)

        remove(path_to_file)

@benchmark
def main() -> None:
    ''' Main program entrypoint '''

    try:
        remove_all_txt_files_from_output()

        file_handler = FileHandler()

        with open(Paths.POSTS_FILEPATH, encoding='utf-8') as posts_json_file:
            posts_file_text_content = posts_json_file.read()
            parsed_posts_json = json.loads(posts_file_text_content)

            mapped_posts = map(map_post_dict_to_post_dto, parsed_posts_json)
            post_to_txt_thread_executor = PostToTxtThreadExecutor(file_handler, list(mapped_posts))

            for generated_filename in post_to_txt_thread_executor.execute_concurrently():
                print(f'File generated: {generated_filename}')
    except Exception as ex:
        print(f'An error has occurred: {ex}')

if __name__ == '__main__':
    main()
