# ubiquitous-waffle-library

![Language](https://img.shields.io/badge/Spellcheck-Pass-green?style=flat)
![Language](https://img.shields.io/badge/Language-Python-yellowgreen?style=flat)
![Testing](https://img.shields.io/badge/PEP8%20Check-Passing-green)
![Testing](https://img.shields.io/badge/Test-Pass-green)

## Description

This repository contains a project developed for Hack Club.

The program webpage.py, offers a simple system to keep a record of all the books someone has in their home.

This all started because I needed a DB for for my Home Library.

The website is very simple, it has only 3 pages:

- main: page with the main book table.
- status: page with the status of all the books.
- single book page: for each book, there is a page with his informations.

For the covers of the books, for now the link you should provide is only a static one,
so:

- download your cover,
- move it in the 'bin/static/covers/' directory
- use the 'add_link' function on the website and write the name of the picture in the box.

Now you should be able to see the cover in the book page.

I might add the possibility to add an online path (like an URL).

## Requirements

python >= 3.8

**Setting Up the Environment**

* Windows: `./start_Windows.bat`
* Linux/macOS: `./start_Linux.sh`

These scripts will install required dependencies, and build a virtual environment for you if you don't have one. They will also start the website automatically.

## Running the Program (CLI or GUI)

### CLI

1. Navigate to the `bin` directory: `cd bin`

2. Execute `python webpage.py [--help]` (use `python3` on Linux/macOS) in your terminal

    The `--help` flag displays available command-line arguments.

### GUI

Double click on the *start files* for your OS, and it should start the website automatically after setting up the environment, like I wrote in the **Requirements** area.

At some point it will ask you 'LAN IP? (y/n):', if you say 'y' then you will load your page on a IP address that is visible from other devices in your LAN network. With 'n' you will run it locally, no access from outside your computer.

## Author

Neetre
