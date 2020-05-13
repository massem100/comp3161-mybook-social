CREATE DEFINER = `root` @`localhost` PROCEDURE `profile_`(
  kvg_id int(10),
  INS_userid int(10),
  kvdate_added date
) BEGIN DECLARE lcount INT;
SELECT
  count(1) INTO lcount
FROM userprofile
WHERE
  userId = INS_userid
  AND g_id = kvg_id;
IF lcount = 0 THEN
INSERT INTO userprofile(g_id, userId, date_added)
VALUES
  (kvg_id, INS_userid, kvdate_added);
  ELSE
UPDATE userprofile
SET
  g_id = kvg_id,
  userId = INS_userid,
  date_added = kvdate_added
WHERE
  userId = INS_userid
  AND g_id = kvg_id;
END IF;
END $$ CREATE DEFINER = `root` @`localhost` PROCEDURE `update_profile`(
  INS_userid int(10),
  INS_photo varchar(100),
  INS_nationality,
  INS_bio,
  kvdate_added date
) BEGIN DECLARE lcount INT;
SELECT
  count(1) INTO lcount
FROM userprofile
WHERE
  userId = INS_userid IF lcount = 0 THEN
INSERT INTO userprofile(
    profile_id,
    userid,
    profile_photo,
    nationality,
    user_bio
  )
VALUES
  (
    NULL,
    INS_userid,
    INS_photo,
    INS_bio,
    INS_nationality
  );
  ELSE
UPDATE userprofile
SET
  g_id = kvg_id,
  userId = INS_userid,
  date_added = kvdate_added
WHERE
  userId = INS_userid
  AND g_id = kvg_id;
END IF;
END $$