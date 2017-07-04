/*
Aggregated function
    Placed after select
        select count(<field>)
        select sum(<field>)
        select avg(<field>)
        select max(<field>)
        select min(<field>)
*/

/* Followed after basics_schema2.sql */

/* count : Return the number of records */
select count(*) from student where year = 3;    # The number of junior students
select count(distinct dept_id) from student;    # The number of departments (without redundancy)
select count(*) from student s, department d where s.dept_id=d.dept_id and d.dept_name='컴퓨터공학과';    # The number of Comp. Sci major students

/* sum : Return the total of records */
select sum(year_emp) from professor;    # The total of professors' employeed years

/* avg: Return the average of records */
select avg(year_emp) from professor;    # The average of professors' employeed years

/* max: Return the largest value of records (string allowed) */
select name, max(grade) from student s, takes t where s.stu_id=t.stu_id group by name;    # The student names and their hightest grades

/* min : Return the smallest value of records (string allowed) */
select title, name, min(grade) from student s, takes t, class cl, course co where s.stu_id=t.stu_id and t.class_id=cl.class_id and cl.course_id=co.course_id group by title, name; 
# The lowest graded students and their grades in each class

/* group  by : Group and edit the output */
select dept_id, count(*) from student group by dept_id;    # The number of students in each department

/* having : Filter grouped output */
select dept_name, count(*), avg(year_emp), max(year_emp) from professor p, department d where p.dept_id=d.dept_id group by dept_name having avg(year_emp) >= 2000;
# The number of professors, average employeed year, latest employ of departments whose average employeed year is equal to or the same as 2000