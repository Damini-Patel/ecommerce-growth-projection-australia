--Create table for ecommerce data
CREATE TABLE ecomau (
id SERIAL PRIMARY KEY,
date VARCHAR,
year VARCHAR,
month VARCHAR,
online_food_turnover FLOAT,
online_nonfood_turnover FLOAT,
online_total_turnover FLOAT,
total_revenue_turnover FLOAT
);

CREATE TABLE precovid (
id SERIAL PRIMARY KEY,
date VARCHAR,
year VARCHAR,
month VARCHAR,
online_food_turnover FLOAT,
online_nonfood_turnover FLOAT,
online_total_turnover FLOAT,
total_revenue_turnover FLOAT
);

CREATE TABLE postcovid (
id SERIAL PRIMARY KEY,
date VARCHAR,
year VARCHAR,
month VARCHAR,
online_food_turnover FLOAT,
online_nonfood_turnover FLOAT,
online_total_turnover FLOAT,
total_revenue_turnover FLOAT
);

CREATE TABLE ecommerce (
id SERIAL PRIMARY KEY,
date VARCHAR,
year VARCHAR,
month VARCHAR,
online_food_turnover FLOAT,
online_nonfood_turnover FLOAT,
online_total_turnover FLOAT,
total_revenue_turnover FLOAT
);