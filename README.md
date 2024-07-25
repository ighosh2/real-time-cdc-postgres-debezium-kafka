
**Project Name**

Real-Time Change Data Capture for Postgres Using Debezium and Kafka

------------------------------------------------------------------------------------------------
**Abstract of Project**

This project implements a Change Data Capture (CDC) architecture to track changes in a 
Postgres database in real-time. The architecture leverages Docker, Debezium, Kafka, and
Apache Zookeeper to capture, stream, and manage data changes efficiently. By capturing database 
changes as they occur, organizations can ensure that their data pipelines and downstream systems
are always up-to-date, enabling more responsive and accurate data processing and analytics.

-------------------------------------------------------------------------------------------------

What Are We Trying to Solve

In many organizations, maintaining up-to-date data across multiple systems is crucial but challenging. Traditional batch processing methods can lead to delays, inconsistencies, and outdated data in downstream applications. This project aims to solve these issues by implementing a real-time data capture and streaming architecture. The goal is to minimize latency, reduce the risk of data inconsistencies, and provide a reliable way to propagate database changes instantly to other systems.


-------------------------------------------------------------------------------------------------

Use Case Which Can Benefit on Implementation in Organizations
Organizations across various industries can benefit from implementing this CDC architecture, particularly those requiring real-time data synchronization, such as:

E-commerce Platforms: Keeping inventory levels and product information up-to-date across multiple sales channels.
Financial Institutions: Ensuring real-time updates of transaction data for fraud detection, risk management, and reporting.
Healthcare Providers: Synchronizing patient records and treatment data across different systems to provide accurate and timely care.
Logistics and Supply Chain Management: Maintaining real-time visibility of shipment status and inventory levels across various locations.


-------------------------------------------------------------------------------------------------

Libraries Used:
faker: Used to generate fake data such as user profiles, cities, countries, etc.
psycopg2: A PostgreSQL adapter for Python to interact with the Postgres database.
datetime: For handling timestamp data.
random: To generate random values for transaction attributes.


-------------------------------------------------------------------------------------------------

Technology Used and Why

Docker:

Why: Containerization ensures each component of the CDC architecture runs in an isolated environment, improving manageability, scalability, and deployment consistency.
Usage: Containerizes all components, including Postgres, Debezium, Kafka, and Zookeeper, allowing them to run independently and cohesively.
Postgres (PostgreSQL):

Why: A reliable, robust, and feature-rich relational database management system widely used in various applications.
Usage: Serves as the primary database where client transactions are stored and changes are monitored.
Debezium:

Why: Provides a comprehensive and reliable solution for capturing database changes in real-time, supporting various databases, including Postgres.
Usage: Monitors the Postgres database for any changes (inserts, updates, deletes) and streams these changes to Kafka.
Kafka (Apache Kafka):

Why: A highly scalable and fault-tolerant distributed streaming platform ideal for handling high volumes of data streams.
Usage: Acts as the central messaging system that receives changes captured by Debezium and distributes them to various consumers.
Apache Zookeeper:

Why: Essential for managing and coordinating Kafka brokers, ensuring smooth operation and configuration management of the Kafka cluster.
Usage: Manages Kafka broker configurations, synchronization, and and naming services.


