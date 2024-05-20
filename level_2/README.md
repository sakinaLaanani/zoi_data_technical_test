# Level 2

### How to

0. Install docker
Then at the root level of the project :
1. Build docker image
   - `docker-compose build`
2. Start docker
   - `docker-compose up -d`
3. Navigate to 
   - `http://127.0.0.1:5000`
4. Run emitter script 
   - `python member_data_emitter.py`
5. Check data in database 
   - `docker exec -it <POSTGRES_CONTAINER_ID> bash`
6. Connect to database with psql and zoi user created in init db
   - `psql -U zoi_user -d zoi_db`
7. Run this query to see the data
   - `select * from member;` 

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
- Avoid inserting duplicate row in table member (idempotency of emitter script is broken with considering there is multiple entries for each member)
- Change model (current model not relational because of sentence read in `Assume that each row represents a separate instance of member activity.` if it is the case we need 2 tables : 1 for members and 1 for recommendations)
- Provide documentation on how to read the alternate model (a mermaid entity relational diagram to start with)