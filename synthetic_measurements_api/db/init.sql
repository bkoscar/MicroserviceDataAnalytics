CREATE TABLE IF NOT EXISTS sensor_data (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP,
    temperature NUMERIC,
    humidity NUMERIC,
    pressure NUMERIC,
    wind_speed NUMERIC,
    wind_direction INTEGER,
    co2_levels NUMERIC,
    luminosity NUMERIC,
    failure INTEGER
);
