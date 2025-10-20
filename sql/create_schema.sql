CREATE TABLE waiting_list_data (
    id SERIAL PRIMARY KEY,
    region_code VARCHAR(10),
    servicio_salud VARCHAR(100),
    specialty_name VARCHAR(100),
    median_wait_days INT,
    patients_waiting INT,
    record_date DATE
);
