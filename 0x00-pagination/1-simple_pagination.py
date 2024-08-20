#!/usr/bin/env python3
"""Simple helper function"""


import csv
import math
from typing import List, Tuple


# def index_range(page: int, page_size: int) -> tuple:
#         """return a tuple of size two containing
#         a start index and an end index"""
#         start_index = page_size * (page - 1)
#         end_index = page_size + start_index
#         return (start_index, end_index)

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

    # def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
    #     """
    #     Get a page from the dataset.
        
    #     :param page: page number (1-indexed)
    #     :param page_size: number of items per page
    #     :return: list of rows corresponding to the requested page
    #     """
    #     assert isinstance(page, int) and page > 0,"`"
    #     assert isinstance(page_size, int) and page_size > 0,"d"
    #     dataset = self.dataset()
    #     start_index, end_index = self.index_range(page, page_size)
    #     if start_index >= len(dataset):
    #         return []
    #     return dataset[start_index:end_index]
    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page from the dataset.
        
        :param page: page number (1-indexed)
        :param page_size: number of items per page
        :return: list of rows corresponding to the requested page
        """
        assert isinstance(page, int) and page > 0, "page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "page_size must be a positive integer"

        dataset = self.dataset()
        start_index, end_index = self.index_range(page, page_size)

        # If the start_index is out of range, return an empty list
        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]