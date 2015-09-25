# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource


class VoiceContext(InstanceContext):

    def __init__(self, version):
        super(VoiceContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {}
        self._uri = "/Voice".format(**self._kwargs)


class VoiceInstance(InstanceResource):

    def __init__(self, version, payload):
        super(VoiceInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'name': payload['name'],
            'url': payload['url'],
            'links': payload['links'],
        }
        
        # Context
        self._lazy_context = None
        self._context_properties = {}

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = VoiceContext(
                self._version,
            )
        return self._lazy_context

    @property
    def name(self):
        """ The name """
        return self._properties['name']

    @property
    def url(self):
        """ The url """
        return self._properties['url']

    @property
    def links(self):
        """ The links """
        return self._properties['links']