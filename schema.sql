CREATE TABLE churn_data (
    id SERIAL PRIMARY KEY,
    churn INT,
    tenure INT,
    monthlycharges FLOAT,
    totalcharges FLOAT
);
