"""
This plugin searches for JWT keys
"""
from __future__ import absolute_import

import re

from .base import RegexBasedDetector


class JwtKeyDetector(RegexBasedDetector):

    secret_type = 'JSON Web Token'

    denylist = (
        # stripe standard keys begin with sk_live and restricted with rk_live
        #re.compile(r'('ey.+\.[A-Za-z0-9-_=]+\.?[A-Za-z0-9-_.+/=]*$')'),
        re.compile(r'(eyJ[a-zA-Z0-9/+_]+\.[a-zA-Z0-9/+_]+\.[a-zA-Z0-9/+_]+)'),
        #re.compile(r'(?:r|s)k_live_[0-9a-zA-Z]{24}'),
    )
