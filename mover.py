import glob
import shutil
from os import chdir
from os import path
from os.path import join
import os


class Mover(object):
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst
        self._files = []

    def get_all_pdfs(self):
        self._get_files("*pdf")

    def get_all_mp4(self):
        self._get_files("*mp4")

    def get_all_png(self):
        self._get_files("*png")

    def move_files(self):
        """Moves files from one directory to another. But the get get_all for
           either pdf, mp4 must be called before the move files can be executed
        """

        self._if_not_exists_create_folder()

        for file in self._files:
            new_path = join(self.src, file)
            shutil.move(new_path, self.dst)
        return True

    def _if_not_exists_create_folder(self):
        if not path.exists(self.dst):
            os.makedirs(self.dst)

    def _get_files(self, ext):
        if path.exists(self.src):
            chdir(self.src)
            self._files = glob.glob(f"{ext}")

