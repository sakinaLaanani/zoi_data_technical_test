import unittest
import os
import json
import sys
sys.path.append('..')
from member_data_processor import Processor


class TestMemberDataProcessor(unittest.TestCase):

    def setUp(self):
        self.processor = Processor("test/input_data_tests", "test/output_tests")

    def test_parse_log_file(self):
        # Process the member log file in json
        processed_member = self.processor.parse_log_file("member-123.log")

        # Get the expected json
        with open(os.path.join(os.path.join(os.getcwd(), 'input_data_tests/member-123.json'))) as file:
            expected_member = file.read()
            expected_member = json.loads(expected_member)

        assert processed_member == expected_member