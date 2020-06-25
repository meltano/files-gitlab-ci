# files-gitlab-ci

Meltano project [file bundle](https://meltano.com/docs/command-line-interface.html#file-bundle) for [GitLab CI/CD](https://docs.gitlab.com/ee/ci/).

Files:
- [`.gitlab-ci.yml`](./bundle/.gitlab-ci.yml)
- [`.gitlab/ci/docker.gitlab-ci.yml`](./bundle/.gitlab/ci/docker.gitlab-ci.yml)

This file bundle builds on top of the [Docker file bundle](https://gitlab.com/meltano/files-docker).

```sh
# Add Docker files to your Meltano project
meltano add files docker

# Add GitLab CI/CD files to your Meltano project
meltano add files gitlab-ci
```
