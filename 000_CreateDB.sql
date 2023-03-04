CREATE DATABASE users;

USE users;

CREATE TABLE user_info(
    id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    dob DATE NOT NULL,
    gender ENUM('male', 'female') NOT NULL,
    name_character_count INT NOT NULL,
    PRIMARY KEY (id)
);
