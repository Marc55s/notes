
- Docker copy
```bash
    docker cp file container:/file
```
Import:
    mariadb -u root -p dbname < /dump.sql
- SQL
- Insert
    ```sql
    insert into [table_name] (col1, col2) values(val1, val2);
    ```
- Update (Prozessabbildung)
    ```sql
    update [table_name] set col1 = val1 where id = 1; 
    ```
- Delete
    ```sql
    delete from [table_name] where id = 1;
    ```
- Join
- Inner Join
    ```sql
    select fr.id as fruit_id, fr.name as fruit_name, fr.seasonality, fi.filename
    from fruits as fr
    inner join fruit_images as fi
    on fruit_id = fi.fruit_id
    limit 3;  
    ```
- Left Join
    - Returns all rows from the left table and the matching rows from the right table.
    - If not match exists, NULL is returned for columns of the right table
- Right Join
    - Returns all rows from the right table  and the matching rows from the left table
    - If no match exists, NULL is returned for columns of the left table
- Full outer Join
    - Combines left and right join
- Subqueries
    - Subqueries are queries nested inside another query
    - Dynamically compute values
    - Can be use in Select, From, Where
    - Prefer joins
    - Use aliases
    - Subqueries can return single or multiple values
    - Usual Use cases
        - Select Type
            - Returns a single value
            - nested for loop
            - `SELECT`clause are used when you need to compute a value for each row in the result set dynamically 
        - From
            - Filter from a sub table set
            - are used to create temporary tables for the main query to process
        - Where
            - More complex conditions
            - Filter results based on values retrieved by another query
            - Example: Get employees which have more than the average salary
        - 
- Procedures
- What is a store procedure?
    - A stored procedure is a set of SQL statements stored in the database tat can be executed as a single unit
    - Purpose
        - Encapsulate reusable logic
        - Improve performance by reducing network traffic
- Syntax
    ```sql
    create procedure GetAllUsers()
    begin
    select * from users;
    end;  

    -- call
    call GetAllUsers();
    ```
- Delimiter
    ```sql
    DELIMITER //
    --write code
    //
    DELIMITER ; 
    ```
- Normalization
    - Normalization is the process of structuring a relational databae in accordance with a series of normal forms
    - First normal Form(1NF)
        - Rule
            - Each column holds atomix values
        - Key criteria
            - No mulit-valued attributes Each column contains a single value
    - Second normal Form(2NF)
        - Rule
            - Table must be 1NF
            - Full functional dependency on the entire primary key
    - Third Normal Form(3NF)
        - Table must be 2NF
        - No transitive dependencies (non-key columns depending on other non-key columns)
- Defining Relationship and constraints
    - Constraints
        - primary key(id)
        - foreign key(id in table) references foreign_table(id_of_table)
        - cascading
            - delete
                - automatically deletes rows in a foreign key table
        - not null
        - unique
        - check
        - default
- Transactions and ACID properties
    - Transaction→A transaction is a unit of work that is performed against a database. It contains one or more SQL operations
    - Is used to ensure data consistency
    - to handle errors
    - Syntax
        ```sql
        start transaction;
        SQL statement1;
        SQL statement2;

        savepoint update_stock; 
        -- either rollback to OR use commit to enclose a transaction
        rollback to update_stock; 

        commit;  
        ```
    - ACID principles
        - Atomicity
            - Entire transaction succeeds or fails
        - Consistency
            - Data remains in a valid state
        - Isolation
            - Transactions do not affect each other
        - Durability
            - Changes persist even after a crash
