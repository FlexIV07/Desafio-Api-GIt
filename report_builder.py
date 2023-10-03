
class Report:

    def __init__(self, user_info):
        self.__user_info: tuple = user_info
    
    def write_report(self):
        user_data = self.__user_info[0]
        repo_data = self.__user_info[1]
        with open(f"{user_data.name}.txt", 'w') as report:
            report.write(f'Nome: {user_data.name}\nPerfil: {user_data.html_url}\nNúmero de repositórios publicos: {user_data.public_repos}\nNúmero de seguidores: {user_data.followers}\nNúmero de usuários seguidos: {user_data.following}\nLista de Repositórios: {repo_data}')
