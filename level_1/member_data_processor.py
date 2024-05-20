import os
import json
import re

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
        filepath = os.path.join(self.output_path, filename)[:-4] + '.json'
        file = self.open_file(filepath, 'w+')
        try:
            json.dump(json_content, file)
            file.close()
        except Exception as error:
            print(error)

    def __format_reco(self, json_object): # TO DO: use variables for better maintanability
        json_object['reco'] = {
                "follow_reco": json_object["follow_reco"],
                "follow_reco_above_50p": json_object["follow_reco_above_50p"],
        }
        del json_object["follow_reco"]
        del json_object["follow_reco_above_50p"]
        return json_object
    
    def parse_log_file(self, filename):
        file = self.open_file(os.path.join(self.input_path, filename), 'r')
        file_content = file.read()
        file_content = file_content.replace('|', ',').replace('=', ':')
        json_formatted_content = re.sub(r'(\w+):', r'"\1":', file_content)
        file.close()
        json_object = json.loads(json_formatted_content)
        json_object = self.__format_reco(json_object)
        return json_object

    def process_files(self):
        self.create_output_dir()
        for filename in os.listdir(self.input_path):
            if filename.endswith(".log"):
                json_content = self.parse_log_file(filename)
                self.save_file(filename, json_content)

