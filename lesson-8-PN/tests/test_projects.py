import pytest
import uuid
from pages.projects_page import ProjectsPage


class TestProjects:
    @pytest.fixture
    def projects_page(self):
        return ProjectsPage()

    @pytest.fixture
    def project_data(self):
        return {
            "title": f"Test Project {uuid.uuid4().hex[:8]}",
            "description": "Test project description"
        }

    def test_create_project_positive(self, projects_page, project_data):
        response = projects_page.create_project(project_data)
        assert response.status_code == 201
        response_data = response.json()
        assert "id" in response_data
        assert response_data["title"] == project_data["title"]
        assert response_data["description"] == project_data["description"]
        return response_data["id"]

    def test_get_project_positive(self, projects_page, project_data):
        create_response = projects_page.create_project(project_data)
        project_id = create_response.json()["id"]
        response = projects_page.get_project(project_id)
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["id"] == project_id
        assert response_data["title"] == project_data["title"]

    def test_update_project_positive(self, projects_page, project_data):
        create_response = projects_page.create_project(project_data)
        project_id = create_response.json()["id"]
        update_data = {
            "title": f"Updated {project_data['title']}",
            "description": "Updated description"
        }
        response = projects_page.update_project(project_id, update_data)
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["title"] == update_data["title"]
        expected_desc = update_data["description"]
        assert response_data["description"] == expected_desc

    def test_create_project_negative_missing_title(self, projects_page):
        invalid_data = {
            "description": "Project without title"
        }
        response = projects_page.create_project(invalid_data)
        assert response.status_code == 400

    def test_get_project_negative_invalid_id(self, projects_page):
        invalid_project_id = "invalid-id-12345"
        response = projects_page.get_project(invalid_project_id)
        assert response.status_code == 404

    def test_update_project_negative_invalid_id(self, projects_page):
        invalid_project_id = "invalid-id-12345"
        update_data = {
            "title": "Updated Title",
            "description": "Updated description"
        }
        response = projects_page.update_project(
            invalid_project_id, update_data)
        assert response.status_code == 404

    def test_update_project_negative_empty_data(self, projects_page,
                                                project_data):
        create_response = projects_page.create_project(project_data)
        project_id = create_response.json()["id"]
        empty_data = {}
        response = projects_page.update_project(project_id, empty_data)
        assert response.status_code in [400, 422]
