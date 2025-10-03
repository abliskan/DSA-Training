# SQL Advanced Queries Notes (POSTGRESQL)
Create table
```
CREATE TABLE StoreTransactions (
    S_ID INT PRIMARY KEY,
    ID_Cabang VARCHAR(255),
    ID_Kasir VARCHAR(255),
    Total_transaksi_kasir NUMERIC(7,2),
    Total_transaksi_cabang NUMERIC(8,2)
);
```
Insert data
```
INSERT INTO StoreTransactions (S_ID, ID_Cabang, ID_Kasir, Total_transaksi_kasir, Total_transaksi_cabang)
VALUES
   (1, 'Cabang-039', '039-053', 14534.50, 145918.25),
   (2, 'Cabang-040', '040-127', 14664.40, 145755.15),
   (3, 'Cabang-041', '041-156', 14397.75, 145900.50),
   (4, 'Cabang-042', '042-212', 14626.50, 146120.25),
   (5, 'Cabang-043', '043-044', 14804.85, 145918.60);
```

## Data Data Manipulation Language (DML)

### View Statement
The following SQL creates a view from StoreTransactions:
```
CREATE VIEW per_kasir AS
    SELECT ID_Cabang,
           ID_Kasir,
           Total_transaksi_kasir,
    FROM sample_data.public.StoreTransactions;
```
Updating a view in SQL means modifying the data it shows:
```
UPDATE sample_data.public.per_kasir
SET Total_transaksi_kasir = 14590.20
WHERE ID_Cabang = 'Cabang-039';
```
The following SQL remove the per_kasir view:
```
DROP VIEW per_kasir;
```

### Store Procedure
The following SQL create a stored procedure:
```
CREATE OR REPLACE PROCEDURE public.per_kasir_cabang(IN cabang VARCHAR(16))
	LANGUAGE sql
AS $procedure$
	BEGIN
        SELECT ID_Cabang,
               ID_Kasir,
               COUNT(*) AS total_transaksi
        FROM public.StoreTransactions
        WHERE ID_Cabang = cabang
        GROUP BY 1,2;      
	END;
$procedure$
```
Execute a Stored Procedure
```
CALL public.per_kasir_cabang('Cabang-039');
```
We do the select query
```
SELECT *
FROM information_schema.parameters
WHERE SPESIFIC_NAME = 'per_kasir_cabang';
```

### Explain
- The goal is to aggregate of the total revenue and group it by order_id, order_date, customer_id, and the status of the orders
```
EXPLAIN
SELECT o.*,
    round(sum(oi.order_item_subtotal)::numeric, 2) as revenue
FROM orders as o
 JOIN order_items as oi
  ON o.order_id = oi.order_item_order_id
WHERE o.order_id = 2
GROUP BY o.order_id, o.order_date, o.order_customer_id, o.order_status;
```
Expected explain query result:
```
|QUERY PLAN                                                                             |
|---------------------------------------------------------------------------------------|
|GroupAggregate  (cost=0.29..3427.86 rows=1 width=58)                                   |
|  Group Key: o.order_id                                                                |
|  ->  Nested Loop  (cost=0.29..3427.82 rows=4 width=34)                                |
|        ->  Index Scan using orders_pkey on orders o  (cost=0.29..8.31 rows=1 width=26)|
|              Index Cond: (order_id = 2)                                               |
|        ->  Seq Scan on order_items oi  (cost=0.00..3419.47 rows=4 width=12)           |
|              Filter: (order_item_order_id = 2)     
```
- To add the actual runtime statistics to the output, you need to execute the statement using the **ANALYZE** option:
```
EXPLAIN ANALYZE
SELECT count(*)
FROM orders AS o
 JOIN order_items as oi
  ON o.order_id = oi.order_item_order_id
WHERE o.order_customer_id = 5;
```
Expected explain with analyze query result:
```
|QUERY PLAN                                                                                                                                                         |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Aggregate  (cost=53.71..53.72 rows=1 width=8) (actual time=2.434..2.435 rows=1 loops=1)                                                                            |
|  ->  Nested Loop  (cost=4.76..53.67 rows=15 width=0) (actual time=1.872..2.428 rows=7 loops=1)                                                                    |
|        ->  Bitmap Heap Scan on orders o  (cost=4.34..26.49 rows=6 width=4) (actual time=1.034..1.315 rows=4 loops=1)                                              |
|              Recheck Cond: (order_customer_id = 5)                                                                                                                |
|              Heap Blocks: exact=4                                                                                                                                 |
|              ->  Bitmap Index Scan on orders_order_customer_id_idx  (cost=0.00..4.34 rows=6 width=0) (actual time=0.696..0.696 rows=4 loops=1)                    |
|                    Index Cond: (order_customer_id = 5)                                                                                                            |
|        ->  Index Only Scan using order_items_order_item_order_id_idx on order_items oi  (cost=0.42..4.49 rows=4 width=4) (actual time=0.275..0.276 rows=2 loops=4)|
|              Index Cond: (order_item_order_id = o.order_id)                                                                                                       |
|              Heap Fetches: 0                                                                                                                                      |
|Planning Time: 5.706 ms                                                                                                                                            |
|Execution Time: 2.565 ms    
```
- This option shows how many data blocks were found in the cache (hit) for each node:
```
EXPLAIN (ANALYZE, BUFFERS)
SELECT count(*)
FROM c
WHERE pid = 1 AND cid > 200;
```
Expected explain with analyze query result:
```
|QUERY PLAN                                                                                                                                                         |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Aggregate  (cost=219.50..219.51 rows=1 width=8) (actual time=2.808..2.809 rows=1 loops=1)                                                                         |
|   Buffers: shared read=45                                                                                                                                         |
|   I/O Timings: read=0.380                                                                                                                                         |
|   ->  Seq Scan on c  (cost=0.00..195.00 rows=9800 width=0) (actual time=0.083..1.950 rows=9800 loops=1)                                                           |
|         Filter: ((cid > 200) AND (pid = 1))                                                                                                                       |
|         Rows Removed by Filter: 200                                                                                                                               |
|         Buffers: shared read=45                                                                                                                                   |
|         I/O Timings: read=0.380                                                                                                                                   | 
| Planning:                                                                                                                                                         |
|   Buffers: shared hit=48 read=29                                                                                                                                  |
|   I/O Timings: read=0.713                                                                                                                                         |
| Planning Time: 1.673 ms                                                                                                                                           |
| Execution Time: 3.096 ms                                                                                                                                          |
```

### Index
To create a index on the column title in the table films (duplicate values are not allowed)
```
CREATE UNIQUE INDEX title_idx ON films(title);
```
Show all the index 
```
SHOW INDEX FROM films;
```
This command will remove the index title_idx
```
ALTER TABLE films DROP INDEX title_idx;
```

### JOIN
- Create new table and insert data
```
CREATE TABLE ms_cabang (
    Id_cabang INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    Kode_cabang VARCHAR(255),
    Nama_cabang VARCHAR(255),
    Kode_kota VARCHAR(255)
);
 #2
CREATE TABLE ms_produk (
    Id_produk INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    Kode_produk VARCHAR(255),
    Nama_produk VARCHAR(255),
    Unit INT,
    Kode_kesatuan VARCHAR(255)
);
 #3 Join to table #1
CREATE TABLE ms_karyawan (
    Kode_cabang VARCHAR(255),
    Kode_kayawan VARCHAR(255),
    Nama_depan VARCHAR(255),
    Nama_belakang VARCHAR(255),
    Jenis_kelamin VARCHAR(255)
);
 #4 Join to table #1 and #3
CREATE TABLE tr_penjualan (
    Kode_transaksi INT,
    Tgl_transaksi VARCHAR(255),
    Kode_cabang VARCHAR(255),
    Kode_kasir VARCHAR(255),
    Kode_item VARCHAR(255),
    Kode_produk VARCHAR(255),
    Jumlah_pembelian INT
);
```

- INNER JOIN: Use when you only care about records that exist in both tables.
```
SELECT trp.Kode_transaksi,
       trp.Kode_item,
       msc.Nama_cabang,
       msc.Kode_kota
FROM ms_cabang msc
JOIN tr_penjualan trp
	ON trp.Kode_cabang = msc.Kode_cabang
```

- LEFT JOIN: Use when you want everything from the first table, even if no match in the second.
```
SELECT Kode_karyawan,
       Nama_depan,
       Jenis_kelamin
FROM ms_karyawan msk
LEFT JOIN ms_cabang msc
	ON msc.Kode_cabang = msk.Kode_cabang
```

- FULL JOIN: Use when you want to include everything from both tables.
```
SELECT *,
      COUNT (*) as jumlah_transaksi
FROM ms_produk msp
FULL JOIN tr_penjualan trp
	ON trp.Kode_produk = msp.Kode_produk
```

- JOIN MULTIPLE TABLE (3)
```
SELECT trp.Kode_transaksi,
 	   trp.Kode_kasir,
       trp.Kode_produk,
       trp.Kode_cabang,
       msp.Unit
FROM ms_cabang msc
	 JOIN tr_penjualan trp
	 	ON trp.Kode_cabang = msc.Kode_cabang
	 LEFT JOIN ms_produk msp
	    ON msp.Kode_produk = trp.Kode_produk 
WHERE trp.Kode_transaksi <= 20;
```

## Subquery
- Subquery - Column Subquery
```
SELECT *
FROM tr_penjualan trp
WHERE jumlah_pembelian IN (
	SELECT max(jumlah_pembelian) 
	FROM tr_penjualan tp
)
LIMIT 10;
```

- Subquery - Derived Subquery
```
SELECT AVG(tp.jumlah_transaksi) AS AVG_jumlah_transaksi
FROM (
	SELECT Kode_cabang,
	       COUNT(*) AS jumlah_transaksi
	FROM tr_penjualan
	GROUP BY 1
) AS tp;
```

- Lateral Subquery
```
CREATE TABLE customers (
   Cust_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
   Name VARCHAR(100)
);

INSERT INTO customers (name)
VALUES 
   ('Md. Anower Hossain'),
   ('Md. Amir Hossain'),
   ('Afjoza Sultana');

CREATE TABLE orders (
   Order_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
   Order_date TIMESTAMP,
   Customer_id INT CONSTRAINT fk_customers REFERENCES customers(Cust_id)
);

INSERT INTO orders (Order_date, Customer_id)
VALUES 
   ('2025-03-01 10:00:00', 1),
   ('2025-03-05 12:00:00', 1),
   ('2025-03-10 15:00:00', 2),
   ('2025-03-08 14:00:00', 3),
   ('2025-03-12 16:00:00', 3);

-- Solution using LATERAL Join
SELECT 
   c.Cust_id AS customer_id,
   c.Name AS customer_name,
   o.Order_id AS latest_order_id,
   o.Order_date AS latest_order_date
FROM 
   customers AS c
JOIN LATERAL (
   SELECT *
   FROM orders AS o
   WHERE o.Customer_id = c.Cust_id
   ORDER BY o.Order_date DESC
   LIMIT 1
) o ON true;
```

## CTE
- Refer to the CTE in a SELECT statement by calling the CTE name defined
```
WITH total_per_cabang AS (
		SELECT Kode_cabang,
	           count(*) AS jumlah_transaksi
		FROM tr_penjualan
		GROUP BY 1
)
SELECT AVG(jumlah_transaksi) AS avg_jumlah_transaksi
FROM total_per_cabang;
);
```

- Wrap JOIN with CTE
```
WITH OrderDetails AS (
    SELECT o.OrderID, c.CustomerName, p.Price, o.Quantity, o.OrderDate
    FROM Orders o
    JOIN Customers c ON o.CustomerID = c.CustomerID
    JOIN Products p ON o.ProductID = p.ProductID
    WHERE YEAR(o.OrderDate) = 2024
)
SELECT CustomerName, SUM(Price * Quantity) AS TotalRevenue
FROM OrderDetails
GROUP BY CustomerName
HAVING SUM(Price * Quantity) > 1000;
```

- Multiple CTEs in a single query, which allows for complex transformations and calculations
```
WITH ProductSales AS (
    -- Step 1: Calculate total sales for each product
    SELECT ProductID, SUM(SalesAmount) AS TotalSales
    FROM Sales
    GROUP BY ProductID
),
AverageSales AS (
    -- Step 2: Calculate the average total sales across all products
    SELECT AVG(TotalSales) AS AverageTotalSales
    FROM ProductSales
),
HighSalesProducts AS (
    -- Step 3: Filter products with above-average total sales
    SELECT ProductID, TotalSales
    FROM ProductSales
    WHERE TotalSales > (SELECT AverageTotalSales FROM AverageSales)
)
-- Step 4: Rank the high-sales products
SELECT ProductID, TotalSales, RANK() OVER (ORDER BY TotalSales DESC) AS SalesRank
FROM HighSalesProducts;
```

- Recursive CTE allowing the query to perform repeated operations
```
WITH EmployeeHierarchy AS (
    -- Anchor member: select the top-level manager
    SELECT EmployeeID, EmployeeName, ManagerID, 1 AS Level
    FROM Employees
    WHERE EmployeeID = 1  -- Starting with the top-level manager
    UNION ALL
    -- Recursive member: find employees who report to the current managers
    SELECT e.EmployeeID, e.EmployeeName, e.ManagerID, eh.Level + 1
    FROM Employees e
    INNER JOIN EmployeeHierarchy eh ON e.ManagerID = eh.EmployeeID
)
SELECT EmployeeID, EmployeeName, Level
FROM EmployeeHierarchy;
```
## Window Functions
- Aggregate Window Functions
```
WITH total_per_cabang AS (
	SELECT Kode_cabang,
		   COUNT(*) AS jumlah_transaksi
	FROM tr_penjualan
	GROUP 1
)
SELECT *,
       AVG(jumlah_transaksi) OVER() AS avg_transaksi
FROM total_per_cabang;
```

- Ranking Window Functions
1. Type1,2,3 (ROW_NUM, RANK, DENSE_RANK)
```
WITH total_per_cabang AS (
	SELECT CAST(Tgl_transaksi AS date) AS Bulan,
	       COUNT(*) AS jumlah_transaksi
	FROM tr_penjualan
	GROUP BY 1
)
SELECT *,
      ROW_NUMBER() OVER(ORDER BY jumlah_transaksi DESC) AS row_num_transaksi,
	  RANK() OVER(ORDER BY jumlah_transaksi DESC) AS rank_transaksi,
	  DENSE_RANK() OVER(ORDER BY jumlah_transaksi DESC) AS dense_rank_transaksi
FROM total_per_cabang;
```

2. Type4 (NTILE)
```
WITH total_per_cabang AS (
	SELECT CAST(Tgl_transaksi AS date) AS Bulan,
	       Kode_kasir,
		   COUNT(*) AS jumlah_transaksi
	FROM tr_penjualan
	GROUP BY 1, 2
)
SELECT *,
      NTILE(1) OVER(PARTITION BY Kode_kasir ORDER BY Bulan)
FROM total_per_cabang;
```

- Value Window Functions
