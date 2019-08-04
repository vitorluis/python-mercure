# -*- coding: utf-8 -*-
"""
@author: Vitor Villar <vitor.luis98@gmail.com>
"""


class Message:
    data = None
    target = None
    message_id = None
    event_type = None
    retry = None
    topics = None

    def __init__(self, topics, data, target=None, message_id=None, event_type=None, retry=None):
        """
        Defines a message

        :param list topics:  Which topics this message will be published
        :param str data: Data itself
        :param str target: Target audience of this update. This key can be present several times. (Optional)
        :param str message_id: The topic's revision identifier: it will be used as the SSE's id property (Optional)
        :param str event_type: The SSE's event property (a specific event type) (Optional)
        :param int retry:  The SSE's retry property (the reconnection time) (Optional)
        """
        self.topics = topics
        self.data = data
        self.target = target
        self.message_id = message_id
        self.event_type = event_type
        self.retry = retry
