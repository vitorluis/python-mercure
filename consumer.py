# -*- coding: utf-8 -*-
"""
@author: Vitor Villar <vitor.luis98@gmail.com>
"""
import urllib
from threading import Thread

import requests
import sseclient

from .message import Message


class Consumer(Thread):
    mercure_hub = None
    topics = None
    sse_client = None
    callback = None

    def __init__(self, mercure_hub, topics, callback):
        super().__init__()

        self.mercure_hub = mercure_hub
        self.topics = topics
        self.callback = callback

    def start_consumption(self):
        """
        Consumes the message into a new thread
        :return:
        """
        response = self._create_request()
        self.sse_client = sseclient.SSEClient(response)
        self.start()

    def run(self) -> None:
        """
        Start the event listening
        """
        for event in self.sse_client.events():
            # Create a new message object for each new income message
            msg = Message(self.topics, event.data, message_id=event.id, event_type=event.event)
            self.callback(msg)

    def _create_request(self):
        """
        Creates the request needed to get the messages

        :return requests.api: The response object
        """
        url = "{}?{}".format(self.mercure_hub, self._create_consumer_query_string())
        return requests.get(url, stream=True)

    def _create_consumer_query_string(self):
        """
        Creates the url with the topic parameters

        :return str: the whole url needed to call mercure
        """
        return urllib.parse.urlencode({
            'topic': self.topics
        }, True)
