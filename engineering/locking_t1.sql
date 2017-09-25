/* Followed after basics_schema2.sql */
/* Open another transaction to use locking_t2.sql and locking_t3.sql */
/* Transaction 1 for lock */

/* Implicit lock */
/* Cause a lock by reading after 50 sec */
SELECT * FROM employee WHERE SLEEP(20);

/* Explicit lock */
/* Exclusive lock a table */
LOCK TABLES student WRITE;
/* Update record */
UPDATE student SET address = 'NYC'  WHERE stu_id = 1292001;

/* Name lock */
/* Create a lock with timeout */
/* 1: success, 0: taken */
SELECT GET_LOCK('locklock', 10);
/* Relase name lock */
/* 1: released, 0: lock is not established in current thread */
SELECT RELEASE_LOCK('locklock');

/* See process */
SHOW PROCESSLIST;

/* Unlock table */
UNLOCK TABLES;