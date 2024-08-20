#!/usr/bin/env python3
"""Simple helper function"""


import csv
import math
from typing import List, Tuple


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

    @staticmethod
    def index_range(page: int, page_size: int) -> tuple:
        """return a tuple of size two containing
        a start index and an end index"""
        start_index = page_size * (page - 1)
        end_index = page_size + start_index
        return (start_index, end_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        dataset = self.dataset()
        total_size_page = math.ceil(len(dataset) / page_size)
        if page > total_size_page:
            return []
        start_index, end_index = self.index_range(page, page_size)
        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        dataset = self.dataset()
        total_item = len(dataset)
        total_page = (total_item + page_size - 1)
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        page_data = self.get_page(page=page, page_size=page_size)
        return {
            'page_size' : page_size,
            'page' : page,
            'data' : page_data,
            'next_page' : page + 1 if page < total_page else None,
            'prev_page' : page - 1 if page > 1 else None,
            'total_page' : total_page
        }
# page_size
# page
# data
# next_page
# prev_page
# total_pages