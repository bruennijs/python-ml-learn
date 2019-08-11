import os
from pprint import pprint

from swagger_client import ActivitiesApi, ApiClient, Configuration, AthletesApi
from swagger_client.rest import ApiException


class StravaApiClient(object):

    def __init__(self) -> None:
        super().__init__()
        self.try_get_access_token()

        configuration = Configuration()
        configuration.access_token = self.try_get_access_token()

        self.client = ApiClient(configuration=configuration)
        self.activitiesApi = ActivitiesApi(api_client=self.client)
        self.athletesApi   = AthletesApi(api_client=self.client)

    def get_Profile(self):
        try:
            # List Athlete Activities
            api_response = self.athletesApi.get_logged_in_athlete()
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling AthletesApi->get_logged_in_athlete: %s\n" % e)

    def loadLoggedInUsersActivities(self):

        before = 56 # Integer | An epoch timestamp to use for filtering activities that have taken place before a certain time. (optional)
        after = 56 # Integer | An epoch timestamp to use for filtering activities that have taken place after a certain time. (optional)
        page = 56 # Integer | Page number. (optional)
        perPage = 56 # Integer | Number of items per page. Defaults to 30. (optional) (default to 30)

        try:
            # List Athlete Activities
            api_response = self.activitiesApi.get_logged_in_athlete_activities()
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ActivitiesApi->getLoggedInAthleteActivities: %s\n" % e)

    def try_get_access_token(self):
        access_token = os.getenv('STRAVA_ACCESS_TOKEN')
        if access_token is None:
            raise Exception('STRAVA_ACCESS_TOKEN environment variable not set')
        return access_token
