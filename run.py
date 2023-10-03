from api.api_factory import ApiFactory
from report_builder import Report


execucao_geral = True

while execucao_geral:

    usuario = str(input('Digite o nome do usuario: '))

    if usuario == 'sair':
        print('Obrigado por testar o desafio!')
        break

    api_git = ApiFactory(usuario)

    try:
        user_data = api_git.user_info()
        print('Usuario encontrado!')
    except Exception as e:
        print(f'Ocorreu uma exceção: {e}')
        continue

    report = Report(user_data)
    print('Gerando o relatorio do usuario!')
    report.write_report()