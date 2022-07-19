from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@email.com",
            password="test123",
        )
        cls.post = Post.objects.create(
            author=cls.user,
            title="A good title",
            description="A description",
            created_at="2022-09-09",
            updated_at="2022-09-09",
        )

    def test_post_model(self):
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.title, "A good title")
        self.assertEqual((self.post.description, "A description"))
        self.assertEqual((self.post.created_at, "2022-09-09"))
        self.assertEqual((self.post.updated_at, "2022-09-09"))

# Not complete