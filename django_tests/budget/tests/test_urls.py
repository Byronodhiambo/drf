from audioop import reverse
from django.test import TestCase
from django.urls import reverse, resolve
from ..urls import *
from ..views import project_list, ProjectCreateView, project_detail


class Test_Urls(TestCase):

    def test_list_url_is_resolved(self):
        url = reverse('list')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, project_list)

    def test_add_url_is_resolved(self):
        url = reverse('add')
        self.assertEquals(resolve(url).func.view_class, ProjectCreateView)

    def test_details_url_is_resolved(self):
        url = reverse('detail', args=['sometthing'])#pass somearguments if the url needs the urguments
        self.assertEquals(resolve(url).func, project_detail)