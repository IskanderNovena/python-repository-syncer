import json
import os
import shutil

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
    os.chdir(settings['workingDirectory'])
    try:
        os.system('git clone --bare {}ass'.format(source))
        os.chdir('./{}'.format(repo_dir))
        os.system('git push --mirror {}'.format(destination))
        os.chdir(settings['workingDirectory'])
    except:
        raise Exception('Something went horribly wrong!!')
    finally:
        if os.path.exists(os.path.join(settings['workingDirectory'], repo_dir)):
            shutil.rmtree(repo_dir)  # , ignore_errors=True)


for repo in repositories:
    print('Processing sync for:\n  Source      : {}\n  Destination : {}\n'.format(
        repo['source'], repo['destination']))
    sync_repo(repo['source'], repo['destination'])
      
    print("\nDone!\nAll repositories have been processed.")
