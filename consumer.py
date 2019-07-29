# -*- coding: utf-8 -*-
"""
@author: Vitor Villar <vitor.luis98@gmail.com>
"""


class Consumer:
    mercure_hub = None
    topics = None

    def __init__(self, mercure_hub, topics):
        self.mercure_hub = mercure_hub
        self.topics = topics

    def start(self):
        import json
        import pprint
        import sseclient

        def with_requests(url):
            """Get a streaming response for the given event feed using requests."""
            import requests
            return requests.get(url, stream=True)

        url = 'http://127.0.0.1:3000/hub?topic=mytopicname'
        response = with_requests(url)  # or with_requests(url)
        client = sseclient.SSEClient(response)
        for event in client.events():
            pprint.pprint(json.loads(event.data))