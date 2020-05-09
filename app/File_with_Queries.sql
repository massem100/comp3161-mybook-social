if request.method =='POST':
        if text_form.validate_on_submit() and text_form.text_post.data:

            worded_post = text_form.text_post.data 
            -- # use statements below with implemented functions to format the time before storing on the database
            userid = current_user.id
            post_date = format_date_joined(datetime.now())
            post_time = format_time_joined(datetime.now())


           
            cur = mysql.connection.cursor()
            cur.execute(""" INSERT INTO post (post_id, userid, post_date, post_time) 
                        VALUES (NULL, "{}", "{}", "{}") """.format(userid,post_date,post_time))
            
            cur.execute(""" INSERT INTO text_post (text_id, post_id, text_message) 
                    VALUES (NULL, (SELECT max(post_id) FROM post WHERE userid = '{}'), "{}") """.format(userid, worded_post))
         
            mysql.connection.commit()
            cur.close()
            
            flash('Text Uploaded', 'success')
            return render_template('dashboard.html', text_form = text_form, image_form = image_form)
