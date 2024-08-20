#!/usr/bin/env python3
"""Simple helper function"""


def index_range(page, page_size):
    """ return a tuple of size two containing a start index and an end index"""
    start_index = page_size * (1 - page)
    end_index = page_size - start_index
    return [start_index, end_index]
