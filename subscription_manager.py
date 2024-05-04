import pymysql
import json
from typing import Optional, List
from dataclasses import dataclass

with open('config_prod.json') as config_file:
    config = json.load(config_file)

@dataclass
class Subscription:
    chat_id: str
    region: str
    area: str
    enable_notifications: bool
    culture: str

def get_db_connection():
    connection = pymysql.connect(host=config['database']['host'],
                                 user=config['database']['user_name'],
                                 password=config['database']['password'],
                                 database=config['database']['database_name'],
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection

def add_subscription(chat_id: str, region: str, area: str, enable_notifications: bool = True, culture: str = 'en-CH') -> Subscription:
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO subscription (ChatId, Region, Area, EnableServiceNotifications, Culture) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (chat_id, region, area, enable_notifications, culture))
        connection.commit()
    finally:
        connection.close()
    return Subscription(chat_id, region, area, enable_notifications, culture)

def get_subscriptions() -> List[Subscription]:
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM subscription"
            cursor.execute(sql)
            result = cursor.fetchall()
            return [Subscription(**row) for row in result]
    finally:
        connection.close()

def update_subscription(chat_id: str, region: Optional[str] = None, area: Optional[str] = None, enable_notifications: Optional[bool] = None, culture: Optional[str] = None) -> Optional[Subscription]:
    connection = get_db_connection()
    updates = []
    parameters = []

    if region is not None:
        updates.append("Region = %s")
        parameters.append(region)
    if area is not None:
        updates.append("Area = %s")
        parameters.append(area)
    if enable_notifications is not None:
        updates.append("EnableServiceNotifications = %s")
        parameters.append(enable_notifications)
    if culture is not None:
        updates.append("Culture = %s")
        parameters.append(culture)

    if updates:
        parameters.append(chat_id)
        sql_update = ", ".join(updates)
        sql = f"UPDATE subscription SET {sql_update} WHERE ChatId = %s"

        try:
            with connection.cursor() as cursor:
                cursor.execute(sql, tuple(parameters))
                connection.commit()
        finally:
            connection.close()

        return get_subscription_by_chat_id(chat_id)
    return None

def get_subscription_by_chat_id(chat_id: str) -> Optional[Subscription]:
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM subscription WHERE ChatId = %s"
            cursor.execute(sql, (chat_id,))
            result = cursor.fetchone()
            if result:
                return Subscription(**result)
    finally:
        connection.close()
    return None

def delete_subscription(chat_id: str) -> None:
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM subscription WHERE ChatId = %s"
            cursor.execute(sql, (chat_id,))
        connection.commit()
    finally:
        connection.close()
