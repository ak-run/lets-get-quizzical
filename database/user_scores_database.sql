CREATE DATABASE user_scores;

USE user_scores;

CREATE TABLE quiz_scores(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nickname VARCHAR(25) NOT NULL CHECK (CHAR_LENGTH(nickname) BETWEEN 3 AND 25) UNIQUE,
    SCORE INT NOT NULL CHECK (score BETWEEN 1 AND 10)
);

CREATE VIEW top_scores_view AS
SELECT
    ROW_NUMBER() OVER (ORDER BY score DESC, nickname) AS position,
    nickname,
    score
FROM
    quiz_scores
ORDER BY
    score DESC, nickname
LIMIT 10;

-- Stored procedure to add data to user_scores
DELIMITER //

CREATE PROCEDURE AddUserScore(IN input_nickname VARCHAR(25), IN input_score INT)
BEGIN
    INSERT INTO quiz_scores (nickname, score) VALUES (input_nickname, input_score);
END //

DELIMITER ;

-- fake starting data
CALL AddUserScore("Frodo Baggins", 1);
CALL AddUserScore("Aragorn", 2);
CALL AddUserScore("Gollum", 3);


SELECT *
FROM quiz_scores;

SELECT *
FROM top_scores_view;
