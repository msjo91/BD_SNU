/* Followed after basics_schema2.sql */

/* Create view cs_student of Comp. Sci students */
create or replace view cs_student as
select s.* from student s natural join department where dept_name='컴퓨터공학과';

/* Create view Aplus_students of grade A+ students */
create or replace view Aplus_students as
select distinct stu_id, name, dept_id from student natural join takes where grade = 'A+';

/* The names of Aplus_students */
select name from Aplus_students;

/* The number of A+ students in each department */
select dept_id, count(*) from Aplus_students natural right outer join department group by dept_id;

/* Create view Aplus_students of grade A+ students and the number of A+s each student has */
create or replace view Aplus_students as
select distinct stu_id, name, dept_id, count(grade) num_Aplus from student natural join takes where grade = 'A+' group by stu_id;

/* The number of A+ students and A+s in each department */
select dept_id, count(*), sum(num_Aplus) from Aplus_students natural right outer join department group by dept_id;