import os

def search_file(path):
    for elem in os.listdir(path):
        res_path = os.path.join(path, elem)
        if elem == 'main.py':
            file = open(res_path, 'r', encoding='utf-8')
            data = file.read()
            file.close()
            file_2 = open('scripts.txt', 'a', encoding='utf-8')
            file_2.write(data)
            file_2.write('\n****************************************\n\n')
            file_2.close()
        if os.path.isdir(os.path.join(path, elem)) and elem != '.git':
            search_file(os.path.join(path, elem))



path = os.path.abspath(os.path.join('..', '..', 'Python_Basic'))


search_file(path)







