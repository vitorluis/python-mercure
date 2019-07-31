# -*- coding: utf-8 -*-
"""
@author: Vitor Villar <vitor.luis98@gmail.com>
"""
import requests
import sseclient


class Consumer:
    mercure_hub = None
    topics = None
    sse_client = None

    def __init__(self, mercure_hub, topics):
        self.mercure_hub = mercure_hub
        self.topics = topics

    def start_consumption(self, callback):
        url = 'http://127.0.0.1:3000/hub?topic=mytopicname'
        response = self._create_request()
        self.sse_client = sseclient.SSEClient(response)

        for event in self.sse_client.events():
            callback(event)

    def _create_request(self):
        return requests.get(self.mercure_hub, stream=True)
