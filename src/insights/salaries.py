from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    data = read(path)
    salaries = [
        int(job["max_salary"])
        for job in data
        if job["max_salary"] != "" and job["max_salary"] != "invalid"
    ]
    return max(salaries)


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    data = read(path)
    salaries = [
        int(job["min_salary"])
        for job in data
        if job["min_salary"] != "" and job["min_salary"] != "invalid"
    ]
    return min(salaries)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """

    try:
        if int(job["min_salary"]) > int(job["max_salary"]):
            raise ValueError("Min salary can't be greater than max salary")

        return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])
    except TypeError:
        raise ValueError("Values passed must be valid integers")
    except KeyError:
        raise ValueError("Max salary and min salary are required")


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    filtered_jobs = []

    for curr_job in jobs:

        try:
            if matches_salary_range(curr_job, salary):
                filtered_jobs.append(curr_job)

        except ValueError:
            ...

    return filtered_jobs
