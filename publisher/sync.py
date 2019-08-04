# -*- coding: utf-8 -*-
"""
@author: Vitor Villar <vitor.luis98@gmail.com>
"""
import requests

from ..exceptions import PublishRejectedError, UnauthorizedPublisherError
from ..message import Message
from .publisher import Publisher


class SyncPublisher(Publisher):

    def publish(self, message: Message) -> str:
        # check the parameters of the request
        self._check_parameters(message)

        # Create the request
        response = requests.post(
            self.mercure_hub,
            Publisher._get_form_data(message),
            headers=self._get_request_headers()
        )

        if response.status_code == 403:
            raise PublishRejectedError(response.text)

        if response.status_code == 401:
            raise UnauthorizedPublisherError(response.text)

        return str(response.text)
