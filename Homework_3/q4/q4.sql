CREATE TABLE new_table(
player INTEGER references more_player_stats,
prl NUMERIC,
position TEXT);

INSERT INTO new_table (player, prl)
(SELECT id, ROUND(per - 67*va/(gp*minutes),1) FROM more_player_stats);

UPDATE new_table
SET position = 'PF'
WHERE prl >= 11.3;

UPDATE new_table
SET position = 'PG'
WHERE prl < 11.3 AND prl >= 10.8;

UPDATE new_table
SET position = 'C'
WHERE prl < 10.8 AND prl >= 10.6;

UPDATE new_table
SET position = 'SG/SF'
WHERE prl < 10.6;

SELECT * FROM new_table
ORDER BY player
LIMIT 10;
