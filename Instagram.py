# todo 1 : import instagram api

import pickle
import time
import getpass
import preprocessing as prep
from pprint import pprint


class Worker:
    def __init__(self
                 ):
        # todo 2: write your username:
        self.user_name = ""
        try:
            self.api = self.load_api_pkl()
            assert self.api.isLoggedIn
        except FileNotFoundError or AssertionError:
            self.api = self.login()
            self.save_api_to_pkl()

    def login(self):
        # get password
        pass_word = getpass.getpass('Password:')

        # todo 3 : create an object of InstagramAPI
        api = None

        while True:
            # todo 4: do login

            if api.LastResponse.status_code == 200:
                break
            if api.LastResponse.status_code == 429:
                print("sleep ...")
                time.sleep(60)
            else:
                print(api.LastResponse.status_code)
                break
        return api

    def load_api_pkl(self):
        file_address = "{}.pkl".format(self.user_name)
        with open(file_address, 'rb') as f:
            api = pickle.load(f)
        print('api loaded')
        return api

    def save_api_to_pkl(self):
        file_address = "{}.pkl".format(self.user_name)
        with open(file_address, 'wb') as f:
            pickle.dump(self.api, f, pickle.HIGHEST_PROTOCOL)

    def get_target_lists(self):
        with open("target_accounts.txt", "rb") as f:
            self.user_name_list = [account.decode("utf-8").strip() for account in f.readlines()]
            print(self.user_name_list)
        pass

    def search_user(self,
                    user_name = None):
        refined_user_info = None
        try:
            # todo : search username

            # todo : assert api response is 200

            # todo : get user_info

            # todo : check if to usernames is equal

            # todo: call refine_user_info from preprocessing module

            pass
        except Exception as ex:
            print(ex.__doc__)
        return refined_user_info

    def get_user_feed(self,user_info = None):
        user_posts = None
        try:
            # todo : get_user_feed

            # todo : assert api response is 200

            user_posts = {
                'user_id': None,
                'user_name': None,
                'posts': None # todo : complete the code
            }
        except Exception as ex:
            print(ex.__doc__)
        return user_posts

    def get_user_followers(self,user_info = None):
        user_followers = None
        try:
            # todo : get username followers

            # todo : assert api response is 200

            # todo : complete the code
            user_list = None
            user_followers = {
                'user_id': None,
                'user_name': None,
                'followers': prep.refine_user_list(user_list=user_list)
            }
        except Exception as ex:
            print(ex.__doc__)
        return user_followers

    def get_user_followings(self,user_info = None):
        user_followings = None
        try:
            self.api.getUserFollowings(usernameId=user_info['user_id'])
            assert self.api.LastResponse.status_code == 200
            print('ok')
            user_followings = {
                'user_id': user_info['user_id'],
                'user_name': user_info['user_name'],
                'followings': prep.refine_user_list(user_list=self.api.LastJson['users'])
            }
        except Exception as ex:
                print(ex.__doc__)
        return user_followings

    def analyze_users(self):
        for user_name in self.user_name_list:
            print(user_name)
            #
            # user_info = self.search_user(user_name = user_name)
            # print(user_info)
            # user_posts = self.get_user_feed(user_info = user_info)
            # # print(user_posts)
            # user_info = prep.engagement_calculator(
            #     user_posts = user_posts,
            #     user_info = user_info
            # )
            #
            # print(user_info)
            # user_followers = self.get_user_followers(user_info=user_info)
            # pprint(user_followers)
            # user_followeings = self.get_user_followings(user_info=user_info)
            # pprint(user_followeings)



if __name__ == '__main__':
    worker = Worker()
    worker.get_target_lists()
    worker.analyze_users()

