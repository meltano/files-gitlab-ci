from setuptools import setup, find_packages

setup(
    name="files-gitlab-ci",
    version="0.1",
    description="Meltano project files for GitLab CI",
    packages=find_packages(),
    package_data={"bundle": [".gitlab-ci.yml", ".gitlab/ci/docker.gitlab-ci.yml"]},
)
