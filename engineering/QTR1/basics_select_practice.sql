/* Followed after basics.sql */

/* select, distinct(no repetition), order by */
select address from student;
select distinct address from student;
select address from student order by address;
select distinct address from student order by address;

/* select fields (= attributes, columns)*/
select name, 2012-year_emp from professor order by name;
select name, 2012-year_emp years from professor order by years;

/* cartesian product and aliasing*/
select * from student s, department d where s.dept_id = d.dept_id;

/* Find the student id of junior students in comp.sci dept */
select stu_id from student s, department d where s.dept_id = d.dept_id and dept_name = '컴퓨터공학과' and year = 3;

/* desc ordering and ordering within ordering */
select name, stu_id from student order by name desc, stu_id;

/* Find name and address of students with the same name */
select s1.name, s1.address, s2.name, s2.address from student s1, student s2 where s1.name = s2.name and s1.stu_id > s2.stu_id;

/* Find a speicific student's classes which the student received an A+ */ 
select title from student s, takes t, class cl, course co where s.stu_id = t.stu_id and t.class_id = cl.class_id and cl.course_id = co.course_id and  s.name='김광식' and grade='A+';

/* LIKE operator */
select * from student where name like '김%';
select * from student where resident_id like '%-2%';

/* null search */
select * from takes where grade is null;
select * from takes where grade is not null;
select stu_id from takes where grade is null;