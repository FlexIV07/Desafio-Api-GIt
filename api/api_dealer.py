import requests


class ApiDealer:

    def __init__(self, username):
        self.__username: str = username
        self.__api_end_point: str = "https://api.github.com/users/"

    def search_user(self) -> dict:

        user_end_point = self.__api_end_point+self.__username

        try:
            get = requests.get(user_end_point)
        except:
            return ConnectionError('Requisicao Nao Efetuada')

        if 'Not Found' in get.text:
            raise ValueError('Usuario nao localizado')
        else:
            return get.json()

        

    def search_user_repos(self) -> dict:

        repos_endpoint = self.__api_end_point+self.__username+'/repos'
        
        try:
            get = requests.get(repos_endpoint)
        except:
            return ConnectionError('Requisicao Nao Efetuada')   

        if 'Not Found' in get.text:
            raise ValueError('Usuario nao localizado')
        else:
            return get.json()

