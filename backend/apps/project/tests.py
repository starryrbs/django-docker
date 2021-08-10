from test_plus.test import TestCase


class ProjectViewTest(TestCase):
    def test_query_project(self):
        response = self.get("/api/project/")
        self.assert_http_200_ok(response)
