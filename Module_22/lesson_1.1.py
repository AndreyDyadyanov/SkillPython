import os

pack = 'access'
file = 'admin.bat'

abs_path = os.path.abspath(os.path.join('..', pack, file))

print('Абсолютный путь до файла: \n{} \n'.format(abs_path))

rel_path = os.path.join('SkillPython', pack, file)

print('Относительный путь до файла: {}'.format(rel_path))

