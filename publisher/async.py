# -*- coding: utf-8 -*-
"""
@author: Vitor Villar <vitor.luis98@gmail.com>
"""
import grequests

from ..message import Message
from ..exceptions import PublishRejectedError, UnauthorizedPublisherError
from .publisher import Publisher


class AsyncPublisher(Publisher):

    def publish(self, message: Message) -> str:
        # check the parameters of the request
        self._check_parameters(message)

        # Create the request
        request = grequests.post(
            self.mercure_hub,
            data=Publisher._get_form_data(message),
            headers=self._get_request_headers()
        )

        response = grequests.map([request]).pop(0)

        if response.status_code == 403:
            raise PublishRejectedError(response.text)

        if response.status_code == 401:
            raise UnauthorizedPublisherError(response.text)

        return str(response.text)
