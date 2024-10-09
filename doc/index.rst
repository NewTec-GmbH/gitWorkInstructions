NewTec Git Work Instructions
=====================================

Git is not restrictive on how the project structure shall look like, or how each repository shall be configured, making it the responsibility of users that work together to agree on the conventions and structures to be used. Depending on the project complexity and team size, different rulesets ensure either light overhead and flexibility or a tight harness around each developer.

This documentation is intended to introduce the overall branching strategy to be used in all NewTec projects, specifically those hosted in `GitHub <https://github.com/NewTec-GmbH>`_. It will serve as a starting point for new project members to get up to speed with the existing workflow and a reference manual for developers.


.. toctree::
   :caption: Git:
   :maxdepth: 2

   git/git.md
   git/github.md
   git/templates.md


.. toctree::
   :caption: Branches:
   :maxdepth: 2

   branches/branch_types.md
   branches/pull_request.md


.. toctree::
   :caption: CI/CD:
   :maxdepth: 2

   ci/ci.md
   ci/cd.md


.. mermaid::

   %%{init: { 'gitGraph': {'showCommitLabel': false}} }%%
   gitGraph
      commit tag: "v1.0.0"
      branch release/v2.0.x
      branch feature/UI
      commit
      checkout release/v2.0.x
      branch feature/AJAX
      commit
      checkout release/v2.0.x
      merge feature/AJAX
      checkout feature/UI
      commit
      checkout release/v2.0.x
      merge feature/UI
      checkout main
      merge release/v2.0.x tag: "v2.0.0"
      branch release/v3.0.x
      branch feature/DB
      commit
      checkout release/v3.0.x
      merge feature/DB
      checkout main
      checkout release/v2.0.x
      branch bugfix/Button
      commit
      checkout release/v2.0.x
      merge bugfix/Button tag: "v2.0.1"
      checkout release/v3.0.x
      branch feature/UI_rework
      commit
      checkout release/v3.0.x
      merge feature/UI_rework
      merge bugfix/Button
      checkout main
      merge release/v3.0.x tag: "v3.0.0"

.. toctree::
   :caption: Submodule Based Configuration Managment:
   :maxdepth: 2

   versioning/submod_versioning.md
