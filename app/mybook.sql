
/* 
Database for MyBook Application
Created April 29, 2020
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
DROP TABLE IF EXISTS group;
DROP TABLE IF EXISTS friend;
DROP TABLE IF EXISTS photo;
DROP TABLE IF EXISTS group_editor;


/*
 user - ( user_ID, f_name, l_name, gender, date_of_birth, username, password) 
 user_info - ( user_ID, email, phon_num)
 userprofile - ( profile_ID, userid,username,  profile_photo,  nationality,user_bio) 
 Post - ( post_ID, userid, post_date, post_time )
 post_text (text_ID, post_ID, text_message) 
 post_image (image_ID, post_ID, image_filename, caption)
 Group - ( group_ID, admin_ID, groupname, dateCreated, grouptype, group_description )
 Comment ( comment_ID, user_ID, comment_Content, time_posted, date_posted ) 
 Friend (fid, userid, friend_type)
 Photo ( photo_id, photo_desc, photo_filename, date_added )
 Admin (admin_ID, group_ID, content_editors)  rename to group_admin
 
 
 */
 /* derived from entities */
CREATE TABLE user(
    userid varchar(10) not null unique, 
    username varchar(25), not null unique,
    f_name varchar(25) not null, 
    l_name varchar(25) not null, 
    gender varchar(10), 
    date_of_birth date,  
    user_password varchar(),
    primary key(userid)

);

CREATE TABLE user_info(
    userid varchar(10) not null unique,
    email  varchar(50),
    phon_num varchar(25),
    primary key(userid)
    -- foreign key references user(userid)- will decide how to treat foreign keys after


);

CREATE table userprofile(
    profile_id varchar(10) not null unique,
    userid varchar(10) not null unique,
    username varchar(25),
    profile_photo varchar(100),
    nationality varchar(25),
    user_bio varchar(150),
    primary key(profile_id, userid) /* deciding whether just profile_id must be a PK or both */
    -- foreign key references user(userid)- will decide how to treat foreign keys after
);

CREATE TABLE post(
    post_id varchar(10) not null unique,
    userid varchar(10) not null unique,
    post_date date,
    post_time time, 
    primary key(postid, userid)
    -- foreign key references user(userid)- will decide how to treat foreign keys after

);

/* derived from ISA */
CREATE TABLE text_post(
    text_id varchar(10) not null unique,
    post_id varchar(10) not null unique,
    text_message varchar(250),
    primary key(text_id, post_id)
    -- foreign key references user(userid)- will decide how to treat foreign keys after
);

CREATE TABLE image_post(
    image_id varchar(10) not null unique,
    post_id varchar(10) not null unique,
    image_filename varchar(100),
    caption varchar(150), 
    primary key (image_id, post_id)
    -- foreign key references user(userid)- will decide how to treat foreign keys after

);

CREATE TABLE comment(
    comment_id varchar(10) not null unique,
    postid varchar(10) not null,
    userid varchar(10) not null,
    comment_Content varchar(250),
    time_posted time not null,
    date_posted date not null, 
    primary key(comment_id, post_id)
    -- foreign key references user(userid)- will decide how to treat foreign keys after
    -- revise primary keys?


); 

CREATE TABLE group(
    group_id varchar(10) not null unique,
    admin_id varchar(10) not null,
    groupname varchar(25)  not null ,
    dateCreated date not null,
    grouptype varchar(7) not null,
    group_description varchar(150),
    primary key(group_id)
    -- foreign key references user(userid)- will decide how to treat foreign keys after
);

CREATE TABLE friend(
    fid varchar(10) not null unique, 
    userid varchar(10) not null, 
    friend_type varchar(9),
    primary key(fid, userid)
    -- foreign key references user(userid)- will decide how to treat foreign keys after
);

CREATE TABLE photo (
    photo_id varchar(10) not null unique,
    userid varchar(10) not null,
    photo_desc varchar(150),
    photo_filename varchar(100) not null,
    date_added date not null, 
    primary key(photo_id)
    -- foreign key references user(userid)- will decide how to treat foreign keys after

);

CREATE TABLE group_editor (
    admin_id varchar (10) not null unique,
    group_id varchar () not null,
    content_editors varchar(25), 
    primary key(admin_id, group_id)
    -- foreign key references user(userid)- will decide how to treat foreign keys after

);

/* derived from relationships - do we have any? Based on ERD? */