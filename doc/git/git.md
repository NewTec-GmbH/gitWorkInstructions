# Git

## What is Git?

[Git](https://git-scm.com/) is a Version Control System (VCS) used in a huge amount of projects, not only open-source but also private and in the industry. It works by creating "snapshots" of your files, so you can share them with others or come back to an old version if something is not working right. It allows efficient cooperative work and a traceable lifecycle for software projects, which is a great advantage for developers.

## Installation and Configuration

### Installer

In order to install Git in your computer, head to the [download page](https://git-scm.com/download/win) and choose the correct version for your operating system. In this document we assume that you are using Windows.

Once you open the installer, you will go through a number of configuration screens. Below you can find the common configuration options that we use.

```{note}
If there is a screen or setting you cannot find, please contact your supervisor as the documentation may be out-of-date.

**Current Git Release**: v2.45.2
```

- Select Components:
  - **Choose**: Windows Explorer integration
  - **Choose**: Associate .git* configuration files with the default text editor
  - **Choose**: Any other setting of your preference. LFS is not necessary.

- Choosing the default editor used by Git
  - **Choose**: Use the editor of your preference. We use Visual Studio Code, or Notepad in case VSCode is not installed.

- Adjusting the name of the initial branch in new repositories
  - **Choose**: Override the default branch name. Use `main`

- Adjusting your PATH environment
  - **Choose**: Git from the command line and also from 3rd-party software

- Choosing the SSH executable:
  - **Choose**: Use bundled OpenSSH

- Choosing HTTPS transport backend
  - **Choose**: Use the OpenSSL library

- Configuring the line ending conversions:
  - **Choose**: Checkout as-is, commit as-is

- Configuring the terminal emulator to use with Git Bash:
  - **Choose**: Use MinTTY

- Choose the default behavior of "git pull"
  - **Choose**: Fast-forward or merge

- Choose a credential helper:
  - **Choose**: Git Credential Manager

- Configuring extra options
  - **Select**: Enable file system caching

### Existing installation

In case you already have Git installed in your machine, make sure the following configurations are set in your `.gitconfig` file:

```ini
[core]
 eol = crlf
 autocrlf = false
 editor = code --wait

[user]
 name = <your-name>
 email = <your-NewTec-email>

[init]
 defaultBranch = main
```

You can write these manually, or set them using the following commands:

```bash
git config --global core.eol crlf
git config --global core.autocrlf false
git config --global core.editor "code --wait"
git config --global user.name <your-name>
git config --global user.email <your-NewTec-email>
git config --global init.defaultBranch main
```

## Using Git

To learn more about using Git, you can visit this [cool website](https://learngitbranching.js.org/).

## Ignore Files

You do not always want to commit everything on your folder, for example, lots of automatically-generated documentation.
This is where the `.gitignore` file comes into play.

[Here](https://github.com/NewTec-GmbH/template_python/blob/main/.gitignore) is an example of how a common ignore file looks like for a Python project. You can add or remove lines depending on your use case but you generally want to ignore any file or folder that can be generated.

:::{danger}
Never commit sensitive data, API keys, credentials, or similar data!
:::

## Line Endings

Line endings are invisible characters that are present on every file and determine how this is to be interpreted by your computer. For Linux machines, the line ending is `LF`, while for Windows it is `CRLF`. Given that we usually work with Windows, the default for all text-based files should always be `CRLF`.

:::{attention}
An exception is made by generated files from tools such as Doxygen, which are usually `LF` and should remain this way.
:::

In order to standarize which files have which ending, a `.gitattributes` file should be present in your repository. [Here](https://github.com/NewTec-GmbH/template_python/blob/main/.gitattributes) is an example of how a common attributes file looks like for a Python project. You can add or remove lines depending on your use case.

## Integrations

Integrations with 3rd-party tools may simplify the way you interact with Git, either by providing a GUI or by showing more information on your current work.

:::{tip}
These are tools that may help you, but are not necessary to use Git.
:::

- Visual Studio Code:
  - Integrated "Source Control" (`Ctrl + Shift + G`) : Tracks your changes, branches, and provides a text field for easy commits.
  - Extension "Git Graph": Visualize your branches and commits.
- TortoiseGit
  - Similar to TortoiseSVN.
  - Provides a simple GUI to manage your local repository without using the commmand line.

:::{attention}
These are just tools! You must still understand what you are doing!
:::

## FAQ

:::{admonition} Git configuration not found on `G:/` drive.
:class: tip
:class: dropdown

On a fresh PC installation, and after following all installation steps for Git, commands may fail with an error related to the `G:/` drive.
This is due to the configuration being present in the `C:/` drive instead.

To fix this, add the following environment variable:

| Key  | Value                  |
| ---  | ---                    |
| HOME | `C:\Users\<your-user>` |

:::
