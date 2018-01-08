class Module:
    def __init__(self, name, dir):
        self.name = name
        self.dir = dir
        pass

class PathKeeper:

    def __init__(self):
        pass
    def set_dir(self, dir):
        self.path = str(dir)
    def display_dir(self):
        print(self.dir)
    def find_py_files(self):
        pass

class Finder(PathKeeper):

    message = ''

    def __init__(self, search_term):
        self.term_len = 0
        self.search_term = self.set_search_term(search_term)

    def set_message(self, msg):
        self.message = str(msg)

    def display_message(self):
        print(self.message)

    def display_term(self):
        print(self.search_term)
        print(self.term_len)

    def set_search_term(self, search_term):
        try:
            length = len(search_term)
            if length > 80: raise ValueError("Term can not be longer than 80 characters!")
            self.term_len = length
            return str(search_term)
        except ValueError as e:
            self.set_message("Input error: {}".format(e))
            self.display_message()

import os
from os.path import join, getsize
from pathlib import Path

def main():
    """"
    print("Welcome, I am dummy searcher!")
    term = input("Write term to search for: ")
    f = Finder(term)
    f.display_term()
    f.set_dir("d/u/p/a")
    f.display_dir()
"""
    #print(os.name)
    print(Path('kod.py').suffix)
    modules = module_finder("C:\\Users\\Mariusz\\PycharmProjects\\sztuczki")
    print(modules)
    locations = module_browser(modules, 'def')
    #print(locations)
    for t in locations:
        print(t[2])

"""
    for root, dirs, files in os.walk("C:\\Users\\Mariusz\\PycharmProjects\\sztuczki"):
        print("root: ", root)
        print("dirs: ", dirs)
        print("files: ", files)
"""


def module_browser(modules, search_term):

    found_locations = []
    for (m, root) in modules:
        try:
            path = root + '\\' + m
            if os.path.isfile(path):
                with open(path, 'rb') as f:
                    for index, line in enumerate(f):
                        if search_term in str(line):
                            # removes \r\b\n and both trailing and leading whitespaces
                            line = str(line)[2:-5].strip()
                            found_locations.append((m, index, line))
            else:
                raise ValueError("There is no such file anymore: {}".format(path))
        except ValueError as e:
            print(e)
    return found_locations


def module_finder(path):

    py_files = []
    try:
        if os.path.isdir(path):
            for root, dirs, files in os.walk(path):
                for f in files:
                    if Path(f).suffix == '.py':
                        print(root, " plik: ", f)
                        py_files.append((f, root))
            return py_files
        else:
            raise ValueError("Path does not exist!")
    except ValueError as err:
        print("Error: {}".format(err))


if __name__ == "__main__": main()