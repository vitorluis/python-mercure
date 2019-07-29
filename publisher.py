# -*- coding: utf-8 -*-
"""
@author: Vitor Villar <vitor.luis98@gmail.com>
"""
import urllib

import requests

from exceptions import PublishRejectedError


class Publisher:
    mercure_hub = None
    mercure_jwt = None

    def __init__(self, mercure_hub, mercure_jwt):
        self.mercure_hub = mercure_hub
        self.mercure_jwt = mercure_jwt

    def publish(self, topics: list, data: str) -> str:
        """
        Publishes an update to Mercure

        :param list topics: Topics to be published
        :param str data: The Data itself
        :return str: The message ID on mercure on UUID format

        """
        # it has to have at least one topic
        if type(topics) is not list:
            raise TypeError('topics must be a list')
        elif len(topics) == 0:
            raise AttributeError('topics cannot be empty')

        # And data must be a string
        if type(data) is not str:
            raise TypeError('data must be a str')

        # Create the request
        headers = {
            'Authorization': 'Bearer ' + self.mercure_jwt,
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        form_data = {
            'topic': topics,
            'data': data
        }

        form_data = urllib.parse.urlencode(form_data, True)
        response = requests.post(self.mercure_hub, form_data, headers=headers)

        if response.status_code == 403:
            raise PublishRejectedError(response.text)

        return str(response.text)
