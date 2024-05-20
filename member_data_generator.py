# -*- coding: utf-8 -*-

import os
from lib.synthetic_data import generate_synthetic_data


def save_synthetic_data_to_log_file():

    synthetic_data = generate_synthetic_data()

    # Extracting the id from the synthetic data
    member_id = synthetic_data.split('|')[0].split('=')[1].strip('"')

    # Ensure the directory './raw' exists
    directory = './raw'
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Constructing the filename
    filename = f'member-{member_id}.log'
    filepath = os.path.join(directory, filename)

    # Saving the synthetic data to the file
    with open(filepath, 'w') as file:
        file.write(synthetic_data)

    print(f'Synthetic data for member {member_id} saved to {filepath}')


if __name__ == "__main__":

    for _ in range(1000):
        save_synthetic_data_to_log_file()
