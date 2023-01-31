#!/usr/bin/env python3
import csv
import math
from typing import List, Dict
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Init Server"""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the page"""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        self.dataset()
        index = index_range(page, page_size)
        return self.__dataset[index[0]: index[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Return a dictionary"""
        data = self.get_page(page, page_size)
        page_size: len(data)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        next_page = (page + 1) if total_pages > page else None
        prev_page = page - 1 if page > 1 else None
        return {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
