# -*- coding: utf-8 -*-
"""
@author: Vitor Villar <vitor.luis98@gmail.com>
"""
import requests

from exceptions import PublishRejectedError, UnauthorizedPublisherError
from .publisher import Publisher


class SyncPublisher(Publisher):

    def publish(self, topics: list, data: str) -> str:
        """
        Publishes an update to Mercure

        :param list topics: Topics to be published
        :param str data: The Data itself
        :return str: The message ID on mercure on UUID format
        """
        # check the parameters of the request
        self._check_parameters(topics, data)

        # Create the request
        response = requests.post(
            self.mercure_hub,
            Publisher._get_form_data(topics, data),
            headers=self._get_request_headers()
        )

        if response.status_code == 403:
            raise PublishRejectedError(response.text)

        if response.status_code == 401:
            raise UnauthorizedPublisherError(response.text)

        return str(response.text)
