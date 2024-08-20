#!/usr/bin/env python3
"""Simple helper function"""


import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page, page_size):
        """return a tuple of size two containing
        a start index and an end index"""
        start_index = page_size * (page - 1)
        end_index = page_size + start_index
        return (start_index, end_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
            if (page > len(page) or len(page_size)):
                return []
            assert page and page_size != 0
            return self.index_range(page, page_size)
