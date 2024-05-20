import os
import json
import re
from utils import parse_string_to_json
#import sys
#sys.path.append('..')
from utils import parse_string_to_json 

class Processor:
    def __init__(self, input_folder, output_folder):
        self.input_path = os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.pardir)), input_folder)
        self.output_path = os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.pardir)), output_folder)

    def open_file(self, path, right): # TO DO : move to utils
        try:
            file = open(path, right)
            return file
        except Exception as error:
            print(error)

    def create_output_dir(self): # TO DO : move to utils and refacto to create_dir
        if not os.path.isdir(self.output_path):
            os.mkdir(self.output_path)

    def save_file(self, filename, json_content):
        filepath = os.path.join(self.output_path, filename)[:-4] + ".json" # TO DO : place file extensions in constants file
        file = self.open_file(filepath, "w+") # TO DO : place file right modes in constants file
        try:
            json.dump(json_content, file)
            file.close()
        except Exception as error:
            print(error)

    def __format_reco(self, json_object):
        follow_reco = "follow_reco"
        follow_reco_above_50p = "follow_reco_above_50p"
        json_object["reco"] = {
                follow_reco: json_object[follow_reco],
                follow_reco_above_50p: json_object[follow_reco_above_50p],
        }
        del json_object[follow_reco]
        del json_object[follow_reco_above_50p]
        return json_object
    
    def parse_log_file(self, filename):
        file = self.open_file(os.path.join(self.input_path, filename), "r")  # TO DO : place file right modes in constants file
        file_content = file.read()
        json_object = parse_string_to_json(file_content)
        file.close()
        json_object = self.__format_reco(json_object)
        return json_object

    def process_files(self):
        self.create_output_dir()
        for filename in os.listdir(self.input_path):
            if filename.endswith(".log"): # TO DO : place file extensions in constants file
                json_content = self.parse_log_file(filename)
                self.save_file(filename, json_content)

