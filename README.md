OpenFEDEM Homepage
==================

Welcome to the repository for the OpenFEDEM homepage.
This repository contains the source files (Markdown) and content for the [OpenFEDEM website](https://www.openfedem.org).

## Introduction

OpenFEDEM (Open Finite Element Dynamics of Elastic Mechanisms) is an open source software package
developed to provide comprehensive solutions in active nonlinear structural dynamics and adjacent engineering fields.
The GUI part of this package can be found at [SAP/fedem-gui](https://github.com/SAP/fedem-gui)
whereas the solvers can be fond at [SAP/fedem-solvers](https://github.com/SAP/fedem-solvers).

This repository is dedicated to the development and maintenance of OpenFEDEM's official website,
built using [MkDocs](https://www.mkdocs.org/) from the Markdown source files.

## Installation

To set up a local version of the web site for development purposes, you will need to install `MkDocs`.
Follow these steps:

1. Clone this repository:

       git clone https://github.com/openfedem/openfedem.org.git

2. Install MkDocs:

       pip install mkdocs mkdocs-material pymdown-extensions

   See the [MkDocs Installation Guide](https://www.mkdocs.org/#installation) for further instructions.

3. Navigate to the cloned directory `openfedem.org and run the command

       mkdocs serve

   This will start a local web-server and you can view the results by visiting the address
   `http://127.0.0.1:8000` in your web browser.

## Usage

After setting up the local environment:

- Edit the Markdown files to update the website content locally.
  The changes will be visible immediately in the local web server when using `mkdocs serve`.

- Once all changes are finalized, they can be built into static files by running the command

      mkdocs build

## Conversions

The first line holds the title of the subpage and shall have Markdown heading level 1, typically `#<title>`

The Markdown heading level 2, e.g., `##<section heading>`, represents the first section level, and so on.

## Contributing

Contributions to improve this website are welcome. Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and test them locally.
4. Submit a pull request with a clear description of the changes.

For more detailed instructions, see [CONTRIBUTING.md](CONTRIBUTING.md).

## Administration

All raw files used by `MkDocs` to make the static website shall be located under the [docs](docs) directory
and adequately linked into the `nav` section of the [mkdocs.yml](mkdocs.yml) file.

### Publish

Publishing new website content can only be performed using the OpenFEDEM website admin user.

Build a local static version with `mkdocs build`. This will create or update a `site` directory where all the files
to be pushed to the web server are located. This can be done from [one.com](https://www.one.com)'s file browser, alternatively using SFTP.
Visit `one.com`'s user guide for more information.

## License

This project is licensed under the [MIT License](LICENSE).???

## Contact

For questions or suggestions regarding OpenFEDEM, please contact [Your Contact Information]. ???

---

This README is a guide to help users and contributors understand and participate in the development of the OpenFEDEM **_website_**. For more information on the OpenFEDEM software's source code, visit [fedem-gui repository](https://github.com/SAP/fedem-gui) and/or [fedem-solvers repository](https://github.com/SAP/fedem-solvers).

