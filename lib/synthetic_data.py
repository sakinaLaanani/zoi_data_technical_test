# -*- coding: utf-8 -*-
import random
import datetime

def generate_synthetic_data(member_id = None):

    # Generating a random member ID if none is provided. Otherwise, use the provided one
    if not member_id:
        member_id = ''.join(random.choices('0123456789abcdef', k=16))

    # Generating a random date within a specified range
    start_date = datetime.date(2023, 1, 1)
    end_date = datetime.date(2023, 12, 31)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    created_at = start_date + datetime.timedelta(days=random_number_of_days)

    # Randomly selecting sex (0 or 1 for simplicity)
    sex = random.randint(0, 1)

    # Generating a random age within a realistic range
    age = random.randint(18, 70)

    # Randomly setting default_language_en to true or false
    default_language_en = random.choice([True, False])

    # Generating a random waiting_list_time
    waiting_list_time = round(random.uniform(0, 30), 1)

    # Randomly setting black_and_white_design to true or false
    black_and_white_design = random.choice([True, False])

    # Generating a random follow_reco score
    follow_reco = round(random.uniform(0, 100), 2)

    # Determining follow_reco_above_50p based on follow_reco
    follow_reco_above_50p = follow_reco > 50

    # Formatting the output
    synthetic_data = f'{{id="{member_id}"|created_at="{created_at}"|sex={sex}|age={age}|default_language_en={str(default_language_en).lower()}|waiting_list_time={waiting_list_time}|black_and_white_design={str(black_and_white_design).lower()}|follow_reco={follow_reco}|follow_reco_above_50p={str(follow_reco_above_50p).lower()}}}'

    return synthetic_data


def generate_synthetic_data_with_duplicates(existing_ids = None):

    if random.random() < 0.25:  # 25% chance of reusing an existing ID

        if existing_ids:
            member_id = random.choice(existing_ids)
            return generate_synthetic_data(member_id=member_id)

        return generate_synthetic_data()

    return generate_synthetic_data()
