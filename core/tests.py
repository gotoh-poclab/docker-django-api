from django.test import TestCase
from core.models import TodoModel

# Create your tests here.

class PostModelTests(TestCase):

    def test_is_empty(self):
        """
        初期状態では何も登録されていないことをテスト
        """
        save_posts=TodoModel.objects.all()
        self.assertEqual(save_posts.count(), 0)

    def test_is_count_one(self):
        """
        1つレコードを適当に作成すると、レコードが1つだけカウントされることをテスト
        """
        post = TodoModel(text='test_text')
        post.save()
        saved_posts = TodoModel.objects.all()
        self.assertEqual(saved_posts.count(), 1)

