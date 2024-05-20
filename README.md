# Zoī Data engineering Challenge

## Guidelines

- clone this repo (do **not** fork it)
- solve the levels in ascending order
- commit your code at the end of each level

Each level uses the previous one, you can re-use your old code.

Don't hesitate to write shameless code at first, and then refactor it in the next levels.

We are interested in seeing code that is:
- maintainable
- clean
- robust
- reliable

Feel free to do whatever you want to achieve that, and not following blindly the existing code and choices made :)

Write your programs, or document your ideas, action plans, in the corresponding level directory.

We are waiting for python (^3.11) code.


## Context

We have a raw non-medical database of our members' behavior with regard to the medical recommendations we offer them through the Zoī app. 

The recommendations are crafted with the help of medical experts. We address several domains, such as nutrition and lifestyle, and our aim is to provide our members with recommendations that are 

1. adapted to their medical needs and constraints,
2. in the optimal format to make the members want to follow them.

Of course, members' eagerness to follow the recommendation isn't recorded; we have some personal information (age, sex), 
as well as a proxy for eagerness, time spent in waiting list; we believe that very enthusiastic members are more likely 
to register early and spent some time on the waiting list. Of course, time spent in waiting list is also a consequence of being in the "B2B" track, 
as companies also tend to register their members earlier, which has nothing to do with member eagerness. 
We don't record this "B2B" billing information, but we do record whether the app is given with default langage French or English, 
bearing in mind that "B2B" members are more prone to be given a version of the app with English as the default language, than "non-B2B".

## Level 1

The member-data logs are infos we get from our members, one log per member. 

Run the `member_data_generator.py` script in order to generate member data logs into folder `./raw/member-{id}.log`
Each file represent one member and will look like this:

`{id="ada6ee1abc22511c"|created_at="2023-06-27"|sex=1|age=48|default_language_en=false|waiting_list_time=13.3|black_and_white_design=true|follow_reco=63.6405580207529|follow_reco_above_50p=true}`

The goal is to read all these files and transform them into json files in `./processed/member-{id}.json` like this: 

```
{
   'id': 'ada6ee1abc22511c', 
   'created_at': '2023-06-27', 
   'sex': 1, 
   'age': 48, 
   'default_language_en': False, 
   'waiting_list_time': 13.3, 
   'black_and_white_design': True,
   'reco': {
      'follow_reco': 63.6405580207529, 
      'follow_reco_above_50p': True
   }
}
```

### Data details


- `id`: unique member ID
- `created_at`: created date of the member analytics
- `sex`: sex of member
- `age`: age of member
- `waiting_list_time`: time spent in waiting list
- `default_language_en`: whether the app was given with default langage english (vs french)
- `black_and_white_design`: whether the app shows the reco with black & white design, or colorful design
- `follow_reco`: a score estimating the percentage of recommendations followed by the member
- `follow_reco_above_50p`: whether the previous score is above 50%

## Level 2

The goal for this level is to process raw member data and store it in a relational database.

Run the program `member_data_emitter.py` that will send unprocessed member data to the address http://127.0.0.1:5000. 
Create a simple HTTP server that will listen to these requests, process member data using processing done in level 1 
and write them into `member` table in a relational database.

You can use a table like this per example:

```
CREATE TABLE member (
    id CHAR(16) PRIMARY KEY,
    created_at DATE,
    sex SMALLINT,
    age SMALLINT,
    default_language_en BOOLEAN,
    waiting_list_time NUMERIC(5,2),
    black_and_white_design BOOLEAN,
    follow_reco NUMERIC(5, 2),
    follow_reco_above_50p BOOLEAN
);
```

Use the method you prefer to set up this database :) 

Hint : You can look at Flask or FastAPI framework per example.

## SQL level

Based on the table previously created we would like to answer these questions:

1. **Segmenting Members Based on Activity Criteria :** 
   Segment members into three categories based on these characteristics : 
   - 'High Engagement' : waiting_list_time less than 10 and follow_reco_above_50p as true.
   - 'Moderate Engagement' : waiting_list_time between 10 and 20 (inclusive) or follow_reco_above_50p as false.
   - 'Low Engagement' : all others.
   - Show the count of members in each category.

2. **Analyzing Member Engagement :**
   - Compute the rolling average of the follow_reco score for each member over their previous 3 entries, 
   ordered by created_at. 
   - Assume that each row represents a separate instance of member activity. 
   - Display the member's ID, the current follow_reco score, and the rolling average. 
   - Consider only members who have at least one follow_reco score above 75.

You can write your queries in the file `level_sql/queries.sql`.

If you haven't made technical level 2 (or don't have time to do it), you can use data stored in 
`./sample/member_data.csv`. In this case, no obligation of setting up a database, we'll only focus on the sql code.

Have fun ! :)
