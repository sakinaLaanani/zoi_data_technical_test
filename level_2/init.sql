\c zoi_db;     

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

CREATE USER zoi_user WITH PASSWORD 'zoi_user_pswd';

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO zoi_user;
