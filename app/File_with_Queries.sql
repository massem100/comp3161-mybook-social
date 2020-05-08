-- Query to INSERT INTO TEXT_POST but also get generate post_id from post_id as it is generated

-- FRAME insert into text_post then select from post table, insert into post table 


-- INSERT INTO
--     text_post 
-- SELECT post_id FROM (
    
-- );

-- --  INSERT INTO table2 (column1, column2, column3, ...)
-- -- SELECT column1, column2, column3, ...
-- -- FROM table1
-- -- WHERE condition;

-- INSERT INTO
--     post (post_id, userid, post_date, post_time)
-- VALUES
--     (
--         NULL,
--         4,
--         12 / 7 / 1999,
--         9 :34 :21
--     ),
--     OUTPUT post_id

INSERT INTO
    joke(joke_text, joke_date, author_id) 
VALUES
    (
        ‘ Humpty Dumpty had a great fall.’,
        ‘ 1899 – 03 – 13 ’,
        (
            SELECT
                id
            FROM
                author
            WHERE
                author_name = ‘ Famous Anthony ’
        )
    );


INSERT INTO 
    text_post(text_id, post_id, text_message )
VALUES
    (NULL,
    (SELECT 
        post_id
    FROM 
        (INSERT INTO 
                post(post_id,userid, post_date, post_time)                
            VALUES 
            (NULL, 
            '5',
            12/10/2009,
            16:24)
            OUTPUT postid
        ), 
    "Feeling Happy!")