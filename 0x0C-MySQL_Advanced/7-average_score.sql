-- Creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student.
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(user_id int)
BEGIN SET @average = (SELECT AVG(score) FROM corrections GROUP BY user_id HAVING user_id = user_id);
UPDATE users SET average_score = @average WHERE id = user_id;
END $$
DELIMITER;
