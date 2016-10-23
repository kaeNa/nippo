# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.test.client import Client
from django.db.models import Q
from django.test import TestCase, RequestFactory
from .models import Report, Comment
from .user_config import create_user


#  ユーザの作成とログイン関係のテスト
class CreateUserTest(TestCase):
    @classmethod
    def setUpClass(cls):
        print("start create user test")
        cls.user_id = ['Sato', 'Suzuki']
        cls.no_user_id = ""
        cls.mail_address = ['sato@example.com', 'suzuki@example.com']
        cls.password = ['satopassword', 'suzukipassword']
        cls.no_password = ""
        cls.error_password = "error_password"
        cls.error_message = ['パスワードは8文字以上で設定してください',
                             'User IDが空白です。User IDを入力してください。',
                             'すでに存在しているUser IDです。別のUser IDに変更してください。']

    @classmethod
    def tearDownClass(cls):
        print("Success create user test")

    def test_create_user(self):
        # ユーザの作成と呼び出し
        client = Client()
        response = client.post('/register',
                              {'user_id': self.user_id[0],
                               'password': self.password[0],
                               'mail_address': self.mail_address[0]})
        check_user = User.objects.get(username=self.user_id[0])

        # 作成したユーザのIDとパスワードが一致しているか確認
        self.assertEquals(check_user.username, self.user_id[0])
        self.assertTrue(check_user.check_password(self.password[0]))
        self.assertEquals(check_user.email, self.mail_address[0])

        self.assertEqual(response.status_code, 302)

    def test_no_create_user_less_password(self):
        # ユーザが作成できないことを確認
        # パスワードが8以下の時
        client = Client()
        response = client.post('/register',
                               {'user_id': self.user_id[0],
                                'password': self.no_password,
                                'mail_address': self.mail_address[0]})

        self.assertEquals(response.context['error_message'],
                          self.error_message[0])
        self.assertEqual(response.status_code, 200)

    def test_no_create_user_no_username(self):
        # ユーザが作成できないことを確認
        # ユーザIDが未入力の時
        client = Client()
        response = client.post('/register',
                               {'user_id': self.no_user_id,
                                'password': self.password[0],
                                'mail_address': self.mail_address[0]})

        self.assertEquals(response.context['error_message'],
                          self.error_message[1])
        self.assertEqual(response.status_code, 200)

    def test_no_create_user_exist(self):
        # ユーザが作成できないことを確認
        # すでに存在するユーザIDを入力したとき

        client = Client()
        client.post('/register',
                    {'user_id': self.user_id[1],
                     'password': self.password[1],
                     'mail_address': self.mail_address[1]})

        response = client.post('/register',
                               {'user_id': self.user_id[1],
                                'password': self.password[1],
                                'mail_address': self.mail_address[1]})

        self.assertEquals(response.context['error_message'],
                          self.error_message[2])
        self.assertEqual(response.status_code, 200)


#  ユーザの作成とログイン関係のテスト
class UserLoginTest(TestCase):
    @classmethod
    def setUpClass(cls):
        print("start create user test")
        cls.user_id = 'Takahashi'
        cls.no_user_id = ""
        cls.mail_address = 'takahashi@example.com'
        cls.password = 'takahashipassword'
        cls.no_password = ""
        cls.error_password = "error_password"
        client = Client()
        client.post('/register',
                      {'user_id': cls.user_id,
                       'password': cls.password,
                       'mail_address': cls.mail_address})

    @classmethod
    def tearDownClass(cls):
        print("Success user login test")


    # 作成したユーザがログインできるかどうか
    def test_login(self):
        # 作成したユーザでログインできるかを確認
        client = Client()
        # response = client.post('/login',
        #                        {'username': self.user_id,
        #                         'password': self.password})
        # print(response.status_code)
        # self.assertEqual(response.status_code, 302)
        self.assertTrue(client.login(username=self.user_id, password=self.password))

    # 異なるID、パスワードでログインできないかどうか

    def test_not_login(self):
        # ユーザを作成
        # create_user(self, self.user_id, self.password)

        # 作成したユーザに異なるパスワードでログインできないかを確認
        client_user = Client()
        self.assertFalse(client_user.login(username=self.user_id, password=self.error_password))
