from .models import Report, Comment
from django.contrib.auth.models import User
from django.test.client import Client
from django.db.models import Q
from django.test import TestCase, RequestFactory


# 日報作成や削除、編集のテスト
class ReportTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.title = 'report'
        cls.user = 'watanabe'
        cls.content_Y = 'content_y'
        cls.content_W = 'content_w'
        cls.content_T = 'content_t'

        print("start create user test")
        cls.user_id = 'Tanaka'
        cls.no_user_id = ""
        cls.mail_address = 'tanaka@example.com'
        cls.password = 'tanakashipassword'
        cls.no_password = ""
        cls.error_password = "error_password"
        client = Client()
        client.post('/register',
                    {'user_id': cls.user_id,
                     'password': cls.password,
                     'mail_address': cls.mail_address})
        Client().login(username=cls.user_id, password=cls.password)

    @classmethod
    def tearDownClass(cls):
        print("Success test")

    # データベースの初期状態の確認(何も入力されていないか確認)
    def test_init_database(self):
        saved_report = Report.objects.all()
        self.assertEquals(saved_report.count(), 0)

    # 日報の各項目の入力、編集、削除をきるか確認
    def test_report_add(self):
        # 各データの入力と呼び出し
        client = Client()
        client.post('/report/add/',
                    {'title': self.title,
                     'user': self.user,
                     'content_Y': self.content_Y,
                     'content_W': self.content_W,
                     'content_T': self.content_T,
                     'report_id': None,
                     'request.user.username': self.user,
                     })

        print(Report.objects.all().count())

        report = Report.objects.get(user=self.user)

        # report = create_report(self, self.title[0], self.content[0], self.user[0], self.time[0])
        #
        # # 各データが一致しているかを確認
        self.assertEquals(report.title, self.title[0])
        self.assertEquals(report.content_Y, self.content[0])
        self.assertEquals(report.user, self.user[0])
        self.assertEquals(report.user_post_time, self.time[0])
        #
        # # 日報の編集
        # report.title = self.title[1]
        # report.content_Y = self.content[1]
        # report.user = self.user[1]
        # report.user_post_time = self.time[1]
        #
        # self.assertEquals(report.title, self.title[1])
        # self.assertEquals(report.content_Y, self.content[1])
        # self.assertEquals(report.user, self.user[1])
        # self.assertEquals(report.user_post_time, self.time[1])
        #
        # # 日報の削除
        # report_id = report.id
        # # print(report_id)
        # report = delete_report(self, report_id)
        #
        # # 各データが削除されているかを確認
        # # self.assertRaises(ValueError, lambda: User.objects.create_user(self.no_user_id, None, self.no_password))
        # self.assertRaises(AttributeError, lambda: report.title)
        # self.assertRaises(AttributeError, lambda: report.content_Y)
        # self.assertRaises(AttributeError, lambda: report.user)
        # self.assertRaises(AttributeError, lambda: report.time)
        # self.assertEquals(report, None)
