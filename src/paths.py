''' This module defines the Paths class '''

from os.path import dirname, join

class Paths:
    ''' Paths class '''

    POSTS_FILEPATH = join(dirname(__file__), '..', 'input', 'posts.json')
    OUTPUT_DIRPATH = join(dirname(__file__), '..', 'output')
