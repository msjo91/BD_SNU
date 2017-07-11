/* Followed after basics_schema2.sql */

/* Q1 */
/* The names of professors whose names are the same to the students' */
select p.name from professor p, student s where p.name = s.name;

/* Q2 */
/* Ascending order of course_id which both Ind. Sci students and Comp. Sci students took without redundancy */
select distinct course_id from class where course_id in (
    select course_id from class c, takes t, student s, department d
    where c.class_id = t.class_id and t.stu_id = s.stu_id and s.dept_id = d.dept_id and dept_name = '산업공학과'
)
and course_id in (
    select course_id from class c, takes t, student s, department d
    where c.class_id = t.class_id and t.stu_id = s.stu_id and s.dept_id = d.dept_id and dept_name = '컴퓨터공학과'
)
order by course_id;

/* Q3 */
/* The department names, names and course titles of students whose names are '광식' */
select dept_name, name, title from department d, student s, takes t, class cl, course co
where d.dept_id = s.dept_id and s.stu_id = t.stu_id and t.class_id = cl.class_id and cl.course_id = co.course_id and name like '%광식';

/* Q4 */
/* The name and years of employment of professors who were employeed later than '최성희' */
select name, (2017 - year_emp) from professor where year_emp > (select year_emp from professor where name='최성희');

/* Q5 */
/* The names, class ids and grades of students (even those who never took a class in ascending order of name */
select name, class_id, grade from student natural left outer join takes ordery by name;

/* Q6 */
/* The professor ids and names of professors paired with the student ids and names of students with the same names also names without pairs */
select prof_id, p.name, stu_id, s.name from professor p left outer join student s using (name)
union
select prof_id, p.name, stu_id, s.name from professor p right outer join student s using (name);

/* Q7 */
/* Ascending order of department names with the number of registered students */
select  dept_name, count(stu_id) from department d, student s where d.dept_id = s.dept_id group by dept_name order by dept_name;

/* Q8 */
/* The names, course ids and grades of students with grade above 'B' */
select name, class_id, grade from student s, takes t where s.stu_id = t.stu_id and grade <= 'B+';

/* Q9 */
/* The names of students with two or more 'B' grades or higher and the number of classes they received such grades */
select name, count(class_id) from student s, takes t where s.stu_id = t.stu_id and grade <= 'B+' group by name having count(class_id) >= 2;

/* Q10 */
/* The ranks and average salary of employees in ascending order of ranks */
select rank, avg(sal) from employee group by rank order by rank;

/* Q11 */
/* The names and income (salary + commission) of employees (commission = salary * bonus / 100 */
select ename, (sal + (sal * bonus / 100)) from employee;

/* Q12 */
/* The names and income of departments whose income is above 14000 in ascending order of name */
select dept_name, sum(sal + (sal * bonus / 100)) from department d, employee e where d.dept_id = e.dept_id group by dept_name having sum(sal + (sal * bonus / 100)) > 14000;

/* Q13 */
/* The names and average income of departments whose the average income of '사원' is greater than 3300 in ascedning order of department name */
select dept_name, avg(sal + (sal * bonus / 100)) from department d, employee e where d.dept_id = e.dept_id and rank = '사원'
group by dept_name having avg(sal + (sal * bonus / 100)) > 3300 order by dept_name;

/* Q14 */
/* The grades and frequency of each grade in ascending string order of grade (A -> A + -> B ...) */
select grade, count(grade) from takes group by grade order by grade;

/* Q15 */
/* The grades and frequency of each grade in descending frequency order and ascending string order if the frequencies are the same */
select grade, count(grade) from takes group by grade order by count(grade) desc, grade;

/* Q16 */
/* A pair tuple of students for each year of student without redundancy and the left person having a smaller student id */
select s1.stu_id, s2.stu_id from student s1, student s2 where s1.year = s2.year and s1.stu_id < s2.stu_id;

/* Q17 */
/* The names of students whose names are the same as the professors' (Use nested query) */
select name from student where name in (select name from professor);

/* Q18 */
/* Ascending order of course_id which both Ind. Sci students and Comp. Sci students took without redundancy (Use nested query) */
select distinct course_id from class where course_id in (
    select course_id from class c, takes t, student s, department d
    where c.class_id = t.class_id and t.stu_id = s.stu_id and s.dept_id = d.dept_id and dept_name = '산업공학과'
)
and course_id in (
    select course_id from class c, takes t, student s, department d
    where c.class_id = t.class_id and t.stu_id = s.stu_id and s.dept_id = d.dept_id and dept_name = '컴퓨터공학과'
)
order by course_id;

/* Q19 */
/* The student ids of students who received 'A+' and 'C' in 2012 (Use nested query) */
select distinct stu_id from takes where stu_id in (
    select stu_id from takes where grade = 'A+'
)
and stu_id in (
    select stu_id from takes where grade = 'C'
)
and class_id in (
    select class_id from class where year = 2012
);

/* Q20 */
/* The names of employees who work in Comp. Sci department and have salary higher than that of Ind. Sci employees (Use nested query) */
select ename from employee where dept_id in 
(
    select dept_id from department where dept_name = '컴퓨터공학과'
)
and sal >= all (
    select sal from employee where dept_id in (
        select dept_id from department where dept_name = '산업공학과'
    )
);