''' Main program module '''

import os
import json

from decorators import benchmark
from file_handler import FileHandler
from mappers import map_post_dict_to_post_dto
from post_to_txt_thread_executor import PostToTxtThreadExecutor

file_handler = FileHandler()

posts_json_filepath = f'{os.path.dirname(__file__)}/../input/posts.json'
output_txt_directory_path = f'{os.path.dirname(__file__)}/../output'

def remove_all_txt_files_from_output() -> None:
    ''' Removes all .txt files from output directory '''

    output_files = os.listdir(output_txt_directory_path)
    output_txt_files = filter(lambda file: file.endswith('.txt'), output_files)

    for txt_file in list(output_txt_files):
        path_to_file = os.path.join(output_txt_directory_path, txt_file)

        os.remove(path_to_file)

@benchmark
def main() -> None:
    ''' Main program start '''

    remove_all_txt_files_from_output()

    with open(posts_json_filepath, encoding='utf-8') as posts_json_file:
        posts_file_text_content = posts_json_file.read()
        parsed_posts_json = json.loads(posts_file_text_content)

        mapped_posts = map(map_post_dict_to_post_dto, parsed_posts_json)
        post_to_txt_thread_executor = PostToTxtThreadExecutor(file_handler, list(mapped_posts))

        for generated_filename in post_to_txt_thread_executor.execute_concurrently():
            print(f'File generated: {generated_filename}')

if __name__ == '__main__':
    main()
