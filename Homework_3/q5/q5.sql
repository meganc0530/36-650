ALTER TABLE player_bios
ADD COLUMN position TEXT;

UPDATE player_bios
SET position = new_table.position
FROM new_table
WHERE player_bios.id = new_table.player;

SELECT firstname, lastname, position
FROM player_bios
ORDER BY id
LIMIT 5;