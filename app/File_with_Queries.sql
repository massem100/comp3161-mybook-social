DELIMITER //
CREATE PROCEDURE `update_profile`(
  INS_userid int(10),
  INS_photo varchar(100),
  INS_nationality varchar(25),
  INS_bio varchar(150)
) 
BEGIN 
DECLARE Icount INT;
SELECT
  count(1) INTO Icount
FROM
  userprofile
WHERE
  userId = INS_userid; 
IF Icount = 0 THEN
INSERT INTO
  userprofile(
    profile_id,
    userid,
    profile_photo,
    nationality,
    user_bio)
VALUES
  (
    NULL,
    INS_userid,
    INS_photo,
    INS_nationality,
    INS_bio);
ELSE
  UPDATE
    userprofile
  SET
    userid = INS_userid,
    profile_photo = INS_photo,
    nationality = INS_nationality,
    user_bio = INS_bio
  WHERE
    userid = INS_userid;
END IF;
END //
DELIMITER;







DELIMITER //
CREATE PROCEDURE `update_user`(
  INS_userid int(10),
  INS_username varchar(25),
  INS_f_name varchar(25),
  INS_l_name varchar(25),
  INS_gender varchar(10),
  INS_dob date, 
  INS_password varchar(100)
) 
BEGIN 
DECLARE Icount INT;
SELECT
  count(1) INTO Icount
FROM
  user
WHERE
  userId = INS_userid;
IF Icount = 0 THEN
INSERT INTO
  user(
    userid, 
    username, 
    f_name, 
    l_name, 
    gender, 
    date_of_birth, 
    user_password)
VALUES
  (
    INS_userid,
    INS_username,
    INS_f_name,
    INS_l_name,
    INS_gender,
    INS_dob,
    INS_password);
ELSE
  UPDATE
    user
  SET
    userid = INS_userid,
    username = INS_username, 
    f_name = INS_f_name, 
    l_name = INS_l_name, 
    gender = INS_gender, 
    date_of_birth = INS_dob, 
    user_password = INS_password    
  WHERE
    userid = INS_userid;
END IF;
END //
DELIMITER;


DELIMITER / / 
CREATE PROCEDURE `update_user_info`(
  INS_userid int(10),
  INS_email varchar(50), 
  INS_phone_num varchar(25)
) 
BEGIN DECLARE Icount INT;
SELECT
  count(1) INTO Icount
FROM
  user
WHERE
  userId = INS_userid;
IF Icount = 0 THEN
INSERT INTO
  user(
    userid,
    email, 
    phone_num
  )
VALUES
  (
    NULL,
    INS_email, 
    INS_phone_num
  );

ELSE
UPDATE
  user
SET
  userid = INS_userid,
  username = INS_username,
  f_name = INS_f_name,
  l_name = INS_l_name,
  gender = INS_gender,
  date_of_birth = INS_dob,
  user_password = INS_password
WHERE
  userid = INS_userid;

END IF;

END / / 
DELIMITER;