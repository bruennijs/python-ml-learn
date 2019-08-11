import os
from pprint import pprint

from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
from swagger_client.rest import ApiException


class StravaApiClient(object):

    def __init__(self) -> None:
        super().__init__()
        if os.getenv('STRAVA_ACCESS_TOKEN') is None:
            raise Exception('STRAVA_ACCESS_TOKEN environment variable not set')

        # self.configuration = Configuration(apikey="MYAPIKEY")
        self.apiClient = ApiClient()


    def loadLoggedInUsersActivities(self):
        # before = 56 # Integer | An epoch timestamp to use for filtering activities that have taken place before a certain time. (optional)
        # after = 56 # Integer | An epoch timestamp to use for filtering activities that have taken place after a certain time. (optional)
        # page = 56 # Integer | Page number. (optional)
        # perPage = 56 # Integer | Number of items per page. Defaults to 30. (optional) (default to 30)

        try:
            # List Athlete Activities
            api_response = self.apiClient.getLoggedInAthleteActivities()
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ActivitiesApi->getLoggedInAthleteActivities: %s\n" % e)
