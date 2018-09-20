# -*- coding: utf-8 -*-
"""
This module is used for testing the functions within the pyawair.data module.
"""

from unittest import TestCase
from pyuhooair.auth import *
import os
try:
    email = os.environ['email']
    password = os.environ['password']
except:
    from secret import *


class TestCreateuHooAuthObject(TestCase):
    """
    Test Case for pyawair.data get_current_air_data function
    """

    def test_create_uHooAUTH(self):
        """
        """
        auth = UhooAuth(email, password)
        self.assertEqual(auth.email, email)