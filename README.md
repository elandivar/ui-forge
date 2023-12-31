# UI-Forge

UI-Forge is a tool designed to streamline the setup process for initiating any Laravel-based admin interface development project. It utilizes open-admin on Laravel and neatly packages it all in a Docker microservices architecture.

Within minutes, a developer can start working on a clean interface for their Laravel-based application.

UI-Forge is compatible across all operating systems (Windows, Linux, macOS) that have Docker installed.

## Requirements

Before running UI-Forge, ensure that your system meets the following requirements:

1. **Python:** UI-Forge is a Python script, so you need Python installed in your system. Check if you have Python using the command: `python --version`. If you don't have Python installed, you can download it from the [Python official website](https://www.python.org/).

2. **Docker Compose:** The tool uses Docker Compose to manage Docker applications. Check if you have Docker Compose installed using the command: `docker-compose --version`. If you don't have Docker Compose installed, you can download it from the [Docker official website](https://docs.docker.com/compose/install/).

## Installation

To use UI-Forge, follow the steps below:

1. Clone this repository to your local machine.
2. Navigate to the 'ui-forge' directory, containing the install.py file.
3. Run the command: `python install.py`

Follow the instructions provided by the script to set up your Laravel-based admin interface.

Check a video demonstration about how to create a Laravel admin interface in less than 3 minutes.

[<img src="https://github.com/elandivar/ui-forge/blob/main/images/video_screen.png" width="80%">](https://youtu.be/Pw6qxI8N3jc "Creating a Web based admin portal in less than 3 minutes!")


## Additional Documentation

Since UI-Forge installs Laravel and OpenAdmin, it is higly recommended to review the OpenAdmin official documentation:

- [Open Admin Documentation](https://open-admin.org/docs)

## Usage

Just navigate to http://localhost:8000 or http://localhost:8000/admin

The easiest way to start expanding the default OpenAdmin functionality is to use the Helpers->Scaffold menu on the Admin interace.

The default username/password is admin/admin. Change it immediately after installation!

## To-do

1. In install.py, check if the docker cointainers are already running.
2. In install.py, change the project name inside the OpenAdmin GUI.
3. Create a service administrator, in order to stop and restart UI-Forge containers.

## Contributions

Contributions, issues, and feature requests are welcome. Feel free to check issues page if you want to contribute.

## License

This project is licensed under the MIT License.

Happy Coding!

