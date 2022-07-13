import os

def catalog(project):
    for elem in os.listdir(project):
        path_catalog = os.path.join(project, elem)
        print('    ', path_catalog)

def direct(name):
    path = os.path.abspath(os.path.join('..', '..', name))

    print('Содержимое каталога {}'.format(path))

    catalog(path)


directory = 'Python_Basic'

direct(directory)

