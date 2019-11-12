import requests

from config.log import LoggingConfiguration
from config.settings import settings


INSP_API_HOST = settings.get("INSP_API_HOST")
INSP_API_AUTH_TOKEN = settings.get("INSP_API_AUTH_TOKEN")
INSP_API_AUTH_USER = settings.get("INSP_API_AUTH_USER")


class InspectionRecordFetcher(object):

    @staticmethod
    def fetch(appointment_id):
        return InspectionRecordFetcher._fetch(appointment_id)

    @staticmethod
    def _fetch(appointment_id):
        logger = LoggingConfiguration.get_default_logger()
        inspection_api_uri = "v2/inspection?action=Search&role=storemanager&client=GS-C2C&appointmentId={" \
                             "appointment_id}&user={user} "
        url = INSP_API_HOST + inspection_api_uri.format(
            appointment_id=appointment_id, user=INSP_API_AUTH_USER)
        headers = {
            "Authorization": "Bearer {}".format(INSP_API_AUTH_TOKEN)
        }
        response = requests.get(url, headers=headers)
        logger.debug("inspection api response: {}".format(response.text))
        if response.status_code == 200:
            return response.json().get('detail', [])
        else:
            logger.error("INSPECTION API FAIL: {}".format(response.text))
            return list()
