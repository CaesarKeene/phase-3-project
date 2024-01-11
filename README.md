# Phase 3 Project 
## Description 
This is a inventory management system where users can add, update, and delete items in their inventory. 
#### ERM Diagram
     +-----------------+      +-----------------+
     |    Category     |      |    Supplier     |
     +-----------------+      +-----------------+
     | id              |      | id              |
     | name            |      | name            |
     +-----------------+      +-----------------+
              |                           |
              |                           |
              |                           |
              |                           |
     +-----------------+      +-----------------+
     |      Item       |      |    Category     |
     +-----------------+      +-----------------+
     | id              |      | id              |
     | name            |      | name            |
     | category_id     |<-----|                 |
     | supplier_id     |<-----|                 |
     +-----------------+      |                 |
                              +-----------------+


## Technologies Used
1. Git 
2. SQL Alchemy 
3. Python
4. SQL
5. Alembic
### Author & License 
'CaesarKeene'
