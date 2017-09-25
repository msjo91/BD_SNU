/* Followed after basics_schema2.sql */
/* Open another transaction to use locking_t1.sql and locking_t3.sql */
/* Transaction 2 for lock */

/* Implicit lock */
/* Update a record while on lock */
UPDATE employee SET rank = 'CEO' WHERE ename = '김광성';

/* Explicit lock */
/* Get a table while on write lock */
SELECT * FROM student;

/* Name lock */
/* See if lock name is free to use */
/* 1: free, 0: taken */
SELECT IS_FREE_LOCK('locklock');
/* Create a lock with the same name while is taken */
/* 1: success, 0: taken */
SELECT GET_LOCK('locklock', 10);
/* Relase name lock while lock not created in current transaction */
/* 1: released, 0: lock is not established in current thread */
SELECT RELEASE_LOCK('locklock');