from .client_proxy import ClientProxy
from .organization import Organization


"""
contentful.organizations_proxy
~~~~~~~~~~~~~~~~~~~~~~~

This module implements the OrganizationsProxy class.

API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/organizations

:copyright: (c) 2017 by Contentful GmbH.
:license: MIT, see LICENSE for more details.
"""


class OrganizationsProxy(ClientProxy):
    """
    API Reference: https://www.contentful.com/developers/docs/references/content-management-api/#/reference/spaces
    """

    def __init__(self, client):
        super(OrganizationsProxy, self).__init__(client, None)

    def __repr__(self):
        return "<OrganizationsProxy>"

    @property
    def _resource_class(self):
        return Organization

    def all(self, query=None, **kwargs):
        """
        Gets all Organizations.
        """

        return super(OrganizationsProxy, self).all(query=query)

    def find(self, organization_id, query=None, **kwargs):
        """Not Supported"""

        raise Exception("Not supported")

    def create(self, attributes=None, **kwargs):
        """Not Supported"""

        raise Exception("Not supported")

    def delete(self, organization_id):
        """Not Supported"""

        raise Exception("Not supported")