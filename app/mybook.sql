/* 
 
 Database for MyBook Application
 
 */
DROP DATABASE IF EXISTS mybook;

CREATE DATABASE mybook;

use mybook;

-- Add DROP TABLE IF EXISTS statements
-- Prevents duplicating tables. 
DROP TABLE IF EXISTS user;

DROP TABLE IF EXISTS user_info;

DROP TABLE IF EXISTS userprofile;

DROP TABLE IF EXISTS post;

DROP TABLE IF EXISTS text_post;

DROP TABLE IF EXISTS image_post;

DROP TABLE IF EXISTS comment;

DROP TABLE IF EXISTS friend_group;

DROP TABLE IF EXISTS group_editor;

DROP TABLE IF EXISTS group_member;

DROP TABLE IF EXISTS group_post;

DROP TABLE IF EXISTS friend;

DROP TABLE IF EXISTS photo;

/* derived from entities */
CREATE TABLE user(
    userid int(10) not null unique AUTO_INCREMENT,
    username varchar(25) not null unique,
    f_name varchar(25) not null,
    l_name varchar(25) not null,
    gender varchar(10),
    date_of_birth date not null,
    user_password varchar(250) not null,
    primary key(userid)
);

CREATE TABLE user_info(
    userid int(10) not null unique,
    email varchar(50),
    phone_num varchar(25),
    primary key(userid),
    foreign key(userid) references user(userid) on update cascade on delete cascade
);

CREATE table userprofile(
    profile_id int(10) not null unique AUTO_INCREMENT,
    userid int(10) not null unique,
    profile_photo varchar(100),
    nationality varchar(25),
    user_bio varchar(150),
    primary key(profile_id),
    foreign key(userid) references user(userid) on update cascade on delete cascade
);

CREATE TABLE post(
    post_id int(10) not null unique AUTO_INCREMENT,
    userid int(10) not null,
    post_date date not null,
    post_time time not null,
    primary key(post_id),
    foreign key(userid) references user(userid) on update cascade on delete cascade
);

/* derived from ISA */
CREATE TABLE text_post(
    text_id int(10) not null unique AUTO_INCREMENT,
    post_id int(10) not null unique,
    text_message varchar(250) not null,
    primary key(text_id, post_id),
    foreign key(post_id) references post(post_id) on update cascade on delete cascade
);

CREATE TABLE image_post(
    image_id int(10) not null unique AUTO_INCREMENT,
    post_id int(10) not null unique,
    image_filename varchar(100) not null,
    caption varchar(150),
    primary key (image_id, post_id),
    foreign key(post_id) references post(post_id) on update cascade on delete cascade
);

CREATE TABLE friend(
    fid int(10) not null unique AUTO_INCREMENT,
    friend_owner int(10) not null,
    friend_id int(10) not null,
    friend_type varchar(9),
    primary key(fid),
    foreign key(friend_id) references user(userid) on update cascade on delete cascade,
    foreign key(friend_owner) references user(userid) on update cascade on delete cascade
);

CREATE TABLE comment(
    comment_id int(11) not null unique AUTO_INCREMENT,
    post_id int(10) not null,
    userid int(10) not null,
    comment_Content varchar(250) not null,
    time_posted time not null,
    date_posted date not null,
    primary key(comment_id, post_id),
    foreign key(post_id) references post(post_id) on update cascade on delete cascade,
    foreign key(userid) references user(userid) on update cascade on delete cascade
);

CREATE TABLE friend_group (
    group_id int(10) not null unique AUTO_INCREMENT,
    admin_id int(10) not null,
    groupname varchar(25) not null unique,
    date_created date not null,
    grouptype varchar(7) not null,
    group_description varchar(150),
    primary key(group_id),
    foreign key(admin_id) references user(userid) on update cascade on delete cascade
);

CREATE TABLE group_member(
    group_id int(10) not null,
    userid int(10) not null,
    date_created date not null,
    primary key (group_id),
    foreign key(userid) references user(userid) on update cascade on delete cascade,
    foreign key(group_id) references friend_group(group_id) on update cascade on delete cascade
);

CREATE TABLE group_editor (
    group_id int(10) not null,
    content_editor int(10),
    date_added date not null,
    primary key(group_id, content_editor),
    foreign key(content_editor) references user(userid) on update cascade on delete cascade,
    foreign key(group_id) references friend_group(group_id) on update cascade on delete cascade
);

CREATE TABLE group_post(
    group_postid int(10) not null unique AUTO_INCREMENT,
    group_id int(10) not null,
    userid int(10) not null,
    gp_heading varchar(25) not null,
    post_type varchar(10) not null,
    image_filename varchar(50),
    text_content varchar(250),
    date_created date not null,
    time_created time not null,
    primary key (group_postid),
    foreign key(userid) references user(userid) on update cascade on delete cascade,
    foreign key(group_id) references friend_group(group_id) on update cascade on delete cascade
);

CREATE TABLE photo (
    photo_id int(10) not null unique AUTO_INCREMENT,
    userid int(10) not null,
    photo_desc varchar(150),
    photo_filename varchar(100) not null,
    date_added date not null,
    primary key(photo_id),
    foreign key(userid) references user(userid) on update cascade on delete cascade
);

-- Stored Procedure to Update Profile
DELIMITER / / CREATE PROCEDURE `update_profile`(
    INS_userid int(10),
    INS_photo varchar(100),
    INS_nationality varchar(25),
    INS_bio varchar(150)
) BEGIN DECLARE Icount INT;

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
        nationality,
        user_bio
    )
VALUES
    (
        NULL,
        INS_userid,
        INS_nationality,
        INS_bio
    );

ELSE
UPDATE
    userprofile
SET
    userid = INS_userid,
    nationality = INS_nationality,
    user_bio = INS_bio
WHERE
    userid = INS_userid;

END IF;

END / / DELIMITER;

DELIMITER / / CREATE PROCEDURE `select_group_members`() BEGIN
SELECT
    group_id,
    userid,
    date_created
FROM
    group_member;

END / / DELIMITER;

-- Stored Procedure to Update Group Members
CREATE DEFINER = `root` @`localhost` PROCEDURE `group_members_upd`(
    group_id int(10),
    userid int(10),
    date_added date
) BEGIN DECLARE lcount INT;

SELECT
    count(1) INTO lcount
FROM
    group_members
WHERE
    userid = group_id
    AND group_id = group_id;

IF lcount = 0 THEN
INSERT INTO
    group_member(group_id, userid, date_added)
VALUES
    (group_id, userId, date_added);

ELSE
UPDATE
    group_member
SET
    group_id = group_id,
    userid = group_id,
    date_added = date_added
WHERE
    userid = group_id
    AND group_id = group_id;

END IF;

END / / DELIMITER;

-- Stored Procedure to delete a post
DELIMITER / / CREATE PROCEDURE `post_del`(pkpostId int(10)) BEGIN
DELETE FROM
    post
WHERE
    postId = pkpostId;

END / / 
DELIMITER;



DELIMITER / / CREATE PROCEDURE `update_user`(
    INS_userid int(10),
    INS_username varchar(25),
    INS_f_name varchar(25),
    INS_l_name varchar(25),
    INS_gender varchar(10),
    INS_dob date,
    INS_password varchar(100)
) BEGIN DECLARE Icount INT;

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
        user_password
    )
VALUES
    (
        NULL,
        INS_userid,
        INS_username,
        INS_f_name,
        INS_l_name,
        INS_gender,
        INS_dob,
        INS_password
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

END / / DELIMITER;