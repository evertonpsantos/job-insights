import pytest
from src.pre_built.sorting import sort_by


@pytest.fixture
def read_mock_response():
    return [
        {
            "job_title": "Marketing",
            "company": "Relief",
            "state": "NY",
            "city": "New York",
            "min_salary": 12000,
            "max_salary": 20000,
            "job_desc": "Marketing operations of the company.",
            "industry": "Finance",
            "rating": "4.0",
            "date_posted": "2020-05-08",
            "valid_until": "2020-06-07",
            "job_type": "FULL_TIME",
            "id": "0",
        },
        {
            "job_title": "Registered Nurse",
            "company": "Queens Boulevard Endoscopy Center",
            "state": "NY",
            "city": "Rego Park",
            "min_salary": 8000,
            "max_salary": 12000,
            "job_desc": "Full-Time Registered Nurse!",
            "industry": "",
            "rating": "3.0",
            "date_posted": "2020-04-25",
            "valid_until": "2020-06-07",
            "job_type": "FULL_TIME",
            "id": "1",
        },
        {
            "job_title": "Dental Hygienist",
            "company": "Batista Dental",
            "state": "NJ",
            "city": "West New York",
            "min_salary": 16000,
            "max_salary": 50000,
            "industry": "",
            "rating": "",
            "date_posted": "2020-05-02",
            "valid_until": "2020-06-07",
            "job_type": "PART_TIME",
            "id": "2",
        },
    ]


def test_sort_by_criteria(read_mock_response):
    max_salary_job = {
            "job_title": "Dental Hygienist",
            "company": "Batista Dental",
            "state": "NJ",
            "city": "West New York",
            "min_salary": 16000,
            "max_salary": 50000,
            "industry": "",
            "rating": "",
            "date_posted": "2020-05-02",
            "valid_until": "2020-06-07",
            "job_type": "PART_TIME",
            "id": "2",
        }
    sort_by(read_mock_response, 'max_salary')
    assert read_mock_response[0] == max_salary_job
