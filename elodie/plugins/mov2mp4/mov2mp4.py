"""
convert mov files to mp4
"""
from __future__ import print_function

from elodie.plugins.plugins import PluginBase

class Dummy(PluginBase):

    __name__ = 'mov2mp4'

    
    def __init__(self):
        self.before_ran = False

    def after(self, file_path, destination_folder, final_file_path, metadata):
        pass

    def batch(self):
        pass

    def before(self, file_path, destination_folder, media):
        print("From mov2mp4:",media ,file_path, destination_folder)
        if media == 'mov':
            print("From mov2mp4:",media ,file_path, destination_folder)

