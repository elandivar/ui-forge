import os
import re
import subprocess
import shutil
import sys

def check_docker_installed():
    try:
        subprocess.check_output(["docker-compose", "--version"])
    except FileNotFoundError:
        print("docker-compose is not installed. Please install it and try again.")
        sys.exit(1)

def check_files_exist():
    if not (os.path.isfile("./Dockerfile") or os.path.isfile("./docker-compose.yml")):
        print("Dockerfile or docker-compose.yml not found. Please make sure either of them is present in the current directory.")
        sys.exit(1)

def get_input(param_name, default_value, required=False, length_limit=16):
    while True:
        try:
            value = input(f"Please enter {param_name} ({default_value if not required else 'mandatory'}): ")
            value = value or default_value
            if not value and required:
                raise ValueError(f"{param_name} is a required parameter. Please provide a value.")
            if length_limit and (len(value) > length_limit or not re.match("^[a-zA-Z0-9_]+$", value)):
                raise ValueError(f"Invalid {param_name}. Please make sure it is not longer than {length_limit} characters and contains only alphanumeric characters and underscores.")
            return value
        except ValueError as e:
            print(str(e))

def replace_macros_in_env_file(db_name, db_user, db_pass):
    if os.path.isfile("./.env"):
        overwrite = input("File .env already exists. Do you want to overwrite it? (yes/no): ")
        if overwrite.lower() != "yes":
            print("Leaving existing .env file.")
            return
    print("Generating .env file...")
    with open("env.tpl", "r") as file:
        file_data = file.read()
    file_data = file_data.replace("{DB_DATABASE}", db_name)
    file_data = file_data.replace("{DB_USERNAME}", db_user)
    file_data = file_data.replace("{DB_PASSWORD}", db_pass)
    with open(".env", "w") as file:
        file.write(file_data)

# This function updates the config files for OpenAdmin. It reads the config/admin.php and 
# changes the values of the expression with the sintax "'variable' => 'value'"
def replace_openadmin_config(project_name):
    print("Updating OpenAdmin config files")
    with open("./laravel/config/admin.php", "r") as file:
        file_data = file.read()
    file_data = file_data.replace("'name' => 'Open Admin',", "'name' => '" + project_name+ "',")
    with open("./laravel/config/admin.php", "w") as file:
        file.write(file_data)

def check_laravel_directory():
    if os.path.isdir("./laravel"):
        print("Warning: Deleting the 'laravel' directory could result in data loss. Please make sure you have a backup before proceeding.")
        delete = input("Directory 'laravel' already exists. Do you want to delete it? (yes/no): ")
        if delete.lower() != "yes":
            print("Leaving existing 'laravel' directory. Execution stopped.")
            sys.exit(1)
        else:
            print("Deleting 'laravel' directory...")
            shutil.rmtree('./laravel')

def run_commands():
    if sys.platform == "win32":
        commands = [
            'docker-compose build app',
            'mkdir laravel',
            'docker-compose up -d',
            'docker-compose exec app composer create-project --prefer-dist laravel/laravel .',
            'del .\\laravel\\.env',
            'copy .env .\\laravel\\',
            'docker-compose exec app composer require open-admin-org/open-admin',
            'docker-compose exec app php artisan vendor:publish --provider="OpenAdmin\\Admin\\AdminServiceProvider"',
            'docker-compose exec app php artisan admin:install',
            'docker-compose exec app php artisan key:generate',
            'docker-compose exec app composer require open-admin-ext/helpers',
            'docker-compose exec app php artisan admin:import helpers',
            'copy .\\installer\\welcome.blade.php .\\laravel\\resources\\views\\'
        ]
    else:
        commands = [
            'docker-compose build app',
            'mkdir laravel',
            'docker-compose up -d',
            'docker-compose exec app composer create-project --prefer-dist laravel/laravel .',
            'rm ./laravel/.env',
            'cp .env ./laravel/',
            'docker-compose exec app composer require open-admin-org/open-admin',
            'docker-compose exec app php artisan vendor:publish --provider="OpenAdmin\\Admin\\AdminServiceProvider"',
            'docker-compose exec app php artisan admin:install',
            'docker-compose exec app php artisan key:generate',
            'docker-compose exec app composer require open-admin-ext/helpers',
            'docker-compose exec app php artisan admin:import helpers',
            'cp ./installer/welcome.blade.php ./laravel/resources/views/'
        ]
        
    for command in commands:
        print(f"Running command: {command}")
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        while True:
            line = p.stdout.readline()
            if not line:
                break
            print(line.decode('utf-8').strip())
        p.wait()
        if p.returncode != 0:
            print(f"An error occurred while running command '{command}'.")
            sys.exit(1)
    print("All commands executed successfully.")

def main():
    check_docker_installed()
    check_files_exist()
    project_name = get_input("Project name", "", required=True, length_limit=32)
    db_name = get_input("database name", "uiforge")
    db_user = get_input("database user name", "uiforge")
    db_pass = get_input("database user password", "", required=True, length_limit=None)
    replace_macros_in_env_file(db_name, db_user, db_pass)
    check_laravel_directory()
    run_commands()
    replace_openadmin_config(project_name)

if __name__ == "__main__":
    main()

