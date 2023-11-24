CREATE DATABASE user_scores;

USE user_scores;

CREATE TABLE quiz_scores(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nickname VARCHAR(25) NOT NULL CHECK (CHAR_LENGTH(nickname) BETWEEN 3 AND 25) UNIQUE,
    SCORE INT NOT NULL CHECK (score BETWEEN 1 AND 10)
);

-- View for top 10 scores
CREATE VIEW top_scores_view AS
SELECT id, nickname, score
FROM quiz_scores
ORDER BY score DESC
LIMIT 10;

-- Stored procedure to add data to user_scores
DELIMITER //

CREATE PROCEDURE AddUserScore(IN input_nickname VARCHAR(25), IN input_score INT)
BEGIN
    INSERT INTO quiz_scores (nickname, score) VALUES (input_nickname, input_score);
END //

DELIMITER ;

-- fake starting data
CALL AddUserScore('user1', 5);
CALL AddUserScore('user2', 8);
CALL AddUserScore('user3', 3);
CALL AddUserScore('user4', 9);
CALL AddUserScore('user5', 2);
CALL AddUserScore('user6', 7);
CALL AddUserScore('user7', 4);
CALL AddUserScore('user8', 6);
CALL AddUserScore('user9', 10);
CALL AddUserScore('user10', 1);
CALL AddUserScore('user11', 5);
CALL AddUserScore('user12', 8);
CALL AddUserScore('user13', 3);
CALL AddUserScore('user14', 9);
CALL AddUserScore('user15', 2);

SELECT *
FROM quiz_scores;

SELECT *
FROM top_scores_view;
