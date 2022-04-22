import conf
import json
import requests


def get_access_token():
    response = requests.post(conf.TOKEN_API_URL, data={
        'session_token': conf.SESSION_TOKEN,
        'client_id': conf.CLIENT_ID,
        'grant_type': conf.GRANT_TYPE
    })
    return response.json()


def get_daily_summary(access):
    response = requests.get(conf.SUMMARY_URL, headers={
        'x-moon-os-language': 'en-US',
        'x-moon-app-language': 'en-US',
        'authorization': access['token_type'] + ' ' + access['access_token'],
        'x-moon-app-internal-version': '321',
        'x-moon-app-display-version': '1.17.0',
        'x-moon-app-id': 'com.nintendo.znma',
        'x-moon-os': 'IOS',
        'x-moon-os-version': '15.4.1',
        'x-moon-model': 'iPhone14,5',
        'accept-encoding': 'gzip;q=1.0, compress;q=0.5',
        'accept-language': 'en-US;q=1.0',
        'user-agent': 'moon_ios/1.17.0 (com.nintendo.znma; build:321; iOS 15.4.1) Alamofire/4.7.3',
        'x-moon-timezone': 'Asia/Shanghai',
        'x-moon-smart-device-id': conf.SMART_DEVICE_ID
    })
    return response.json()


def get_monthly_summary(access):
    response = requests.get(conf.MONTHLY_URL, headers={
        'x-moon-os-language': 'en-US',
        'x-moon-app-language': 'en-US',
        'authorization': access['token_type'] + ' ' + access['access_token'],
        'x-moon-app-internal-version': '321',
        'x-moon-app-display-version': '1.17.0',
        'x-moon-app-id': 'com.nintendo.znma',
        'x-moon-os': 'IOS',
        'x-moon-os-version': '15.4.1',
        'x-moon-model': 'iPhone14,5',
        'accept-encoding': 'gzip;q=1.0, compress;q=0.5',
        'accept-language': 'en-US;q=1.0',
        'user-agent': 'moon_ios/1.17.0 (com.nintendo.znma; build:321; iOS 15.4.1) Alamofire/4.7.3',
        'x-moon-timezone': 'Asia/Shanghai',
        'x-moon-smart-device-id': conf.SMART_DEVICE_ID
    })
    count = response.json()['count']
    index = response.json()['indexes']
    data = []
    for i in range(count):
        tmpresponse = requests.get(conf.MONTHLY_URL+'/'+index[i], headers={
            'x-moon-os-language': 'en-US',
            'x-moon-app-language': 'en-US',
            'authorization': access['token_type'] + ' ' + access['access_token'],
            'x-moon-app-internal-version': '321',
            'x-moon-app-display-version': '1.17.0',
            'x-moon-app-id': 'com.nintendo.znma',
            'x-moon-os': 'IOS',
            'x-moon-os-version': '15.4.1',
            'x-moon-model': 'iPhone14,5',
            'accept-encoding': 'gzip;q=1.0, compress;q=0.5',
            'accept-language': 'en-US;q=1.0',
            'user-agent': 'moon_ios/1.17.0 (com.nintendo.znma; build:321; iOS 15.4.1) Alamofire/4.7.3',
            'x-moon-timezone': 'Asia/Shanghai',
            'x-moon-smart-device-id': conf.SMART_DEVICE_ID
        })
        data.append(tmpresponse.json())
        print(f'Fetched monthly data: {index[i]}[{i+1}/{count}]')
    return data


if __name__ == '__main__':
    print('Start fetching...')
    while True:
        try:
            token = get_access_token()
            summary = get_daily_summary(token)
            monthly = get_monthly_summary(token)
            break
        except Exception as e:
            print(e)
            print('Retrying...')

    with open(conf.PATH + '/summary.json', 'w') as f:
        f.write(json.dumps(summary))
    for imonth in monthly:
        with open(f'{conf.PATH}/monthly[{imonth["month"]}].json', 'w') as f:
            f.write(json.dumps(imonth))
