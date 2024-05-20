# Level 2

### How to

0. Install docker
Then at the root level of the project :
1. Build docker image
   - `docker-compose build`
2. Start docker
   - `docker-compose up -d`
3. Run emitter script 
   - `python member_data_emitter.py`

### Action plan
- Build a multi container app with one container for the server and one container for the database
- Initialize database schema automatically 
- Implement logic for listenning to post requests from emitter script
- Use an ORM (for better readability)
- Refacto some methods from LEVEL_1 into a file `utils.py` 

### Improvments ideas
- At this stage the docker is not deployment ready, prepare next steps
- Automate pipeline (emitter script)
- Package LEVEL_1 folder for portability to import the package later in app.py (instead of duplicating utils.py file)
- Add contraints in database 
- Add hooks running automatically on database to check data integrity
- Handle secrets
