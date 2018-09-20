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

    def test_GetAllDevices(self):
        """
        """
        devices = get_all_devices(auth)
        self.assertEqual(type(devices), list)
        keys = devices[0].keys()
        self.assertIn('serialNumber', keys)
        self.assertIn('deviceName', keys)
        self.assertIn('macAddress', keys)


class TestCurrentData(TestCase):
    """
    Test Case for pyawair.data get_current_air_data function
    """

    def test_GetCurrentData_id_pos(self):
        """
        """
        devices = get_all_devices(auth)
        dev1 = devices[0]
        current_data = get_current_data(auth, serial=dev1['serialNumber'])
        self.assertEqual(type(current_data), dict)
        keys = current_data.keys()
        self.assertIn('Ozone', keys)
        self.assertIn('Timestamp', keys)
        self.assertIn('TVOC', keys)
        self.assertIn('CO2', keys)
        self.assertIn('Air Pressure', keys)
        self.assertIn('Relative Humidity', keys)
        self.assertIn('NO2', keys)
        self.assertIn('PM2.5', keys)
        self.assertIn('Temperature', keys)
        self.assertIn('DateTime', keys)

    def test_GetCurrentData_id_neg(self):
        """
        """
        devices = get_all_devices(auth)
        dev1 = devices[0]
        current_data = get_current_data(auth, serial='Doesnt Exist')
        self.assertEqual(current_data,  {'message': 'Incorrect serialNumber', 'status': 2})

    def test_GetCurrentData_name_pos(self):
        """
        """
        devices = get_all_devices(auth)
        dev1 = devices[0]
        current_data = get_current_data(auth, device_name=dev1['deviceName'])
        self.assertEqual(type(current_data), dict)
        keys = current_data.keys()
        self.assertIn('Ozone', keys)
        self.assertIn('Timestamp', keys)
        self.assertIn('TVOC', keys)
        self.assertIn('CO2', keys)
        self.assertIn('Air Pressure', keys)
        self.assertIn('Relative Humidity', keys)
        self.assertIn('NO2', keys)
        self.assertIn('PM2.5', keys)
        self.assertIn('Temperature', keys)
        self.assertIn('DateTime', keys)

    def test_GetCurrentData_name_neg(self):
        """
        """
        devices = get_all_devices(auth)
        dev1 = devices[0]
        current_data = get_current_data(auth, device_name='Doesnt Exist')
        self.assertEqual(current_data, "Device Doesn't Exist")




class TestHourlyData(TestCase):
    """
    Test Case for pyawair.data get_hourly_air_data function
    """

    def test_GetHourlyData_id_pos(self):
        """
        """
        devices = get_all_devices(auth)
        dev1 = devices[0]
        hourly_data = get_hourly_data(auth, serial=dev1['serialNumber'])
        print (hourly_data)
        self.assertEqual(type(hourly_data), list)
        keys = hourly_data[0].keys()
        self.assertIn('Ozone', keys)
        self.assertIn('Timestamp', keys)
        self.assertIn('TVOC', keys)
        self.assertIn('CO2', keys)
        self.assertIn('Air Pressure', keys)
        self.assertIn('Relative Humidity', keys)
        self.assertIn('NO2', keys)
        self.assertIn('PM2.5', keys)
        self.assertIn('Temperature', keys)
        self.assertIn('DateTime', keys)


    def test_GetHourlyData_id_neg(self):
        """
        """
        hourly_data = get_hourly_data(auth, serial='Doesnt Exist')
        self.assertEqual(hourly_data,  {'message': 'Incorrect serialNumber', 'status': 2})

    def test_GetHourlyData_name_pos(self):
        """
        """
        devices = get_all_devices(auth)
        dev1 = devices[0]
        hourly_data = get_hourly_data(auth, device_name=dev1['deviceName'])
        self.assertEqual(type(hourly_data), list)
        keys = hourly_data[0].keys()
        self.assertIn('Ozone', keys)
        self.assertIn('Timestamp', keys)
        self.assertIn('TVOC', keys)
        self.assertIn('CO2', keys)
        self.assertIn('Air Pressure', keys)
        self.assertIn('Relative Humidity', keys)
        self.assertIn('NO2', keys)
        self.assertIn('PM2.5', keys)
        self.assertIn('Temperature', keys)
        self.assertIn('DateTime', keys)

    def test_GetHourlyData_name_neg(self):
        """
        """
        hourly_data = get_hourly_data(auth, device_name='Doesnt Exist')
        self.assertEqual(hourly_data, "Device Doesn't Exist")


#get_daily_data

class TestDailyData(TestCase):
    """
    Test Case for pyawair.data get_daily_air_data function
    """

    def test_GetDailyData_id_pos(self):
        """
        """
        devices = get_all_devices(auth)
        dev1 = devices[0]
        daily_data = get_daily_data(auth, serial=dev1['serialNumber'])
        print(daily_data)
        self.assertEqual(type(daily_data), list)
        keys = daily_data[0].keys()
        self.assertIn('Ozone', keys)
        self.assertIn('Timestamp', keys)
        self.assertIn('TVOC', keys)
        self.assertIn('CO2', keys)
        self.assertIn('Air Pressure', keys)
        self.assertIn('Relative Humidity', keys)
        self.assertIn('NO2', keys)
        self.assertIn('PM2.5', keys)
        self.assertIn('Temperature', keys)
        self.assertIn('DateTime', keys)


    def test_GetDailyData_id_neg(self):
        """
        """
        daily_data = get_daily_data(auth, serial='Doesnt Exist')
        self.assertEqual(daily_data, {'message': 'Incorrect serialNumber', 'status': 2})

    def test_GetDailyData_name_pos(self):
        """
        """
        devices = get_all_devices(auth)
        dev1 = devices[0]
        daily_data = get_daily_data(auth, device_name=dev1['deviceName'])
        self.assertEqual(type(daily_data), list)
        keys = daily_data[0].keys()
        self.assertIn('Ozone', keys)
        self.assertIn('Timestamp', keys)
        self.assertIn('TVOC', keys)
        self.assertIn('CO2', keys)
        self.assertIn('Air Pressure', keys)
        self.assertIn('Relative Humidity', keys)
        self.assertIn('NO2', keys)
        self.assertIn('PM2.5', keys)
        self.assertIn('Temperature', keys)
        self.assertIn('DateTime', keys)

    def test_GetDailyData_name_neg(self):
        """
        """
        daily_data = get_daily_data(auth, device_name='Doesnt Exist')
        self.assertEqual(daily_data, "Device Doesn't Exist")