# The main file used for generating CHAOSS Metrics Release PDF

import pypandoc
import git
import os, subprocess
import helper
from sys import argv, exit
import yaml
from pprint import pprint
from shutil import copyfile

paths = []

def display_banner():
    helper.banner()


def help_message():
    print("\nUsage: python3 main.py active_user_input/WG_conf.yml")
    print("Make sure WG_conf.yml is configured properly")
    exit(1)


def change_env():

    # clean test_env dir
    print("\nCleaning test_env directory...\n")
    os.system("rm -rf test_env/*")

    # copy all files from active + passive dirs to test_env
    for dir in ["active_user_input", "passive_user_input"]:
        for file in os.listdir(dir):
            src = dir + '/' + file
            dst = 'test_env/' + file
            print(f'Copying file {src} to {dst}')
            copyfile(src, dst)

    print("\nMoving to test_env...")
    os.chdir("test_env")


def clone_WG_repo(key, values):

    print(f"\nCloning '{key}' from '{values['github-branch']}' branch\n")
    subprocess.check_call(['git', 'clone', '-b', values['github-branch'], values['github-link'], key])
















def main():

    global paths

    # display banner
    # display_banner()

    # read the YML file
    try:
        with open(argv[1]) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
    except:
        help_message()

    print("\nLoading the YML file...")
    print("YML file structure: \n")
    pprint(data)

    change_env()

    for key, values in data.items():

        if values['include-wg-flag']:

            clone_WG_repo(key, values)

            
            # # generate markdown for WG names
            # paths = helper.generate_WG_md(values['wg-name'], 1, paths)

            # paths = generate_paths(values, paths)

        else:
            print('\n[WARNING]: Flag off for {}, ignoring this WG'.format(key))











if __name__ == '__main__':
    main()
