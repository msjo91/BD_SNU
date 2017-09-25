/* Followed after basics_schema2.sql */
/* Open another transaction to use locking_t1.sql and locking_t2.sql */
/* Transaction 1 for lock */

/* Implicit lock */
/* Get 5 records while on lock */
SELECT * FROM employee LIMIT 5;