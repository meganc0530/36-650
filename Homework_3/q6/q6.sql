ALTER TABLE player_bios
ADD COLUMN height_temp NUMERIC;

UPDATE player_bios
SET height_temp = 12*split_part(height,'-',1)::integer + split_part(height,'-',2)::integer;

ALTER TABLE player_bios
DROP COLUMN height;

ALTER TABLE player_bios
RENAME COLUMN height_temp TO height;

SELECT firstname, lastname, height 
FROM player_bios
ORDER BY id
LIMIT 5;