CREATE TABLE users (
    ID SERIAL PRIMARY KEY, 
    name TEXT, 
    password TEXT
);
CREATE TABLE events (
    ID SERIAL PRIMARY KEY, 
    name TEXT, 
    date DATE, 
    description TEXT, 
    type INT, 
    open INT,
    user_id INT REFERENCES users
);
CREATE TABLE participants (
    ID SERIAL PRIMARY KEY,
    event_id INT REFERENCES events,
    user_id INT REFERENCES users
);