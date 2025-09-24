# SQL Advanced Queries Notes
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
