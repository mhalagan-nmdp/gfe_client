# coding: utf-8

"""
    Allele Calling Service

    The Allele Calling  service provides an API for converting raw sequence data to GFE and HLA allele calls.  # noqa: E501

    OpenAPI spec version: 0.0.5
    Contact: mhalagan@nmdp.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from gfe_client.models.feature import Feature  # noqa: F401,E501
from gfe_client.models.seqdiff import Seqdiff  # noqa: F401,E501


class Typing(object):
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
        'seqdiff': 'list[Seqdiff]',
        'protdiff': 'list[Seqdiff]',
        'features': 'list[Feature]',
        'novel_features': 'list[Feature]',
        'gfe': 'str',
        'hla': 'str',
        'closest_gfe': 'str',
        'full_gene_accession': 'int',
        'differences': 'int',
        'status': 'str',
        'pygfe_version': 'str',
        'gfedb_version': 'str',
        'imgtdb_version': 'str',
        'seqann_version': 'str'
    }

    attribute_map = {
        'seqdiff': 'seqdiff',
        'protdiff': 'protdiff',
        'features': 'features',
        'novel_features': 'novel_features',
        'gfe': 'gfe',
        'hla': 'hla',
        'closest_gfe': 'closest_gfe',
        'full_gene_accession': 'full_gene_accession',
        'differences': 'differences',
        'status': 'status',
        'pygfe_version': 'pygfe_version',
        'gfedb_version': 'gfedb_version',
        'imgtdb_version': 'imgtdb_version',
        'seqann_version': 'seqann_version'
    }

    def __init__(self, seqdiff=None, protdiff=None, features=None, novel_features=None, gfe=None, hla=None, closest_gfe=None, full_gene_accession=None, differences=None, status=None, pygfe_version=None, gfedb_version=None, imgtdb_version=None, seqann_version=None):  # noqa: E501
        """Typing - a model defined in Swagger"""  # noqa: E501

        self._seqdiff = None
        self._protdiff = None
        self._features = None
        self._novel_features = None
        self._gfe = None
        self._hla = None
        self._closest_gfe = None
        self._full_gene_accession = None
        self._differences = None
        self._status = None
        self._pygfe_version = None
        self._gfedb_version = None
        self._imgtdb_version = None
        self._seqann_version = None
        self.discriminator = None

        if seqdiff is not None:
            self.seqdiff = seqdiff
        if protdiff is not None:
            self.protdiff = protdiff
        if features is not None:
            self.features = features
        if novel_features is not None:
            self.novel_features = novel_features
        if gfe is not None:
            self.gfe = gfe
        if hla is not None:
            self.hla = hla
        if closest_gfe is not None:
            self.closest_gfe = closest_gfe
        if full_gene_accession is not None:
            self.full_gene_accession = full_gene_accession
        if differences is not None:
            self.differences = differences
        if status is not None:
            self.status = status
        if pygfe_version is not None:
            self.pygfe_version = pygfe_version
        if gfedb_version is not None:
            self.gfedb_version = gfedb_version
        if imgtdb_version is not None:
            self.imgtdb_version = imgtdb_version
        if seqann_version is not None:
            self.seqann_version = seqann_version

    @property
    def seqdiff(self):
        """Gets the seqdiff of this Typing.  # noqa: E501


        :return: The seqdiff of this Typing.  # noqa: E501
        :rtype: list[Seqdiff]
        """
        return self._seqdiff

    @seqdiff.setter
    def seqdiff(self, seqdiff):
        """Sets the seqdiff of this Typing.


        :param seqdiff: The seqdiff of this Typing.  # noqa: E501
        :type: list[Seqdiff]
        """

        self._seqdiff = seqdiff

    @property
    def protdiff(self):
        """Gets the protdiff of this Typing.  # noqa: E501


        :return: The protdiff of this Typing.  # noqa: E501
        :rtype: list[Seqdiff]
        """
        return self._protdiff

    @protdiff.setter
    def protdiff(self, protdiff):
        """Sets the protdiff of this Typing.


        :param protdiff: The protdiff of this Typing.  # noqa: E501
        :type: list[Seqdiff]
        """

        self._protdiff = protdiff

    @property
    def features(self):
        """Gets the features of this Typing.  # noqa: E501


        :return: The features of this Typing.  # noqa: E501
        :rtype: list[Feature]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this Typing.


        :param features: The features of this Typing.  # noqa: E501
        :type: list[Feature]
        """

        self._features = features

    @property
    def novel_features(self):
        """Gets the novel_features of this Typing.  # noqa: E501


        :return: The novel_features of this Typing.  # noqa: E501
        :rtype: list[Feature]
        """
        return self._novel_features

    @novel_features.setter
    def novel_features(self, novel_features):
        """Sets the novel_features of this Typing.


        :param novel_features: The novel_features of this Typing.  # noqa: E501
        :type: list[Feature]
        """

        self._novel_features = novel_features

    @property
    def gfe(self):
        """Gets the gfe of this Typing.  # noqa: E501


        :return: The gfe of this Typing.  # noqa: E501
        :rtype: str
        """
        return self._gfe

    @gfe.setter
    def gfe(self, gfe):
        """Sets the gfe of this Typing.


        :param gfe: The gfe of this Typing.  # noqa: E501
        :type: str
        """

        self._gfe = gfe

    @property
    def hla(self):
        """Gets the hla of this Typing.  # noqa: E501


        :return: The hla of this Typing.  # noqa: E501
        :rtype: str
        """
        return self._hla

    @hla.setter
    def hla(self, hla):
        """Sets the hla of this Typing.


        :param hla: The hla of this Typing.  # noqa: E501
        :type: str
        """

        self._hla = hla

    @property
    def closest_gfe(self):
        """Gets the closest_gfe of this Typing.  # noqa: E501


        :return: The closest_gfe of this Typing.  # noqa: E501
        :rtype: str
        """
        return self._closest_gfe

    @closest_gfe.setter
    def closest_gfe(self, closest_gfe):
        """Sets the closest_gfe of this Typing.


        :param closest_gfe: The closest_gfe of this Typing.  # noqa: E501
        :type: str
        """

        self._closest_gfe = closest_gfe

    @property
    def full_gene_accession(self):
        """Gets the full_gene_accession of this Typing.  # noqa: E501


        :return: The full_gene_accession of this Typing.  # noqa: E501
        :rtype: int
        """
        return self._full_gene_accession

    @full_gene_accession.setter
    def full_gene_accession(self, full_gene_accession):
        """Sets the full_gene_accession of this Typing.


        :param full_gene_accession: The full_gene_accession of this Typing.  # noqa: E501
        :type: int
        """

        self._full_gene_accession = full_gene_accession

    @property
    def differences(self):
        """Gets the differences of this Typing.  # noqa: E501


        :return: The differences of this Typing.  # noqa: E501
        :rtype: int
        """
        return self._differences

    @differences.setter
    def differences(self, differences):
        """Sets the differences of this Typing.


        :param differences: The differences of this Typing.  # noqa: E501
        :type: int
        """

        self._differences = differences

    @property
    def status(self):
        """Gets the status of this Typing.  # noqa: E501


        :return: The status of this Typing.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Typing.


        :param status: The status of this Typing.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def pygfe_version(self):
        """Gets the pygfe_version of this Typing.  # noqa: E501


        :return: The pygfe_version of this Typing.  # noqa: E501
        :rtype: str
        """
        return self._pygfe_version

    @pygfe_version.setter
    def pygfe_version(self, pygfe_version):
        """Sets the pygfe_version of this Typing.


        :param pygfe_version: The pygfe_version of this Typing.  # noqa: E501
        :type: str
        """

        self._pygfe_version = pygfe_version

    @property
    def gfedb_version(self):
        """Gets the gfedb_version of this Typing.  # noqa: E501


        :return: The gfedb_version of this Typing.  # noqa: E501
        :rtype: str
        """
        return self._gfedb_version

    @gfedb_version.setter
    def gfedb_version(self, gfedb_version):
        """Sets the gfedb_version of this Typing.


        :param gfedb_version: The gfedb_version of this Typing.  # noqa: E501
        :type: str
        """

        self._gfedb_version = gfedb_version

    @property
    def imgtdb_version(self):
        """Gets the imgtdb_version of this Typing.  # noqa: E501


        :return: The imgtdb_version of this Typing.  # noqa: E501
        :rtype: str
        """
        return self._imgtdb_version

    @imgtdb_version.setter
    def imgtdb_version(self, imgtdb_version):
        """Sets the imgtdb_version of this Typing.


        :param imgtdb_version: The imgtdb_version of this Typing.  # noqa: E501
        :type: str
        """

        self._imgtdb_version = imgtdb_version

    @property
    def seqann_version(self):
        """Gets the seqann_version of this Typing.  # noqa: E501


        :return: The seqann_version of this Typing.  # noqa: E501
        :rtype: str
        """
        return self._seqann_version

    @seqann_version.setter
    def seqann_version(self, seqann_version):
        """Sets the seqann_version of this Typing.


        :param seqann_version: The seqann_version of this Typing.  # noqa: E501
        :type: str
        """

        self._seqann_version = seqann_version

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
        if not isinstance(other, Typing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
