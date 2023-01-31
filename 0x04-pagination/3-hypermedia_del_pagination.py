#!/usr/bin/env python3
""" Deletion-resilient hypermedia pagination """
import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Init Server"""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return a dictionary with the hyper_index"""
        assert isinstance(index, int)
        assert index <= list(self.__indexed_dataset.keys())[-1]
        next_index = index + page_size
        data = []
        i = index
        while i < next_index:
            try:
                data.append(self.__indexed_dataset[i])
            except Exception:
                next_index += 1
            i += 1
        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
        }
