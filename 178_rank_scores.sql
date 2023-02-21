SELECT
Scores.score,
dense_rank() OVER (ORDER BY Scores.score DESC) AS 'rank'
FROM Scores
