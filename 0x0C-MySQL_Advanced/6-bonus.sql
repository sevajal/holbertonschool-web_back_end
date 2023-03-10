-- Creates a stored procedure AddBonus that adds a new correction for a student.
DELIMITER $$
CREATE PROCEDURE AddBonus (user_id int, project_name varchar(255), score int)
BEGIN SET @project_id = (SELECT id FROM projects WHERE name = project_name);
    IF @project_id IS NULL THEN
        INSERT INTO projects(name) VALUES (project_name);
        SET @project_id = (SELECT id FROM projects WHERE name = project_name);
    END IF;
INSERT INTO corrections(user_id, project_id, score) VALUES (user_id, @project_id, score);
END $$
DELIMITER;
