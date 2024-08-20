#!/usr/bin/env python3
"""Simple helper function"""


import csv
import math
from typing import List, Tuple, Dict, Union, Optional


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
    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
        Retrieve a specific page of data.
        '''
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        data_set = self.dataset()
        total_set_size = math.ceil(len(data_set) / page_size)

        n_index_range = self.index_range(page=page, page_size=page_size)
        if page > total_set_size:
            return []
        return data_set[n_index_range[0]: n_index_range[1]]
    
    # def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Optional[int]]:
    #     """
    #     Get a dictionary containing hypermedia pagination details.
        
    #     :param page: page number (1-indexed)
    #     :param page_size: number of items per page
    #     :return: dictionary with pagination details
    #     """
    #     data = self.get_page(page, page_size)
    #     total_items = len(self.dataset())
    #     total_pages = math.ceil(total_items / page_size)

    #     return {
    #         "page_size": len(data),
    #         "page": page,
    #         "data": data,
    #         "next_page": page + 1 if page < total_pages else None,
    #         "prev_page": page - 1 if page > 1 else None,
    #         "total_pages": total_pages
    #     }
    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Optional[int]]:
        dataset = self.dataset()
        total_item = len(dataset)
        total_page = math.ceil(total_item / page_size)
        page_data = self.get_page(page, page_size)

        return {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': page + 1 if page < total_page else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_page
        }
