import requests
from pyquery import PyQuery as pq

class Login(object):
    def __init__(self):
        self.headers = {
            'Host': 'github.com',
            'Referer': 'https://github.com/',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.logined_url = 'https://github.com/settings/profile'
        self.session = requests.Session()

    def token(self):
        response = self.session.get(self.login_url, headers=self.headers)
        doc = pq(response.text)
        return doc('form input:nth-child(2)').attr('value')

    def login(self, username, password):
        post_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': self.token(),
            'login': username,
            'password': password,
            'webauthn-support': 'supported'
        }
        response = self.session.post(self.post_url,data=post_data,headers=self.headers)
        if response.status_code == 200:
            self.dynamics(response.text)

        response = self.session.get(self.logined_url, headers=self.headers)
        if response.status_code == 200:
            self.profile(response.text)

    def dynamics(self, html):
        pass

    def profile(self, html):
        doc = pq(html)
        user_name = doc('#user_profile_name').attr('value')
        user_email = doc('#user_profile_email')('option:nth-child(2)').text()
        print(user_name,user_email)

if __name__ == '__main__':
    login = Login()
    login.login(username='Ph0en1x77',password='705jl721')

