# Level 1

### How to

1. Create a virtual environment (common to the whole project); then at the root level of the project run
   - `pip install -r requirements.txt`
2. Run the scrip to generate log files
   - `python member_data_generator.py`
3. Move to level_1 folder 
   - `cd level_1`
4. Run click command line
   - `python cli.py process_log_files -i raw -o processed`
5. Move to test folder 
   - `cd test`
6. Run unit tests 
   - `pytest test_member_data_processor.py`
7. Run coverage : 
   - `coverage run -m pytest test_member_data_processor.py`
   - `coverage report -m`

Current coverage report : 

Name                                | Stmts   | Miss | Cover | Missing 
------------------------------------|---------|------|-------|-------- 
__init__.py                         | 0       | 0    | 100%  |-- 
member_data_processor.py            | 45      | 17   | 62%   | 14-15, 18-19, 22-29, 50-54 
test_member_data_processor.py       | 13      | 0    | 100%  |-- 
TOTAL                               | 58      | 17   | 71%   |-- 

### Action plan
- Write a script to process log files into json files
- Sample the data in a folder with one file to run tests 
- Write unit tests : anonimize test data
- Add a click command to run the script
- Install all packages while developping and pip freeze to get the requirements

### Improvments ideas
- Add a precommit hook to format the code automatically : blake, flake8, isort 
- Refacto the class with a utils file (some methods should not be class methods)
- Automate coverage with CI (gitlab runners)
- E2E test
- Control the input files 
- Control ouput format (all keys in json) if the object has no vocation to mutate
- Clean processed data at each run ? 
- Add a cache to manage already processed data ?
- Test values out of bound in files (for example age of 999 years)
- Add explicit logs
- Manage exceptions