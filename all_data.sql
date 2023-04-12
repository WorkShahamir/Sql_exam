SELECT 
  c.name AS course_name,
  c.start_date AS course_start_date,
  CONCAT(s.first_name, ' ', s.last_name) AS student_name,
  CONCAT(m.first_name, ' ', m.last_name) AS mentor_name,
  c.language AS course_language
FROM 
  courses c 
  JOIN students s ON c.id = s.course_id 
  JOIN mentors m ON c.mentor_id = m.id;
