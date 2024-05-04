CREATE DATABASE altpapierBot;

use altpapierBot;

CREATE TABLE subscription (
    ChatId VARCHAR(255) NOT NULL,
    Region VARCHAR(20) NOT NULL,
    Area VARCHAR(5) NOT NULL,
    EnableServiceNotifications BOOLEAN NOT NULL DEFAULT 1,
    Culture VARCHAR(5) NOT NULL DEFAULT 'en-CH'
);