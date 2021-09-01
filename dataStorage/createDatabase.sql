CREATE DATABASE altpapierBot;

use altpapierBot;

CREATE TABLE userData (
    ChatId VARCHAR(255) NOT NULL,
    ZipCode SMALLINT NULL,
    AreaCode VARCHAR(7) NULL
);

CREATE TABLE bebbiBotUserData (
    ChatId VARCHAR(255) NOT NULL,
    AreaCode VARCHAR(7) NULL
);