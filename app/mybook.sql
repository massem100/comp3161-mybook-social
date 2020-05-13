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
    email varchar(50) ,
    phone_num varchar(25),
    primary key(userid),
    foreign key(userid) references user(userid) on update cascade on delete cascade
);

CREATE table userprofile(
    profile_id int(10) not null unique AUTO_INCREMENT,
    userid int(10) not null unique,
    profile_photo varchar(100) ,
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
