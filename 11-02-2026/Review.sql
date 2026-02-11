
USE LMSDATABASE;

SELECT 
	u.user_id,
	l.lesson_id,
	l.title AS Lesson_Title,
	c.title AS Course_Name
FROM lms.users u
JOIN lms.Courses c
ON u.user_id = c.user_id
JOIN lms.Lessons l
ON c.course_id = l.course_id
ORDER BY u.user_id;


SELECT 
	u.user_id,
	a.title AS Assessment_Title,
	s.submitted_at
FROM lms.Users u
JOIN lms.AssessmentSubmission s
ON u.user_id = s.user_id
JOIN lms.Assesments a
ON a.assessment_id = s.assessment_id
ORDER BY u.user_id;


SELECT
	DISTINCT u.user_id,
    c.course_id,
    c.title,
	s.score
FROM lms.Courses c
JOIN lms.Assesments a
ON c.course_id = a.course_id
JOIN lms.Users u 
ON u.user_id = c.user_id
JOIN lms.AssessmentSubmission s
ON a.assessment_id = s.assessment_id
ORDER BY u.user_id;
