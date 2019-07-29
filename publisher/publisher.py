# -*- coding: utf-8 -*-
"""
@author: Vitor Villar <vitor.luis98@gmail.com>
"""
import urllib

import requests
from abc import ABC, abstractmethod
from exceptions import PublishRejectedError, UnauthorizedPublisherError


class Publisher(ABC):
    mercure_hub = None
    mercure_jwt = None

    def __init__(self, mercure_hub, mercure_jwt):
        self.mercure_hub = mercure_hub
        self.mercure_jwt = mercure_jwt

    @abstractmethod
    def publish(self, topics: list, data: str) -> str:
        """
        Publishes an update to Mercure

        :param list topics: Topics to be published
        :param str data: The Data itself
        :return str: The message ID on mercure on UUID format
        """
        response = requests.post(self.mercure_hub, form_data, headers=headers)

        if response.status_code == 403:
            raise PublishRejectedError(response.text)

        if response.status_code == 401:
            raise UnauthorizedPublisherError(response.text)

        return str(response.text)

    def _check_parameters(self, topics: list, data: str):
        """
        Check if the parameters has the right values

        :param list topics: Topics to be published
        :param str data: The Data itself
        """
        if len(self.mercure_hub) == 0:
            raise AttributeError('Please provide a mercure hub url')

        if len(self.mercure_jwt) == 0:
            raise AttributeError('Please provide a mercure jwt')

        # it has to have at least one topic
        if type(topics) is not list:
            raise TypeError('topics must be a list')
        elif len(topics) == 0:
            raise AttributeError('topics cannot be empty')

        # And data must be a string
        if type(data) is not str:
            raise TypeError('data must be a str')

    def _get_request_headers(self) -> object:
        """
        Return the headers needed by Mercure
        :return object
        """
        return {
            'Authorization': 'Bearer ' + self.mercure_jwt,
            'Content-Type': 'application/x-www-form-urlencoded'
        }

    @staticmethod
    def _get_form_data(topics: list, data: str) -> str:
        form_data = {
            'topic': topics,
            'data': data
        }

        return urllib.parse.urlencode(form_data, True)
