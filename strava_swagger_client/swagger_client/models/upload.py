# coding: utf-8

"""
    Strava API v3

    Strava API  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Upload(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'id': 'int',
        'id_str': 'str',
        'external_id': 'str',
        'error': 'str',
        'status': 'str',
        'activity_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'id_str': 'id_str',
        'external_id': 'external_id',
        'error': 'error',
        'status': 'status',
        'activity_id': 'activity_id'
    }

    def __init__(self, id=None, id_str=None, external_id=None, error=None, status=None, activity_id=None):  # noqa: E501
        """Upload - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._id_str = None
        self._external_id = None
        self._error = None
        self._status = None
        self._activity_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if id_str is not None:
            self.id_str = id_str
        if external_id is not None:
            self.external_id = external_id
        if error is not None:
            self.error = error
        if status is not None:
            self.status = status
        if activity_id is not None:
            self.activity_id = activity_id

    @property
    def id(self):
        """Gets the id of this Upload.  # noqa: E501

        The unique identifier of the upload  # noqa: E501

        :return: The id of this Upload.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Upload.

        The unique identifier of the upload  # noqa: E501

        :param id: The id of this Upload.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def id_str(self):
        """Gets the id_str of this Upload.  # noqa: E501

        The unique identifier of the upload in string format  # noqa: E501

        :return: The id_str of this Upload.  # noqa: E501
        :rtype: str
        """
        return self._id_str

    @id_str.setter
    def id_str(self, id_str):
        """Sets the id_str of this Upload.

        The unique identifier of the upload in string format  # noqa: E501

        :param id_str: The id_str of this Upload.  # noqa: E501
        :type: str
        """

        self._id_str = id_str

    @property
    def external_id(self):
        """Gets the external_id of this Upload.  # noqa: E501

        The external identifier of the upload  # noqa: E501

        :return: The external_id of this Upload.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this Upload.

        The external identifier of the upload  # noqa: E501

        :param external_id: The external_id of this Upload.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def error(self):
        """Gets the error of this Upload.  # noqa: E501

        The error associated with this upload  # noqa: E501

        :return: The error of this Upload.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this Upload.

        The error associated with this upload  # noqa: E501

        :param error: The error of this Upload.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def status(self):
        """Gets the status of this Upload.  # noqa: E501

        The status of this upload  # noqa: E501

        :return: The status of this Upload.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Upload.

        The status of this upload  # noqa: E501

        :param status: The status of this Upload.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def activity_id(self):
        """Gets the activity_id of this Upload.  # noqa: E501

        The identifier of the activity this upload resulted into  # noqa: E501

        :return: The activity_id of this Upload.  # noqa: E501
        :rtype: int
        """
        return self._activity_id

    @activity_id.setter
    def activity_id(self, activity_id):
        """Sets the activity_id of this Upload.

        The identifier of the activity this upload resulted into  # noqa: E501

        :param activity_id: The activity_id of this Upload.  # noqa: E501
        :type: int
        """

        self._activity_id = activity_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Upload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other