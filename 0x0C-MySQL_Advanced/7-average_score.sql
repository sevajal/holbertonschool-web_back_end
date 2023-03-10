-- Creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student.
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(arg_user_id int)
BEGIN SET @average = (SELECT AVG(score) FROM corrections GROUP BY user_id HAVING user_id = arg_user_id);
UPDATE users SET average_score = @average WHERE id = arg_user_id;
END $$
DELIMITER;
