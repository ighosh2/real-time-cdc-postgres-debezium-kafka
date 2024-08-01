import faker
import psycopg2
from datetime import datetime
import random

fake = faker.Faker()

def generate_transaction():
    user = fake.simple_profile()

    return {
        "productId": fake.uuid4(),
        "userId": user['username'],
        "timestamp": datetime.utcnow().timestamp(),
        "amount": round(random.uniform(10, 1000), 2),
        "currency": random.choice(['USD', 'GBP']),
        'city': fake.city(),
        "country": fake.country(),
        "merchantName": fake.company(),
        "paymentMethod": random.choice(['credit_card', 'debit_card', 'online_transfer']),
        "ipAddress": fake.ipv4(),
        "voucherCode": random.choice(['', 'DISCOUNT10', '']),
        'affiliateId': fake.uuid4()
    }

def create_table(conn):
    with conn.cursor() as cursor:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS retail_transaction_info (
                product_id VARCHAR(255) PRIMARY KEY,
                user_id VARCHAR(255),
                timestamp TIMESTAMP,
                amount DECIMAL,
                currency VARCHAR(255),
                city VARCHAR(255),
                country VARCHAR(255),
                merchant_name VARCHAR(255),
                payment_method VARCHAR(255),
                ip_address VARCHAR(255),
                voucher_code VARCHAR(255),
                affiliate_id VARCHAR(255)
            )
            """
        )
    conn.commit()

def insert_transaction(conn, transaction):
    with conn.cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO retail_transaction_info (
                product_id, user_id, timestamp, amount, currency, city, country, merchant_name, payment_method, 
                ip_address, affiliate_id, voucher_code
            ) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                transaction["productId"],
                transaction["userId"],
                datetime.fromtimestamp(transaction["timestamp"]).strftime('%Y-%m-%d %H:%M:%S'),
                transaction["amount"],
                transaction["currency"],
                transaction["city"],
                transaction["country"],
                transaction["merchantName"],
                transaction["paymentMethod"],
                transaction["ipAddress"],
                transaction["affiliateId"],
                transaction["voucherCode"]
            )
        )
    conn.commit()

if __name__ == "__main__":
    conn = None
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='retail_info_db',
            user='postgres',
            password='postgres',
            port=5433
        )
        print("Connection successful")
        
        create_table(conn)
        
        transaction = generate_transaction()
        print(transaction)
        
        insert_transaction(conn, transaction)
        
    except psycopg2.OperationalError as e:
        print(f"Connection failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()
