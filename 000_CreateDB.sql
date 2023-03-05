CREATE DATABASE users;
USE users;
CREATE TABLE IF NOT EXISTS user_info (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    dob DATETIME NOT NULL,
    gender VARCHAR(255) NOT NULL,
    name_character_count INT NOT NULL,
    UNIQUE INDEX unique_user_info (first_name, last_name, dob)
);