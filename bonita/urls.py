from django.conf.urls import url

from .api import (
    BonitaStartProcessView,
    BonitaConfirmTaskView,
    BonitaGetVariableView
)


bonita_urls = [
    url(
        r'^start$',
        BonitaStartProcessView.as_view(),
        name='bonita-start-process'
    ),

    url(
        r'^confirm$',
        BonitaConfirmTaskView.as_view(),
        name='bonita-confirm-task'
    ),

    url(
        r'^variable$',
        BonitaGetVariableView.as_view(),
        name='bonita-get-variable'
    ),
]
