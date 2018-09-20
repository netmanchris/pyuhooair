import json, requests


def get_all_devices(auth):
    url = 'https://api.uhooinc.com/v1/getdevicelist'
    data = {'username' : auth.email, 'password' : auth.hexdigest}
    r = requests.post(url, data=data)
    device_list = json.loads(r.text)
    return device_list

def get_current_data(auth, device_name=None, serial=None):
    url = 'https://api.uhooinc.com/v1/getlatestdata'
    if serial is None:
        device_list = get_all_devices(auth)
        for dev in device_list:
            if dev['deviceName'] == device_name:
                serial = dev['serialNumber']
            else:
                return "Device Doesn't Exist"
    else:
        serial = serial
    data = {'username': auth.email, 'password': auth.hexdigest, 'serialNumber': serial}
    r = requests.post(url, data=data)
    current_data = json.loads(r.text)
    return current_data

def get_hourly_data(auth, device_name=None, serial=None):
    url = 'https://api.uhooinc.com/v1/gethourlydata'
    if serial is None:
        device_list = get_all_devices(auth)
        for dev in device_list:
            if dev['deviceName'] == device_name:
                serial = dev['serialNumber']
            else:
                return "Device Doesn't Exist"
    data = {'username': auth.email, 'password': auth.hexdigest, 'serialNumber': serial}
    r = requests.post(url, data=data)
    current_data = json.loads(r.text)
    return current_data

def get_daily_data(auth, device_name=None, serial=None):
    url = 'https://api.uhooinc.com/v1/getdailydata'
    device_list = get_all_devices(auth)
    if serial is None:
        device_list = get_all_devices(auth)
        for dev in device_list:
            if dev['deviceName'] == device_name:
                serial = dev['serialNumber']
            else:
                return "Device Doesn't Exist"
    data = {'username': auth.email, 'password': auth.hexdigest, 'serialNumber': serial}
    r = requests.post(url, data=data)
    current_data = json.loads(r.text)
    return current_data
