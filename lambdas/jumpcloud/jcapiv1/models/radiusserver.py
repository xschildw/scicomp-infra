# coding: utf-8

"""
    JumpCloud APIs

    V1 & V2 versions of JumpCloud's API. The previous version of JumpCloud's API. This set of endpoints allows JumpCloud customers to manage commands, systems, & system users.

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Radiusserver(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'organization': 'str',
        'network_source_ip': 'str',
        'shared_secret': 'str',
        'name': 'str',
        'tags': 'list[str]',
        'tag_names': 'list[str]'
    }

    attribute_map = {
        'id': '_id',
        'organization': 'organization',
        'network_source_ip': 'networkSourceIp',
        'shared_secret': 'sharedSecret',
        'name': 'name',
        'tags': 'tags',
        'tag_names': 'tagNames'
    }

    def __init__(self, id=None, organization=None, network_source_ip=None, shared_secret=None, name=None, tags=None, tag_names=None):
        """
        Radiusserver - a model defined in Swagger
        """

        self._id = None
        self._organization = None
        self._network_source_ip = None
        self._shared_secret = None
        self._name = None
        self._tags = None
        self._tag_names = None

        if id is not None:
          self.id = id
        if organization is not None:
          self.organization = organization
        if network_source_ip is not None:
          self.network_source_ip = network_source_ip
        if shared_secret is not None:
          self.shared_secret = shared_secret
        if name is not None:
          self.name = name
        if tags is not None:
          self.tags = tags
        if tag_names is not None:
          self.tag_names = tag_names

    @property
    def id(self):
        """
        Gets the id of this Radiusserver.

        :return: The id of this Radiusserver.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Radiusserver.

        :param id: The id of this Radiusserver.
        :type: str
        """

        self._id = id

    @property
    def organization(self):
        """
        Gets the organization of this Radiusserver.

        :return: The organization of this Radiusserver.
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this Radiusserver.

        :param organization: The organization of this Radiusserver.
        :type: str
        """

        self._organization = organization

    @property
    def network_source_ip(self):
        """
        Gets the network_source_ip of this Radiusserver.

        :return: The network_source_ip of this Radiusserver.
        :rtype: str
        """
        return self._network_source_ip

    @network_source_ip.setter
    def network_source_ip(self, network_source_ip):
        """
        Sets the network_source_ip of this Radiusserver.

        :param network_source_ip: The network_source_ip of this Radiusserver.
        :type: str
        """

        self._network_source_ip = network_source_ip

    @property
    def shared_secret(self):
        """
        Gets the shared_secret of this Radiusserver.

        :return: The shared_secret of this Radiusserver.
        :rtype: str
        """
        return self._shared_secret

    @shared_secret.setter
    def shared_secret(self, shared_secret):
        """
        Sets the shared_secret of this Radiusserver.

        :param shared_secret: The shared_secret of this Radiusserver.
        :type: str
        """

        self._shared_secret = shared_secret

    @property
    def name(self):
        """
        Gets the name of this Radiusserver.

        :return: The name of this Radiusserver.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Radiusserver.

        :param name: The name of this Radiusserver.
        :type: str
        """

        self._name = name

    @property
    def tags(self):
        """
        Gets the tags of this Radiusserver.

        :return: The tags of this Radiusserver.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this Radiusserver.

        :param tags: The tags of this Radiusserver.
        :type: list[str]
        """

        self._tags = tags

    @property
    def tag_names(self):
        """
        Gets the tag_names of this Radiusserver.

        :return: The tag_names of this Radiusserver.
        :rtype: list[str]
        """
        return self._tag_names

    @tag_names.setter
    def tag_names(self, tag_names):
        """
        Sets the tag_names of this Radiusserver.

        :param tag_names: The tag_names of this Radiusserver.
        :type: list[str]
        """

        self._tag_names = tag_names

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Radiusserver):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other