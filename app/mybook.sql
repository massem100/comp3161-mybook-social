
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
DROP TABLE IF EXISTS group;
DROP TABLE IF EXISTS comment;
DROP TABLE IF EXISTS friend;
DROP TABLE IF EXISTS photo;
DROP TABLE IF EXISTS group_admin;
DROP TABLE IF EXISTS post_text; 
DROP TABLE IF EXISTS post_image;

/*
 user - ( user_ID, f_name, l_name, gender, date_of_birth, username, password) 
 user_info - ( user_ID, email, phon_num)
 userprofile - ( profile_ID, userid, email,username,  profile_pic,  nationality,user_bio) )
 Post - ( post_ID, post_date, post_time )
 Group - ( group_ID, admin_ID, groupname, dateCreated, grouptype, group_description )
 Comment ( comment_ID, user_ID, comment_Content, time_posted, date_posted ) 
 Friend (fid, userid, friend_type)
 Photo ( pic_id, pic_desc, pic_name, date_pic_posted )
 Admin (admin_ID, group_ID, content_editors)  rename to group_admin
 post_text ( text_ID, post_ID, text_message ) 
 post_image ( image_ID, post_ID, image_filename, caption)
 
 */
CREATE TABLE user(
    userid varchar(10) not null unique, 
    f_name varchar(25) not null , 
    l_name varchar(25) not null, 
    gender varchar(10), 
    date_of_birth date, 
    email varchar , 
    password

);

