---
tags: Data Infrastructure
description: Connect to SQL or NoSQL databases to query, store, and manage structured data.
---
# Database Integration

The Database Integration allows you to connect your AI-generated applications to real databases, automatically generating schemas and enabling data-driven functionality.

```python exec
import reflex as rx
from reflex_image_zoom import image_zoom
```

```python eval
rx.el.div(
    image_zoom(
        rx.image(
            src=rx.color_mode_cond(
                "/ai_builder/integrations/database_light.webp",
                "/ai_builder/integrations/database_dark.webp",
            ),
            class_name="p-2 rounded-md h-auto",
            border=f"0.81px solid {rx.color('slate', 5)}",
        ),
        class_name="rounded-md overflow-hidden",
    ),
    class_name="w-full flex flex-col rounded-md cursor-pointer",
)
```

## Supported Databases

- **PostgreSQL** - Recommended for production applications
- **MySQL** - Popular open-source database
- **SQLite** - Lightweight database, perfect for development and small applications

## Getting Started

### Opening the Database Integration

1. Navigate to your app in the AI Builder
2. Open the **Settings drawer** (gear icon)
3. Click on the **Integrations** tab
4. Find and enable the **Database** integration

### Connection Methods

The Database Integration offers two convenient ways to connect:

#### 1. Connection Details (Recommended)

This user-friendly form breaks down your database connection into individual fields:

**For PostgreSQL and MySQL:**
- **Database Type**: Select from dropdown (PostgreSQL/MySQL)
- **Hostname**: Your database server address (e.g., `localhost`, `db.company.com`)
- **Port**: Automatically filled (PostgreSQL: 5432, MySQL: 3306) or specify custom port
- **Username**: Your database username
- **Password**: Your database password (securely handled)
- **Database Name**: The specific database to connect to

**For SQLite:**
- **Database Type**: Select "SQLite" from dropdown
- **SQLite Download URL**: Either a local file path or HTTP URL to download the database file

#### 2. Database URI

For advanced users who prefer the traditional connection string format:

**PostgreSQL:**
```
postgresql://username:password@hostname:port/database_name
```

**MySQL:**
```
mysql://username:password@hostname:port/database_name
```

**SQLite:**
```
sqlite:///path/to/database.sqlite
sqlite+https://example.com/database.sqlite
```

## Database URI Components

Protocol (postgresql://) - Database type identifier
Username (admin) - Database user credentials
Password (secret123) - User password (kept secure)
Hostname (db.company.com) - Server address
Port (5432) - Connection port
Database (mydatabase) - Target database name

## Connection Process

1. **Choose your method**: Use either Connection Details form or Database URI
2. **Fill in credentials**: Provide your database connection information
3. **Click Connect**: The system will validate and test your connection
4. **Schema Generation**: Upon successful connection, the system automatically:
   - Connects to your database
   - Analyzes the database structure
   - Generates SQLAlchemy models
   - Makes schema available to the AI for queries


```md alert
# NoSQL Databases

NoSQL databases (e.g., MongoDB, DynamoDB) can be accessed via Python SDKs which the AI Builder can install if you prompt for it. The first class Database integration currently supports only SQL databases.
```