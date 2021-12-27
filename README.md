# python-repository-syncer

Python-script to update Git Repository Mirrors, based on a JSON-formatted settings-file

## Installation

Clone this repository to a location of your choosing. Next, create a `settings.json` file (you can use the `settings.json.example` as a template) and change the source and destination of the two existing examples, adding or removing repository-entries as needed.

Change the `workingDirectory` to an existing location, that you want to use as the base-directory for the synchronisations.

## Usage

Run the script:

```bash
python3 repository-syncer.py
```

The script will read the list of repositories from `settings.json` which should exist in the same directory as the script.

<!--
## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.

-->