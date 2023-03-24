''' This module defines the JsonToTxtThreadExecutor class '''

from concurrent import futures
from concurrent.futures import ThreadPoolExecutor

from typing import Generator, List

from file_handler import FileHandler

class JsonToTxtThreadExecutor:
    ''' JsonToTxtThreadExecutor class '''

    file_handler: FileHandler = None
    jsons: List[dict] = []

    MAX_THREADS: int = 4

    def __init__(self, file_handler: List[dict], jsons: List[dict]) -> None:
        self.file_handler = file_handler
        self.jsons = jsons

    def execute_concurrently(self) -> None:
        ''' Execute the following task concurrently '''

        with ThreadPoolExecutor(max_workers=self.MAX_THREADS) as executor:
            save_file_json_to_txt_futures = [
                executor.submit(self.file_handler.save_json_as_txt, json)
                for json in self.jsons
            ]

            for future in futures.as_completed(save_file_json_to_txt_futures):
                exception = future.exception()

                yield exception if exception else future.result()
