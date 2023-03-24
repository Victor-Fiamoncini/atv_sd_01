''' This module defines the PostToTxtThreadExecutor class '''

from concurrent import futures
from concurrent.futures import ThreadPoolExecutor

from typing import Generator, List

from file_handler import FileHandler
from mappers import map_post_dto_to_post_dict
from post import Post

class PostToTxtThreadExecutor:
    ''' PostToTxtThreadExecutor class '''

    file_handler: FileHandler = None
    posts: List[Post] = []

    MAX_THREADS: int = 4

    def __init__(self, file_handler: FileHandler, posts: List[Post]) -> Generator[str, str, str]:
        self.file_handler = file_handler
        self.posts = posts

    def execute_concurrently(self) -> Generator:
        ''' Execute the following task concurrently '''

        with ThreadPoolExecutor(max_workers=self.MAX_THREADS) as executor:
            save_file_json_to_txt_futures = [
                executor.submit(self.file_handler.save_json_as_txt, map_post_dto_to_post_dict(post))
                for post in self.posts
            ]

            for future in futures.as_completed(save_file_json_to_txt_futures):
                exception = future.exception()

                yield exception if exception else future.result()