CREATE TABLE IF NOT EXISTS fakedata (id serial PRIMARY KEY, num integer, data varchar);
INSERT INTO fakedata (num, data) VALUES (100, 'toto');
SELECT * FROM fakedata;