from flask import Flask, render_template, request, redirect, url_for, make_response

from my_lib import database_worker, encrypt_password, check_password

app = Flask(__name__)


def create_database():
    db = database_worker("social_net.db")
    query_user = """CREATE table if not exists users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        email TEXT,
        password TEXT,
        bio TEXT 
    )
    """
    query_post = """CREATE table if not exists posts(
        id INTEGER PRIMARY KEY,
        title VARCHAR(100),
        content TEXT not null,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(id) on delete cascade
    )
    """
    db.run_save(query_user)
    db.run_save(query_post)
    db.close()


# login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    error_message = None

    if request.method == 'POST':
        email = request.form['email']
        passwd = request.form['password']

        if len(email) > 0 and len(passwd) > 0:
            db = database_worker('social_net.db')

            # Check if the user exists
            user = db.search(f"SELECT id,email,password from users where email='{email}'")
            existing_user = db.get(f"SELECT * from users where email = '{email}'")

            if not existing_user:
                error_message = "User with this email is not registered"
            elif user:
                user = user[0]  # search returns a list, so here I select one
                user_id, email, hashed_password = user

                if check_password(hashed=hashed_password, user_password=passwd):
                    # create cookie with logged-in user
                    # 1-create the response webpage (redner template)
                    resp = make_response(redirect('post'))
                    resp.set_cookie('user_id', f"{user_id}")
                    print("password is correct")
                    return resp
                else:
                    error_message = "Password incorrect"

    # Render the login template with the error message
    return render_template('login.html', error_message=error_message)


# register page
@app.route('/register', methods=['GET', 'POST'])
def register():
    error_message = None

    if request.method == "POST":
        # Get the form data
        username = request.form['username']
        email = request.form['email']
        passwd = request.form['password']
        passwd_check = request.form['check_password']
        bio = request.form['description']

        # Check password validity
        if passwd_check != passwd or len(passwd_check) < 8:
            error_message = "Passwords do not match or are not at least 8 characters long."
        elif " " in username:
            error_message = "Username must not contain spaces"
        else:
            # Connect to the database
            db = database_worker('social_net.db')

            # Check if the email or username already exists
            existing_email = db.get(f"SELECT * from users where email = '{email}'")
            existing_user = db.get(f"SELECT * from users where username = '{username}'")

            if existing_email or existing_user:
                error_message = "User with this email/username is already registered."
            else:
                # Insert new user into the database
                new_user = f"INSERT into users (username, password, email, bio) values('{username}', '{encrypt_password(passwd)}','{email}','{bio}')"
                db.run_save(new_user)
                db.close()
                return redirect(url_for("login"))

    # Render the register template with the error message
    return render_template("register.html", error_message=error_message)


@app.route('/post', methods=['GET', 'POST'])
def post_review():
    # here you can read the cookie
    print("hello")
    error_message = None

    # Check if user_id cookie exists
    if request.cookies.get('user_id'):
        user_id = request.cookies.get('user_id')
        db = database_worker("social_net.db")

    if request.method == 'POST':
        # Retrieve form data
        title = request.form['title']
        rate = request.form['rate']
        content = request.form['content']

        if len(title) > 0 and len(content) > 0 and len(rate) > 0:
            # Insert new post into the database
            new_post = f"""INSERT into posts(title, rate, content, user_id) values 
                ('{title}','{rate}','{content}',{user_id})"""
            db.run_save(new_post)
            return redirect(url_for("post_review", user_id=user_id))
        else:
            error_message = "You must fill out all fields"

    user, posts = None, None

    # Retrieve user and posts from the database
    user = db.search(f"SELECT * from users where id={user_id}")
    if user:
        posts = db.search(f"SELECT * FROM posts WHERE user_id={user_id} ORDER BY created_at DESC")
        user = user[0]  # remember db.search returns a list

    # Render the profile template with the user, posts, and error message
    return render_template("profile.html", user_id=user_id, posts=posts, user=user, error_message=error_message)


@app.route('/statistics')
def statistics():
    # Connect to the database
    db = database_worker("social_net.db")

    # Get the number of users
    no_user = db.get(f"SELECT count(*) from users")

    # Get the number of posts
    no_post = db.get(f"SELECT count(*) from posts")

    # Render the statistics template with the number of users and posts
    return render_template("statistics.html", no_user=no_user[0], no_post=no_post[0])


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/logout')
def logout():
    resp = make_response(render_template('index.html'))
    resp.set_cookie('user_id', "", expire=0)  # delete cookie
    return render_template("index.html")


@app.route('/users')
def users():
    # Connect to the database
    db = database_worker("social_net.db")

    # Retrieve all users from the database
    all_users = db.search("SELECT * FROM users")

    # Close the database connection
    db.close()

    # Render the users template with the list of users
    return render_template("users.html", users=all_users)


@app.route('/all-posts')
def allposts():
    # Connect to the database
    db = database_worker("social_net.db")

    # Retrieve all posts from the database, ordered by created_at in descending order
    posts = db.search(f"select * from posts ORDER BY created_at DESC")

    # Close the database connection
    db.close()

    # Render the all-posts template with the list of posts and users
    return render_template("all-posts.html", posts=posts, users=users)


@app.route('/delete_post', methods=['POST'])
def delete_post():
    # Get the post_id from the form data
    post_id = request.form['post_id']

    # Connect to the database
    db = database_worker("social_net.db")

    # Delete the post from the database based on the post_id
    db.run_save(f"DELETE FROM posts WHERE id={post_id}")

    # Redirect to the post_review route
    return redirect(url_for("post_review"))


@app.route("/account", methods=["GET", "POST"])
def account():
    # Check if user_id cookie exists
    if request.cookies.get('user_id'):
        user_id = request.cookies.get('user_id')

        # Connect to the database
        db = database_worker("social_net.db")

        # Retrieve user from the database based on user_id
        user = db.search(f"SELECT * from users where id={user_id}")

        # Render the account template with user information
        return render_template("account.html", user_id=user_id, user=user)


@app.route('/all-posts/<int:post_id>/like', methods=['POST'])
def like_post(post_id):
    # Check if user_id cookie exists
    if request.cookies.get('user_id'):
        user_id = int(request.cookies.get('user_id'))

        # Connect to the database
        db = database_worker("social_net.db")

        # Check if the user has already liked the post
        likes_query = f"SELECT * FROM likes WHERE post_id={post_id} AND user_id={user_id}"
        user_like = db.search(likes_query)

        if user_like:
            # If the user has already liked the post, remove their like
            delete_like_query = f"DELETE FROM likes WHERE post_id={post_id} AND user_id={user_id}"
            db.run_save(delete_like_query)
        else:
            # If the user hasn't liked the post yet, add their like
            add_like_query = f"INSERT INTO likes(post_id, user_id) VALUES ({post_id}, {user_id})"
            db.run_save(add_like_query)

        # Update the likes count for the post in the database
        likes_query = f"SELECT COUNT(*) FROM likes WHERE post_id={post_id}"
        likes_count = db.search(likes_query)[0][0]
        update_post_query = f"UPDATE posts SET likes={likes_count} WHERE id={post_id}"
        db.run_save(update_post_query)
        print(likes_count)

        # Close the database connection
        db.close()

        # Redirect to the allposts route
        return redirect(url_for("allposts"))
    else:
        # If user_id cookie doesn't exist, redirect to the login route
        return redirect(url_for("login"))


print("Creating the database")  # Print a message indicating the creation of the database
create_database()  # Call the function to create the database

if __name__ == '__main__':
    app.run()  # Run the Flask application
