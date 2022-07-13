from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Category, Post


class Test_Create_Post(TestCase):

    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(name='django')
        category.save()

        user = User.objects.create(username='test_user', password='123456789')
        user.save()

        post = Post.objects.create(category_id=1, title='Post title', excerpt='Post excerpt',
                                   content='Post content', slug='post-title', author_id=1, status='published')
        post.save()

    def test_blog_content(self):
        post = Post.postobjects.get(id=1)
        category = Category.objects.get(id=1)

        self.assertEqual(str(post), 'Post title')
        self.assertEqual(str(category), 'django')
