# Branches

This page will introduce the naming conventions for the different types of branches and highlight their specific use cases.

## Main branch

The `main` branch is the singular and first branch existing on a new repository.
It is used to represent the current state of the project, therefore it is most important to keep it in a stable state.

:::{danger}
Direct work on the `main` branch is forbidden!
:::

The `main` branch is used to track the latest release version of the project. A release is a traceable version of the project, and therefore the `main` branch can be seen as an overview of the different releases, as seen below:

```{mermaid}
%%{init: { 'gitGraph': {'showCommitLabel': false}} }%%
gitGraph
   commit
   commit tag: "v1.0.0"
   commit tag: "v2.0.0"
   commit tag: "v2.2.0"
   commit tag: "v3.0.0"
```

Note that the commits in the figure above are the result of merge operations from [release branches](#release-branches).

:::{hint}
We use [Semantic Versioning](https://docs.npmjs.com/about-semantic-versioning) to determine the version number of each release.
:::

## Release branches

Release branches serve as a staging area for the integration of new features and fixes.

A release branch has the prefix `release/` followed by the **future** release version that will be published to main when the work on all features has been completed excluding the patch version: `release/v<major>.<minor>.x`. For example, the branch `release/v2.0.x` contains all the patches belonging to major version 2 and minor version 0.

While the state of the software on a release branch does not necessarily have to be stable, they are not intended to be worked on directly. For this reason, [feature](#feature-branches) and [bugfix](#bugfix-branches) branches are introduced.

### Ready for release

Once all the features planned for the release have been implemented and the release branch is ready, a [Pull Request (PR)](./pull_request.md) can be started to merge it into `main`.

:::{warning}
A [Pull Request (PR)](./pull_request.md) **must** be performed to merge a `release` into `main`.
:::

```{mermaid}
%%{init: { 'gitGraph': {'showCommitLabel': false}} }%%
gitGraph
   commit
   commit tag: "v1.0.0"
   branch release/v2.0.x
   commit
   commit
   commit
   checkout main
   merge release/v2.0.x tag: "v2.0.0"
```

In an ideal world, the work on release v3.0.0 can begin after release v2.0.0 is completed and the new tag can be used as a branching point for the next release branch. In practice, shifting priorities and complexities will result in the need for parallel release branches as shown below.

```{mermaid}
%%{init: { 'gitGraph': {'showCommitLabel': false}} }%%
gitGraph
   commit
   commit tag: "v1.0.0"
   branch release/v2.0.x
   commit
   commit
   branch release/v3.0.x
   commit
   checkout release/v2.0.x
   commit
   checkout main
   merge release/v2.0.x tag: "v2.0.0"
   checkout release/v3.0.x
   merge release/v2.0.x
   commit
   commit
   checkout main
   merge release/v3.0.x tag: "v3.0.0"
```

:::{important}
Do not delete the `release/` branches after these have been merged to `main`!
You can keep using them for future patches or bugfixes, or as reference for future development.
:::

## Feature branches

Feature branches are created to implement or change a distinct feature. There are no special restrictions on feature branches and work can be directly commited to a feature branch.

Feature branch naming convention is a prefix plus the name of the feature to be worked on, like `feature/multiuser_support` or `feature/client_rework`.

```{mermaid}
%%{init: { 'gitGraph': {'showCommitLabel': false}} }%%
gitGraph
   commit tag: "v1.0.0"
   branch release/v2.0.x
   branch feature/multiuser_support
   commit
   checkout release/v2.0.x
   branch feature/client_rework
   commit
   checkout feature/multiuser_support
   commit
   checkout feature/client_rework
   commit
   checkout release/v2.0.x
   merge feature/multiuser_support
   merge feature/client_rework
   checkout main
   merge release/v2.0.x tag: "v2.0.0"
```

:::{warning}
A [Pull Request (PR)](./pull_request.md) **must** be performed to merge a `feature` into a `release`.
:::

## Bugfix branches

Bugfix branches are indicated by the `bugfix/<name>` naming sheme. They are used to solve identified issues in already existing releases.
To make these fixes available for already published releases, a special release branch can be created. For example branch `release/v4.0.x` would serve as the way to release bugfix versions of release v4.0.0.
This allows for a cleaner main branch and the possibility to resolve issues in old releases without affecting the work for future software versions.

```{mermaid}
%%{init: { 'gitGraph': {'showCommitLabel': false}} }%%
gitGraph
    commit tag: "v3.0.0"
    branch release/v4.0.x
    commit
    checkout main
    merge release/v4.0.x tag: "v4.0.0"
    branch release/v5.0.x
    commit
    checkout main
    checkout release/v4.0.x
    branch bugfix/error_condition
    commit
    commit
    checkout release/v4.0.x
    merge bugfix/error_condition
    checkout main
    merge release/v4.0.x tag: "v4.0.1"
    checkout release/v5.0.x
    commit
    checkout main
    merge release/v5.0.x tag: "v5.0.0"
```

:::{warning}
A [Pull Request (PR)](./pull_request.md) **must** be performed to merge a `bugfix` into a `release`.
:::
