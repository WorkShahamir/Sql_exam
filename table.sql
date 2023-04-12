CREATE TABLE payments (
  id SERIAL PRIMARY KEY,
  course_id INT REFERENCES courses(id),
  amount INT NOT NULL,
  pay_date DATE NOT NULL
);

INSERT INTO payments (course_id, amount, pay_date)
VALUES (
  (SELECT get_course_id_by_email('aman@mail.ru')),
  15000,
  '2022-08-15'
),
(
  (SELECT get_course_id_by_email('aapina@bk.ru')),
  55000,
  '2022-08-05'
),
(
  (SELECT get_course_id_by_email('spencer@microsoft.com')),
  5000,
  '2022-08-25'
);
