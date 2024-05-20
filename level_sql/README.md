# Level SQL

### How to

0. Install docker
Then at the root level of the project :
1. Build docker image
   - `docker-compose build`
2. Start docker
   - `docker-compose up -d`
3. Run emitter script 
   - `python member_data_emitter.py`
5. Copy file containing queries to docker container
   - `docker cp level_sql/queries.sql <POSTGRES_CONTAINER_ID>:/tmp`
6. Check database 
   - `docker exec -it <POSTGRES_CONTAINER_ID> bash`
7. Connect to database with psql and zoi user created in init db
   - `psql -U zoi_user -d zoi_db`
8. Run queries against database with psql and zoi user
   - `psql -U zoi_user -d zoi_db -f /tmp/queries.sql`

### Improvments ideas
- Manage queries in transactions

