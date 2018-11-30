# -*- coding: utf-8 -*-
import logging

from rest_framework.views import APIView

from rest_framework import permissions

from rest_framework import status
from rest_framework.response import Response

from employees.models import Employee

from .bonita_client import BonitaClient

from django.conf import settings


class BonitaStartProcessView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        product_id = self.request.data.get('product_id')
        coupon_number = self.request.data.get('coupon_number')
        user_id = self.request.user.id
        is_employee_q = Employee.objects.filter(user=request.user)
        is_employee = 'true' if is_employee_q else 'false'
        server_url = settings.SITE_URL

        try:
            if product_id and user_id:
                bc = BonitaClient()

                # Login first
                logged_in = bc.login()

                if logged_in:
                    if coupon_number:
                        bonita_process = bc.start_process([
                            {'name': 'id_producto', 'value': product_id},
                            {'name': 'server_url', 'value': server_url},
                            {'name': 'numero_cupon', 'value': coupon_number},
                            {'name': 'user_id', 'value': user_id},
                            {'name': 'is_employee', 'value': is_employee}
                        ])
                    else:
                        bonita_process = bc.start_process([
                            {'name': 'id_producto', 'value': product_id},
                            {'name': 'server_url', 'value': server_url},
                            {'name': 'user_id', 'value': user_id},
                            {'name': 'is_employee', 'value': is_employee}
                        ])

                    case_id = bonita_process.get('rootCaseId')

                    return Response({'case_id': case_id})

                return Response(
                    {'errors': 'Can not log in to bonita'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            return Response(
                {'errors': 'Missing paramenter product_id'},
                status=status.HTTP_400_BAD_REQUEST
            )

        except Exception as e:
            logging.error(str(e))

            return Response(
                {'errors': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


class BonitaConfirmTaskView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        confirm = self.request.data.get('confirm')
        case_id = self.request.data.get('case_id')

        try:
            if confirm and case_id:
                bc = BonitaClient()

                # Login first
                logged_in = bc.login()

                if logged_in:
                    # Get HumanTask id
                    human_task = bc.get_human_task(case_id)
                    human_task_id = human_task.get('id')

                    # Assign it
                    task_assigned = bc.assign_task(human_task_id)

                    if task_assigned.status_code == 200:
                        # Set Confirma
                        variable_setted = bc.set_variable(
                            case_id,
                            'confirma',
                            'java.lang.Boolean',
                            confirm
                        )

                        if variable_setted.status_code == 200:
                            # Execute task
                            executed = bc.execute_task(human_task_id)

                            if executed.status_code == 204:
                                return Response({'ok': True})

                            msg = 'Task execution failed: {0}'.format(
                                human_task_id
                            )

                            return Response(
                                {'errors': msg},
                                status=status.HTTP_400_BAD_REQUEST
                            )

                        msg = 'Can not set variable {0} on bonita'.format(
                            confirm
                        )

                        return Response(
                            {'errors': msg},
                            status=status.HTTP_400_BAD_REQUEST
                        )

                    msg = 'Can not assign human task {0} on bonita'.format(
                        human_task_id
                    )

                    return Response(
                        {'errors': msg},
                        status=status.HTTP_400_BAD_REQUEST
                    )

                return Response(
                    {'errors': 'Can not log in to bonita'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            return Response(
                {'errors': 'Missing paramenter/s confirm or case_id'},
                status=status.HTTP_400_BAD_REQUEST
            )

        except Exception as e:
            logging.error(str(e))

            return Response(
                {'errors': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


class BonitaGetVariableView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        v_name = self.request.GET.get('v_name')
        case_id = self.request.GET.get('case_id')

        try:
            if case_id and v_name:
                bc = BonitaClient()

                # Login first
                logged_in = bc.login()

                if logged_in:
                    value = bc.get_variable(case_id, v_name)
                    return Response({v_name: value})

                return Response(
                    {'errors': 'Can not log in to bonita'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            return Response(
                {'errors': 'Missing paramenter v_name or case_id'},
                status=status.HTTP_400_BAD_REQUEST
            )

        except Exception as e:
            logging.error(str(e))

            return Response(
                {'errors': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
