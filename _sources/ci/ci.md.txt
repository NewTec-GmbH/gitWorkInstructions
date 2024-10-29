# Continuous Integration

Continuous integration is a DevOps software development practice where developers regularly merge their code changes into a central repository, after which automated builds and tests are run. (Source: [AWS](https://aws.amazon.com/devops/continuous-integration/))

## Github Actions

GitHub Actions are the Continuous Integration service of GitHub, which is configured on each of our projects to run tests, build documentation, lint and do much more automatically.

The process is configured using a workflow file found in the `.github/workflows/` folder and specified in `.yml` format. An example workflow file can be found [here](https://github.com/NewTec-GmbH/template_python/blob/4d2acf95ab71a20211560b5fe9471267ede13582/.github/workflows/test.yml).
