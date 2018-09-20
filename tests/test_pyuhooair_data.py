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
from pyuhooair.data import *

auth = UhooAuth(email, password)

class TestGetAllDevices(TestCase):
    """
    Test Case for pyawair.data get_current_air_data function
    """

    def test_create_uHooAUTH(self):
        """
        """
        devices = get_all_devices(auth)
        self.assertEqual(type(devices), list)
        keys = devices[0].keys()
        self.assertIn('serialNumber', keys)
        self.assertIn('deviceName', keys)
        self.assertIn('macAddress', keys)
