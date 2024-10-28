# gitWorkInstructions

[![documentation](https://github.com/NewTec-GmbH/gitWorkInstructions/actions/workflows/documentation.yml/badge.svg)](https://github.com/NewTec-GmbH/gitWorkInstructions/actions/workflows/documentation.yml)

This is the documentation for the NewTec Git Work Instructions. You can find the resulting GitHub Pages in [here](https://newtec-gmbh.github.io/gitWorkInstructions/).

## Build the documentation

### Requirements

* Node 20
* Python 3.11

### Instructions

1. Clone the repository: `git clone https://github.com/NewTec-GmbH/gitWorkInstructions.git`
2. Change directory: `cd gitWorkInstructions`
3. Install Python dependencies: `pip install -r requirements.txt`
4. Install Node dependencies: `npm install`
5. Build the documentation: `sphinx-build doc _build --fail-on-warning`
6. Open the documentation: `_build/index.html`

### Visual Studio Code Tasks

If you are using VSCode, the commands mentioned above are packed into tasks, making it easier for the developer to use.

1. Clone the repository: `git clone https://github.com/NewTec-GmbH/gitWorkInstructions.git`
2. Open the folder with VSCode: `code ./gitWorkInstructions`
3. On the top menu, choose `Terminal` -> `Run Task...` and select the task you require.

#### Available Tasks

* Install Python Requirements
* Install NPM Requirements
* Install all requirements
* Build
* Clean
* Build and open

## Used Libraries

Used 3rd party libraries which are not part of the standard Python package:

* [Sphinx](https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html) - Powerful documentation generator that has many great features for writing technical documentation - BSD-2 License
* [sphinx-rtd-theme](https://sphinx-rtd-theme.readthedocs.io/en/stable/) - Read the Docs theme for Sphinx. - MIT License
* [sphinx-rtd-dark-mode](https://github.com/MrDogeBro/sphinx_rtd_dark_mode) - Adds a toggleable dark mode to the Read the Docs theme for Sphinx. - MIT License
* [sphinxcontrib-mermaid](https://github.com/mgaitan/sphinxcontrib-mermaid) - Mermaid diagrams in yours Sphinx powered docs. - BSD-2 License
* [sphinx-copybutton](https://github.com/executablebooks/sphinx-copybutton) - Add a "copy" button to code blocks in Sphinx. - MIT License
* [sphinx-togglebutton](https://github.com/executablebooks/sphinx-togglebutton) - Show and hide content with a button in Sphinx. - MIT License
* [myst-parser](https://github.com/executablebooks/MyST-Parser) - An extended commonmark compliant parser, with bridges to docutils/sphinx. - MIT License
* [mermaid-js/mermaid-cli](https://github.com/mermaid-js/mermaid-cli) - Command line tool for the Mermaid library. - MIT License

## Issues, Ideas And Bugs

If you have further ideas or you found some bugs, great! Create an [issue](https://github.com/NewTec-GmbH/gitWorkInstructions/issues) or if you are able and willing to fix it by yourself, clone the repository and create a pull request.

## License

The whole source code is published under [BSD-3-Clause](https://github.com/NewTec-GmbH/gitWorkInstructions/blob/main/LICENSE).
Consider the different licenses of the used third party libraries too!

## Contribution

Unless you explicitly state otherwise, any contribution intentionally submitted for inclusion in the work by you, shall be licensed as above, without any additional terms or conditions.
