-- Database to store user scores
CREATE DATABASE user_scores;

USE user_scores;

-- Create a table to store quiz scores
CREATE TABLE quiz_scores(
	id INT AUTO_INCREMENT PRIMARY KEY,
	avatar VARCHAR(100),
    nickname VARCHAR(25) NOT NULL CHECK (CHAR_LENGTH(nickname) BETWEEN 1 AND 25),
    SCORE INT NOT NULL CHECK (score BETWEEN 0 AND 10)
);

-- View to display top 10 scores
CREATE VIEW top_scores_view AS
SELECT
    ROW_NUMBER() OVER (ORDER BY score DESC, nickname) AS position,
    avatar,
    nickname,
    score
FROM
    quiz_scores
ORDER BY
    score DESC, nickname
LIMIT 10;

-- Stored procedure to add data to user_scores
DELIMITER //

CREATE PROCEDURE AddUserScore(IN input_avatar VARCHAR(100), IN input_nickname VARCHAR(25), IN input_score INT)
BEGIN
    INSERT INTO quiz_scores (avatar, nickname, score) VALUES (input_avatar, input_nickname, input_score);
END //

DELIMITER ;

-- fake starting data
CALL AddUserScore("avatar-2.png", "Frodo Baggins", 1);
CALL AddUserScore("avatar-7.png", "Aragorn", 2);
CALL AddUserScore("avatar-4.png", "Gollum", 3);
