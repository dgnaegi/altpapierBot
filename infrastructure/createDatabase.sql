CREATE DATABASE altpapierBot;

use altpapierBot;

CREATE TABLE subscription (
    chat_id VARCHAR(255) NOT NULL,
    region VARCHAR(20) NOT NULL,
    area VARCHAR(5) NOT NULL,
    enable_service_notifications BOOLEAN NOT NULL DEFAULT 1,
    culture VARCHAR(5) NOT NULL DEFAULT 'en-CH'
);