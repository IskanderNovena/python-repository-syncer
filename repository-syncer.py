import json
import os
import shutil
import subprocess

# Opening the file as part of loading the JSON-file automatically closes the
# file after loading it. Otherwise, an explicit 'close' has to be done.
settings = json.load(open('settings.json'))
repositories = settings['repositories']

# Check if the given working directory exists
if not os.path.exists(settings['workingDirectory']):
    raise Exception(
        'Working-directory "{}" does not exist!'.format(settings['workingDirectory']))


def sync_repo(source, destination):
    # Get the name of the repository from the source
    repo_dir = source.rsplit('/', 1)[-1]
    full_repo_dir = os.path.join(settings['workingDirectory'], repo_dir)
    os.chdir(settings['workingDirectory'])
    try:
        subprocess.check_call(["git", "clone", "--bare", "{}".format(source)])
        print(os.getcwd())
        os.chdir(full_repo_dir)
        print(os.getcwd())
        subprocess.check_call(
            ["git", "push", "--mirror", "{}".format(destination)])
    except subprocess.CalledProcessError as error:
        raise Exception("ERROR: Command '{}' failed with exit code '{}'".format(
            ' '.join(error.cmd), error.returncode))
    finally:
        if os.path.exists(full_repo_dir):
            print('Cleaning up directory...')
            shutil.rmtree(full_repo_dir)


for repo in repositories:
    print('\nProcessing sync for:\n  Source      : {}\n  Destination : {}\n'.format(
        repo['source'], repo['destination']))
    try:
        sync_repo(repo['source'], repo['destination'])
    except Exception as error:
        print('\n{}'.format(error))
        print('Processing has been interrupted!')
    else:
        print("\nDone!\nAll repositories have been processed.")
