# -*- coding: utf-8 -*-

import requests
import random
from lib.synthetic_data import generate_synthetic_data_with_duplicates


def send_member_data(endpoint="http://127.0.0.1:5000"):

    # Generate a set of 100 ids to have multiple data by ids
    existing_ids = []

    for _ in range(0, 100):
        member_id = ''.join(random.choices('0123456789abcdef', k=16))
        existing_ids.append(member_id)

    # Generate 1000 messages and send them to the endpoint
    for _ in range(1000):
      try:
        requests.post(
            endpoint,
            json={'member': generate_synthetic_data_with_duplicates(existing_ids)}
        )
      except requests.ConnectionError:
        print(f'Connection refused on {endpoint}')


if __name__ == "__main__":

    send_member_data()
