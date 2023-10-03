from api.api_dealer import ApiDealer
from api.models import UsarioGit


class ApiFactory:

    def __init__(self, username):
        self.__username: str =username


    def __api_git_object(self):
        api_git = ApiDealer(self.__username)
        
        return api_git


    def __get_user_object(self, api_git) -> UsarioGit:
        
        user_dict = api_git.search_user()

        user_object = UsarioGit(login=user_dict['login'],
                                        id=user_dict['id'],
                                        node_id=user_dict['node_id'],
                                        avatar_url=user_dict['avatar_url'],
                                        gravatar_id=user_dict['gravatar_id'],
                                        url=user_dict['url'],
                                        html_url=user_dict['html_url'],
                                        followers_url=user_dict['followers_url'],
                                        following_url=user_dict['following_url'],
                                        gists_url=user_dict['gists_url'],
                                        starred_url=user_dict['starred_url'],
                                        subscriptions_url=user_dict['subscriptions_url'],
                                        organizations_url=user_dict['organizations_url'],
                                        repos_url=user_dict['repos_url'],
                                        events_url=user_dict['events_url'],
                                        received_events_url=user_dict['received_events_url'],
                                        type=user_dict['type'],
                                        site_admin=user_dict['site_admin'],
                                        name=user_dict['name'],
                                        company=user_dict['company'],
                                        blog=user_dict['blog'],
                                        location=user_dict['location'],
                                        email=user_dict['email'],
                                        hireable=user_dict['hireable'],
                                        bio=user_dict['bio'],
                                        twitter_username=user_dict['twitter_username'],
                                        public_repos=user_dict['public_repos'],
                                        public_gists=user_dict['public_gists'],
                                        followers=user_dict['followers'],
                                        following=user_dict['following'],
                                        created_at=user_dict['created_at'],
                                        updated_at=user_dict['updated_at'])
        
        return user_object


    def __get_user_repos_list(self, api_git) -> list: 
        
        repos_list = []

        repos_dict = api_git.search_user_repos()

        for repo in repos_dict:
            repos_list.append(repo["name"])

        return repos_list

    def user_info(self) -> tuple:
        api_git = self.__api_git_object()

        user_object = self.__get_user_object(api_git)

        repo_list = self.__get_user_repos_list(api_git)

        return (user_object, repo_list)
