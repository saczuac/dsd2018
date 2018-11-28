import json
import requests

from django.conf import settings


class BonitaClient:
    def __init__(self):
        self.url = settings.BONITA_URL
        self.process_id = settings.BONITA_PROCESS_ID
        self.token = ''
        self.sessionid = ''

    def login(self):
        data = {
            'username': settings.BONITA_USERNAME,
            'password': settings.BONITA_PASSWORD,
            'redirect': 'false'
        }

        url = '{0}/{1}'.format(self.url, 'loginservice')

        res = requests.post(
            url,
            data=data,
            headers={
                "Content-Type": "application/x-www-form-urlencoded"
            }
        )

        self.sessionid = res.cookies.get('JSESSIONID')
        self.token = res.cookies.get('X-Bonita-API-Token', '')
        return True

    def start_process(self, variables=[]):
        if not self.sessionid:
            return False

        url = '{0}/{1}'.format(self.url, 'API/bpm/case')

        data = {
            'processDefinitionId': self.process_id,
            'variables': variables
        }

        cookies = {
            'JSESSIONID': self.sessionid,
            'X-Bonita-API-Token': self.token
        }

        res = requests.post(
            url,
            cookies=cookies,
            data=json.dumps(data),
            headers={
                "Content-type": "application/json",
                'JSESSIONID': self.sessionid,
                'X-Bonita-API-Token': self.token
            }
        )

        # bc.start_process([{'name': 'id_producto', 'value': 1}, {'name': 'id_cupon', 'value': 3}])

        return res
