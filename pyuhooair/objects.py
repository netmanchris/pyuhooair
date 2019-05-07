
#!/usr/bin/env python3
# coding=utf-8
# author: @netmanchris
# -*- coding: utf-8 -*-

from pyuhooair.auth import *
from pyuhooair.data import get_current_data, get_all_devices
import datetime


class UhooDev:
    def __init__(self, device_name: str, auth: UhooAuth, cache_time: float = 15):
        """
        Initialise AwairDev object.

        :param device_name: The name of the device a can be found in the Awair app. Careful, case sensitive.
        :param auth: The authentication object as created by the UhooAuth function.
        :param cache_time: The time in minutes that the state values should be cached. When this time has expired, new values
                           will be requested. Keep in mind that the API has daily limits so setting this too low might
                           cause problems.
        """
        self._auth = auth
        self._cache_time = cache_time
        self._last_update = datetime.datetime.now()  # records the last update

        self._device_name = device_name

        # Get device type and ID from name
        devices = get_all_devices(self._auth)
        self._serial = next((item for item in devices if item["deviceName"] == device_name),
                          False)['serialNumber']  # get the device type
        # Initiate data fields
        self._data = {}
        self._last_update = None
        self.refresh()

    def get_state(self, indicator: str) -> float:
        """
        Function to get the state of a specific indicator.

        The values are cached, in accordance with the cache time that is set for the object.

        :param indicator: A string containing one of the values from: score, temp, humid, co2, voc or dust.
        :return: The value of the specific indicator.
        """
        now = datetime.datetime.now()
        delta_min = (now - self._last_update).total_seconds() / 60
        if delta_min > self._cache_time:
            self.refresh()
        return(self._data[indicator])

    def refresh(self):
        """
        Function to refresh the state of the objects.

        The values are cached internally for the period equal to the cache
        time value. The refresh function refreshed these values, independent of the time that has past since the last
        refresh.
        """
        current_data = get_current_data(self._auth, serial=self._serial)
        self._data['CO'] = current_data['CO']
        self._data['air_pressure'] = current_data['Air Pressure']
        self._data['humidity'] = current_data['Relative Humidity']
        self._data['co2'] = current_data['CO2']
        self._data['voc'] = current_data['TVOC']
        self._data['dust'] = current_data['PM2.5']
        self._data['timestamp'] = current_data['Timestamp']
        self._data['ozone'] = current_data['Ozone']
        self._data['NO2'] = current_data['NO2']
        self._data['DateTime'] = current_data['DateTime']
        self._data['Temperature'] = current_data['Temperature']
        self._last_update = datetime.datetime.now()  # records the time of the last update


