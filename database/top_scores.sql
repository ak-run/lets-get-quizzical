CREATE DATABASE user_scores;

USE user_scores;

CREATE TABLE quiz_scores(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nickname VARCHAR(25) NOT NULL CHECK (CHAR_LENGTH(nickname) BETWEEN 3 AND 25) UNIQUE,
    SCORE INT NOT NULL CHECK (score BETWEEN 1 AND 10)
);

-- View for top 10 scores
CREATE VIEW top_scores_view AS
SELECT nickname, score
FROM quiz_scores
ORDER BY score DESC, nickname
LIMIT 10;

-- Stored procedure to add data to user_scores
DELIMITER //

CREATE PROCEDURE AddUserScore(IN input_nickname VARCHAR(25), IN input_score INT)
BEGIN
    INSERT INTO quiz_scores (nickname, score) VALUES (input_nickname, input_score);
END //

DELIMITER ;

-- fake starting data
CALL AddUserScore("Frodo Baggins", 5);
CALL AddUserScore("Aragorn", 8);
CALL AddUserScore("Gollum", 3);
CALL AddUserScore("Legolas", 9);
CALL AddUserScore("Gimli", 2);
CALL AddUserScore("Galadriel", 7);
CALL AddUserScore("Samwise Gamgee", 4);
CALL AddUserScore("Gandalf", 6);
CALL AddUserScore("Sauron", 1);
CALL AddUserScore("Smeagol", 1);
CALL AddUserScore("Boromir", 5);
CALL AddUserScore("Eowyn", 8);
CALL AddUserScore("Thranduil", 3);
CALL AddUserScore("Arwen Undomiel", 10);
CALL AddUserScore("Merry", 2);

SELECT *
FROM quiz_scores;

SELECT *
FROM top_scores_view;
