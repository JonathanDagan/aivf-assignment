from datetime import datetime


class User:
    username: str
    password: str


class Treatment:
    treatment_id: str
    date: str


class Patient:
    patient_id: str
    treatments: list[Treatment]


class Embryo:
    embryo_id: str
    embryo_video: str


class API():
    def __init__(self) -> None:
        self.access_token = ''

    def login(self, user: User) -> dict:
        try:
            access_token = self.call_api(endpoint='login', input=user)[
                "access_token"]
            self.access_token = access_token
            return {'access_token': access_token}
        except Exception as e:
            print('''Error: {}'''.format(e))

    def look_for_patient(self, patient_id: str, access_token: str) -> Patient:
        try:
            return self.__call_api(endpoint='/api/patients', input={'patient_id': patient_id}, access_token=access_token)
        except Exception as e:
            print('''Error: {}'''.format(e))

    def get_treatment_embryos(self, treatment_id: str, access_token: str) -> list[Embryo]:
        try:
            return self.__call_api(endpoint='/api/treatments', input={'treatment_id': treatment_id}, access_token=access_token)
        except Exception as e:
            print('''Error: {}'''.format(e))

    def video_path_from_treatment(self, treatment: Treatment, access_token=None) -> dict:
        if access_token is None:
            access_token = self.access_token

        embryos = self.get_treatment_embryos(
            treatment.treatment_id, access_token=access_token)

        embryo_paths = dict()
        for embryo_id, embryo_video in embryos:
            embryo_paths[embryo_id] = [].append(embryo_video)

        return embryo_paths

    def get_treatments_from_date(self, patient_id: str, date: str, access_token=None) -> list[Treatment]:
        if access_token is None:
            access_token = self.access_token

        treatments = self.look_for_patient(
            access_token=access_token, patient_id=patient_id).treatments

        # TODO: create a better expression which handles dates
        return [treatment for treatment in treatments if treatment.date == date]

    def __call_api(self, endpoint: str, input: dict, access_token: str) -> dict:
        ''' Method was not defined in the API, but is used to call the API '''
        pass


def __main__():
    '''
    Program that fetches all of the video paths of all of the embryos of a patient's treatments from a spesific date.
    '''
    user = User(username="lior", password="liors password")
    patient_id = "12345"
    treatment_date = "2021-01-01"

    api = API()
    api.login(user)

    treatments = api.get_treatments_from_date(
        patient_id=patient_id, date=treatment_date)
    paths = [
        paths for treatment in treatments for paths in api.video_path_from_treatment(treatment)]

    print(paths)
