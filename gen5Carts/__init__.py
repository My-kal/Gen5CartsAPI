#!/usr/bin/env python

"""__init__.py: Interface for Gen5Carts.com API"""

__author__ = "Dev Mykal"
__version__ = "0.1.0"
__data__ = "31-July-2017"

from requests import get, post, exceptions, codes
from requests.adapters import HTTPAdapter
from json import load

class Gen5(object):
    """
    Initialize Gen5 API object

    :param string api_key: API key can be retrieved at https://gen5carts.com/apiDocs
    """
    def __init__(self, api_key):
        self.api_key = api_key
        self.BASE_URL = 'https://gen5carts.com'

    """
    Upload Cart to Gen5

    :param string site: Adidas US or Adidas UK
    :param string email: Email associated with Adidas account
    :param string password: Password associated with Adidas account
    :param string price: Cart price
    :return string err, string resp
    """
    def upload_cart(self, site, email, password, price):
        payload = {
            'apiKey': self.api_key,
            'site': site,
            'email': email,
            'password': password,
            'price': price
        }

        resp = post('{}/api/uploadCart'.format(self.BASE_URL), data = payload)

        if (resp.status_code == codes.accepted):
            return None, resp.json()['resp']
        else:
            return resp.json()['error'], None

    """
    Retrieve Accounts from Gen5

    :param string site: Adidas US or Adidas UK
    :return string err, list accounts
    """
    def retrieve_accounts(self, site):
        params = {
            'apiKey': self.api_key,
            'site': site
        }

        resp = get('{}/api/accounts'.format(self.BASE_URL), params = params)

        if (resp.status_code == codes.ok):
            return None, resp.json()
        else:
            return resp.json()['error'], None
