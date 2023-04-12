SELECT 
  c.language AS language,
  SUM(p.amount) AS sum_amount
FROM 
  payments p
  JOIN courses c ON p.course_id = c.id
GROUP BY 
  c.language;
