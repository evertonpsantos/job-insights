from src.pre_built.brazilian_jobs import read_brazilian_file
import pytest


@pytest.fixture
def single_job_response():
    return {"salary": "2000", "title": "Maquinista", "type": "trainee"}


def test_brazilian_jobs(single_job_response):
    assert read_brazilian_file(
        "tests/mocks/brazilians_jobs.csv")[0] == single_job_response
