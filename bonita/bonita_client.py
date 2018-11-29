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

    def set_variable(self, case_id, v_name, v_type, v_value):
        if not self.sessionid:
            return False

        url = '{0}/{1}/{2}/{3}'.format(
            self.url,
            'API/bpm/caseVariable',
            case_id,
            v_name
        )

        data = {
            'type': v_type,
            'value': v_value
        }

        cookies = {
            'JSESSIONID': self.sessionid,
            'X-Bonita-API-Token': self.token
        }

        res = requests.put(
            url,
            cookies=cookies,
            data=json.dumps(data),
            headers={
                "Content-type": "application/json",
                'JSESSIONID': self.sessionid,
                'X-Bonita-API-Token': self.token
            }
        )

        #bc.set_variable(1031, 'confirma', 'java.lang.Boolean', 'true')

        return res

    def get_human_task(self, case_id):
        if not self.sessionid:
            return False

        url = '{0}/{1}{2}'.format(self.url, 'API/bpm/humanTask?f=caseId=', case_id)

        cookies = {
            'JSESSIONID': self.sessionid,
            'X-Bonita-API-Token': self.token
        }

        res = requests.get(
            url,
            cookies=cookies,
            headers={
                "Content-type": "application/json",
                'JSESSIONID': self.sessionid,
                'X-Bonita-API-Token': self.token
            }
        )

        #  bc.get_human_task(1031)

        return res.json()[0]

    def execute_task(self, task_id):
        if not self.sessionid:
            return False

        url = '{0}/{1}/{2}/{3}'.format(self.url, 'API/bpm/userTask', task_id, 'execution')

        cookies = {
            'JSESSIONID': self.sessionid,
            'X-Bonita-API-Token': self.token
        }

        res = requests.post(
            url,
            cookies=cookies,
            headers={
                "Content-type": "application/json",
                'JSESSIONID': self.sessionid,
                'X-Bonita-API-Token': self.token
            }
        )

        return res

    def assign_task(self, task_id):
        if not self.sessionid:
            return False

        url = '{0}/{1}/{2}'.format(self.url, 'API/bpm/userTask', task_id)

        cookies = {
            'JSESSIONID': self.sessionid,
            'X-Bonita-API-Token': self.token
        }

        data = {
            "assigned_id": 1,
        }

        res = requests.put(
            url,
            cookies=cookies,
            data=json.dumps(data),
            headers={
                "Content-type": "application/json",
                'JSESSIONID': self.sessionid,
                'X-Bonita-API-Token': self.token
            }
        )

        return res

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

        #bc.start_process([{'name': 'id_producto', 'value': 1}, {'name': 'server_url', 'value': 'http://localhost:8006'}, {'name': 'numero_cupon', 'value': 123 }, {'name': 'user_id', 'value': 1 }, {'name': 'is_employee', 'value': 'true' }])

        return res.json()
