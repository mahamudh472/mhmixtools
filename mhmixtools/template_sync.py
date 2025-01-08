import os
from .decorators import execution_time

def list_html(exclude_dirs=None):
    path = os.getcwd()
    extentions = ('html', 'htm')
    if not exclude_dirs:
        exclude_dirs = []
    for root, dirs, files in os.walk(path):
        dirs[:] = [i for i in dirs if i not in exclude_dirs]
        for file in files:
            if file.endswith(extentions):
                print(os.path.relpath(os.path.join(root, file), path).replace('\\', '/'))
        