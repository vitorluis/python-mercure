# -*- coding: utf-8 -*-
"""
@author: Vitor Villar <vitor.luis98@gmail.com>
"""
import urllib
from abc import ABC, abstractmethod

from ..message import Message


class Publisher(ABC):
    mercure_hub = None
    mercure_jwt = None
    message = None

    def __init__(self, mercure_hub, mercure_jwt):
        self.mercure_hub = mercure_hub
        self.mercure_jwt = mercure_jwt

    @abstractmethod
    def publish(self, message: Message) -> str:
        """
        Publishes an update to Mercure

        :param list topics: Topics to be published
        :param Message message: The message component with all the update details
        """
        pass

    def _check_parameters(self, message):
        """
        Check if the parameters has the right values

        :param Message message: THe message object
        """
        if len(self.mercure_hub) == 0:
            raise AttributeError('Please provide a mercure hub url')

        if len(self.mercure_jwt) == 0:
            raise AttributeError('Please provide a mercure jwt')

        # it has to have at least one topic
        if type(message.topics) is not list:
            raise TypeError('topics must be a list')
        elif len(message.topics) == 0:
            raise AttributeError('topics cannot be empty')

        # And data must be a string
        if type(message.data) is not str:
            raise TypeError('data must be a str')

        # if target is available, check if its string
        if message.target is not None and type(message.target) is not str:
            raise TypeError('target  must be a string')

        # if message_id is available, check if its string
        if message.message_id is not None and type(message.message_id) is not str:
            raise TypeError('message_id must be a string')

        # if event_type is available, check if its string
        if message.event_type is not None and type(message.event_type) is not str:
            raise TypeError('event_type must be a string')

        # if event_type is available, check if its string
        if message.retry is not None and type(message.retry) is not int:
            raise TypeError('retry must be a integer')

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
    def _get_form_data(message) -> str:
        """
        Encode the message
        :param Message message:
        :return str
        """
        form_data = {
            'topic': message.topics,
            'data': message.data
        }

        if message.target is not None:
            form_data['target'] = message.target

        if message.message_id is not None:
            form_data['id'] = message.message_id

        if message.event_type is not None:
            form_data['type'] = message.event_type

        return urllib.parse.urlencode(form_data, True)
