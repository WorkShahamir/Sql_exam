CREATE OR REPLACE FUNCTION get_course_id_by_email(p_email TEXT)
RETURNS INT AS $$
  SELECT c.id FROM courses c 
  JOIN students s ON c.id = s.course_id
  WHERE s.email = p_email;
$$ LANGUAGE SQL;
