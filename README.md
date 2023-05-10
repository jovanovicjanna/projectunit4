# Unit 4 project: Social network

![Hella cute-1 (1)](https://user-images.githubusercontent.com/111895127/236603162-12001a94-8bf8-435f-922e-27bd17110f79.png)
Fig 1 shows the logo I have made in Adobe Express for social network

# Criterion A: Planning

## Problem Description
My client is a student at a local school. After meeting with her (see Appendix 1), I discovered that she is interested in exploring new makeup brands and products. She is new to the industry and doesn’t know where to begin or how to know the real quality of the product. Currently, she is exploring her area of interest through various social media apps but the information is too disorganized as it does not guide users to each page. Other social networks are not well-established communities concentrated just on makeup and she is not able to learn from people who know more than she does and view their reviews on products. Moreover, she would like to make reviews of the makeup she tries and share her experience with others.

## Proposed Solution
After meeting with my client (see Appendix 1), I brainstormed about what the best solution for her would be. I concluded that a website created using Python, HTML, and CSS would be the most convenient one. This social network will be concentrated just on makeup, simple to understand and it will guide users to each page using the top navigation bar. She would be able to see other people's posts and interact with them by liking them. Additionally, she would be able to create her posts with properties such as titles, ratings, and reviews. Users’ personal information will be stored in the SQLite database, and their passwords will be encrypted. Users’ posts will be stored in a separate table of the same database.

## The rationale for the proposed solution
### Why website?
Website is the perfect option for my client because it can be accessed on any device that has an internet connection and a web browser. Additionally,  users can access the social network from their desktop, tablet, laptop, or smartphone. Compared to an application it doesn’t have to be installed which means the user can just simply access the website and start using the social network. For those reasons, this social network website has the potential to reach a wider audience than a social network application. This matches my client's concern about not having a well-established community and wanting to learn from other people, which means that the more popular the social network gets the more people she would get to interact with.

### Why Python?
Python has a very simple syntax compared to languages such as Java, C, and C++, and because of that it has a large community of people using it, so other programmers to comprehend and use my code for future development. Additionally, Python is a programming language which is free of charge and open. The OSI-approved open source license under which the Python is developed makes it a language free to use and distribute, including for commercial purposes [^6]. 

### Why Flask?
Flask is a micro framework offering basic features of web apps. This framework has no dependencies on external libraries [^3]. Flask support for secure cookies (client-side sessions). The usage of secure cookies to control client-side sessions is important when creating social networks or any other website that needs user identification. Secure cookies are more secure than plain text cookies because they are encrypted and can only be decrypted by the server that created them. Flask comes with built-in support for secure cookies, making it simple to build client-side sessions without having to write any additional code. Compared to the Django library, for example, Flask is a lightweight and more flexible framework. For smaller projects, Flask may be quicker and more effective because it has a lower footprint than Django. Due to its reduced size and fewer dependencies, Flask is simpler to deploy and maintain [^3].

### Why SQLite?

SQLite is a compact, file-based relational database, which doesn't need a separate server or installation procedure [^4]. This makes it an excellent option for small projects or applications where usability and simplicity are crucial. SQLite maintains data in a single file, simplifying usage, upkeep, and access [^4]. If we compare SQLite with other ways to store data, such as CSV files, which we used in Project Unit 1, SQLite stores data in a structured, orderly format that makes data retrieval and querying quick and easy. Contrarily, CSV saves data in a plain-text format that might be challenging to read and efficiently query. Additionally, data security is improved by SQLite's support for features like encryption and password protection whereas CSV files lack any built-in security protections and are easily readable and modifiable by anyone with access to the file.

### Why HTML and CSS?

HTML and CSS are the foundational languages used in website creation. The structure and content of the website can be created using HTML, and the styling and layout may be changed using CSS. They provide websites with their overall structure and aesthetics together. Additionally, they have been around for decades, which allows me as a developer to find a large number of recourses to help me create a social network.

## Design statement
I will design and make a social network for a client who is a student at a local school. The social network will be about sharing reviews of makeup products and is constructed using the software HTML, CSS, and Python. It will take 3 weeks to make and will be evaluated according to the criteria listed below.

## Criteria for Success
1. The social network has a login and register system. *[issue tackled=” Other social networks ”]*
2. The user must be able to input their reviews of a product, rate them, and delete them. *[issue tackled=Moreover, she would like to make reviews of the makeup she tries and share her experience with others.]*
3. Users must be able to view the reviews posted by other users. *[issue tackled = she is not able to learn from people who know more than she does and view their reviews on products.]*
4. Users must be able to view basic statistics such as number of users registered and number of posts. [*issue tackled =  Other social networks are not well-established communities ]*
5. Users must be able to like reviews. *[issue tackled = Other social networks are not well-established communities concentrated just on makeup.]*
6. The social network includes a top navigation bar that is visible on pages so it guides users to each page. *[issue tackled = Currently, she is exploring her area of interest through various social media apps but the information is too disorganized as it does not guide viewers to each page]*
# Criterion B: Design Overview
## System diagram
![unit4_systemdiagram (1)](https://github.com/jovanovicjanna/projectunit4/assets/111895127/98d20eed-5459-4a09-821d-61639c3a6480)

Fig 2 shows the system diagram for the Hellacute network which is a visual representation of the system, its parts, and how they relate to one another. 

## Flow diagrams for algorithms
![Blank diagram (1)](https://user-images.githubusercontent.com/111895127/236694225-fbee2249-5671-4c24-8fb2-128448e815b3.png)
Fig 3 shows the flow diagram for the login function

This ‘login’ function takes email and password as user input. The function checks if the user already exists in the database and if the password is correct, and if both statements are true it creates a cookie with the user's ID and redirects them to the ‘post’ page. If user input is not in the database or the password is incorrect, the function displays an error message and renders the ‘login’ page.

![likesflowchart](https://user-images.githubusercontent.com/111895127/236696274-aa0d1ecc-08c3-43fb-a7bd-9c2df114ae65.png)
Fig 4 shows the flow diagram for the like_post function

This ‘like_post’ function allows users to like or unlike posts. It checks whether has user already liked the post and accordingly adds or removes likes. It updates the likes count in the posts table in the database and redirects the user to the ‘allposts’ page.

![postreviewflowchart](https://user-images.githubusercontent.com/111895127/236698406-f8310ed7-0fb0-4ebd-a724-e8c58b30eb2b.png)
Fig 5 shows the flow diagram for the post_review function

This ‘post_review’ function allows the user who is logged in to make a post by entering properties such as title, rating, and content. The user must fill out all the fields or else an error message will be displayed. Posts will be displayed in reverse chronological order (the newest one being at the top of the page).

## Wireframe diagram
![unit4wireframe_diagram (1)](https://github.com/jovanovicjanna/projectunit4/assets/111895127/dd39007e-08bf-4d0c-bc4d-2efbee2204b9)

Fig 6 shows the wireframe diagram for the Hellacute network

This wireframe diagram's objective is to provide a visual representation of the user interface design that outlines the structure and layout of the social network. The wireframe also shows how various screens will be accessed via various buttons. The user can see which screen will open when they press and release the button according to the arrows that extend from the button to the screen.

## ER diagram
![unit4_erdiagram](https://user-images.githubusercontent.com/111895127/236603554-a630ea69-0334-4f8d-bfdf-9f51f76515b2.png)
Fig 7 shows the ER diagram for the database that the client requires

This is the ER diagram for the database illustrating the relationship between the “users”, “posts” and “likes” table from the “social_net” database. In the “users” table, there are 5 different columns including id, username email, password, and bio. Each column will have the specific data type after the column name. The second table “posts” has 7 columns which are id, title, rate, content, likes, created_at, and user_id. The third table “likes” has 3 columns id, post_id, and user_id. This diagram also shows that one user can have multiple posts which can have multiple likes.

## Example of the database

![Screen Shot 2023-05-08 at 5 30 23](https://user-images.githubusercontent.com/111895127/236701264-76e3a714-f29c-4beb-9468-19b1762b59f7.png)

Fig 8 shows the example of the data stored in the "users" table in the "social_net" database

![Screen Shot 2023-05-08 at 5 35 50](https://user-images.githubusercontent.com/111895127/236701422-8ce56a55-12b1-43ff-923f-7b26f0ae07a1.png)

Fig 9 shows the example of the data stored in the "posts" table in the "social_net" database

![Screen Shot 2023-05-08 at 5 36 52](https://user-images.githubusercontent.com/111895127/236701458-2a1cab37-05ca-4f88-a9b9-3e841a713254.png)

Fig 10 shows the example of the data stored in the "likes" table in the "social_net" database

## Record of Task
| Task No | Planned Action                                                                                             | Planned outcome                                                                                                                                                                                                                                                              | Time estimate | Target completion date | Criterion |
|---------|------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1       | Planning: Meeting with client                                                                              | Understand the problem that the client is facing                                                                                                                                                                                                                             | 15 mins       | Apr 6                  | A         |
| 2       | Planning: Write down the problem definition                                                                | Have problem definition which will identify who client is and the product that client want                                                                                                                                                                                   | 20 mins       | Apr 6                  | A         |
| 3       | Planning: Write the proposed solution and rationale for propsed solution                                   | Have a clear justification and reasoning that will both me and the client                                                                                                                                                                                                    | 1 hour        | Apr 7                  | A         |
| 4       | Planning: Write the design statement                                                                       | Have a clear design statement statement that suits the clients needs                                                                                                                                                                                                         | 15 mins       | Apr 7                  | A         |
| 5       | Planning: Have an interview with client                                                                    | Interview the client and present them a proposed solution and confirm their needs. Ask them for feedback and do they have anything to add to it                                                                                                                              | 5 mins        | Apr 9                  | A         |
| 6       | Planning: Write down success criteria                                                                      | Have a clear outline of what needs to be achieved in order to fulfill the client's needs                                                                                                                                                                                     | 30 mins       | Apr 14                 | A         |
| 7       | Design: Create the system diagram                                                                          | Have a visual representation of the system, its parts, and how they relate to one another                                                                                                                                                                                    | 1 hour        | Apr 15                 | B         |
| 8       | Design: Create the wireframe diagram                                                                       | Have an understanding of how many screens the social network will have, how are they going to be connected, and how am I going to style them using CSS and HTML                                                                                                              | 2 hours       | Apr 17                 | B         |
| 9       | Design: Create the flow diagram for key functions                                                          | Create flow diagrams that explain how the main function of the application would be organized and carried out using natural language                                                                                                                                         | 2 hours       | Apr 19                 | B         |
| 10      | Design: Create logo for the social network                                                                 | Create a logo which will appear on the top of every page of the social network                                                                                                                                                                                               | 30 mins       | Apr 20                 | B         |
| 11      | Develop: Build HTML template                                                                               | Create base template HTML code and CSS design that can be used for all pages with the top navigation bar                                                                                                                                                                     | 20 mins       | Apr 21                 | C         |
| 13      | Develop: Create the databases                                                                              | Create the databases for users and posts                                                                                                                                                                                                                                     | 15 mins       | Apr 22                 | C         |
| 14      | Develop: Create validation functions                                                                       | Create code validation functiones which validate email, username, password and ensures that password and password check match, this can be used in future code development                                                                                                   | 45 mins       | Apr 25                 | C         |
| 15      | Develop: Create registration function                                                                      | Make registration function, use template from the "Learning log" and upgrade it, user will be able to enter properties such as email, username, password and biography and they will be stored in the database. Password is encrypted.                                       | 2 hours       | Apr 29                 | C         |
| 16      | Develop: Create login function                                                                             | Make login function, create cookies when the user successfully logged in, validation of username and password match                                                                                                                                                          | 1 hour        | May 1                  | C         |
| 17      | Develop: Create function for posting reviews                                                               | Make post function and ensure that all the properties entered by user (title, rate, content) successfully stored in the database.                                                                                                                                            | 45 mins       | May 1                  | C         |
| 18      | Develop: Validate input for function for posting reviews                                                   | Validate users input and ensure that the user can't upload empty post.                                                                                                                                                                                                       | 20 mins       | May 1                  | C         |
| 19      | Develop: Create delete function                                                                            | Adding an option for user to delete posts that they have created                                                                                                                                                                                                             | 20 mins       | May 2                  | C         |
| 20      | Develop: Adding feature which displays datetime                                                            | Adding a feature that will display datetime when the post is created, accordingly, posts will be displayed in reverse chronological order (the newest one being at the top of the page)                                                                                      | 20 mins       | May 2                  | C         |
| 21      | Develop: Allowing user to view all the posts posted on the social network                                  | Adding a feature which will allow user to view all the posts posted on the social network and which user posted specific post                                                                                                                                                | 45 mins       | May 2                  | C         |
| 22      | Develop: Make function which will display basic statistics: number of posts and number of users registered | Making a function which will calculate number of the users registered and posts posted from the database and displaying that information on the separate page                                                                                                                | 20 mins       | May 3                  | C         |
| 23      | Develop: Create function for liking posts                                                                  | Adding an option for user to like and unlike posts; make a separate table in the database; ensure that user can't like the post twice; display the number of likes on each post and update the number in the database when it changes; make a heart button for that function | 4 hours       | May 3                  | C         |
| 23      | Develop: Create a function which will display users basic information on the 'all-posts' page              | Making a profile page which displays a basic information about user such as their username, id, email and biography                                                                                                                                                          | 15 mins       | May 4                  | C         |
| 24      | Develop: Create logout function                                                                            | Make log out function, clear all the cookies                                                                                                                                                                                                                                 | 10 mins       | May 4                  | C         |
| 25      | Test: Create test plans                                                                                    | Create detailed test plans for the prototype, and test functions including login, register, and post. All types of tests including unit tests, integrated tests, and non-functional test                                                                                     | 25 mins       | May 5                  | C         |
| 26      | Test: Execute test plans                                                                                   | Execute the test plans that have been done                                                                                                                                                                                                                                   | 10 mins       | May 5                  | C         |
| 27      | Test: Preform beta testing                                                                                 | Ask the client to test the prototype once, gather feedbacks on implementation                                                                                                                                                                                                | 20 mins       | May 5                  | C,D       |
| 28      | Implement: Debug the code                                                                                  | Implement all of the testing-related bugs, if any                                                                                                                                                                                                                            | 30 mins       | May 6                  | C, D      |
| 29      | Implement: Preform beta testing                                                                            | Implement: Beta testing                                                                                                                                                                                                                                                      | 1 hour        | May 6                  | C, D      |
| 30      | Evaluation: Testing my program with client and another user                                                | Ask the client and another user to do beta testing on the program                                                                                                                                                                                                            | 35 mins       | May 7                  | E         |
| 31      | Evaluation: Interview client and another user                                                              | Interview the client and a user who has seen the website prototype. Verify that the success criteria are met and collect additional feedback and implementable recommendations.                                                                                              | 15 mins       | May 7                  | E         |
| 32      | Implement: Implement recommendations                                                                       | After the beta testing, put the suggestions gained from the user and client interviews into practice.                                                                                                                                                                        | 50 mins       | May 7                  | C, E      |
| 33      | Functionality: Write the script for the video                                                              | Write the script for the video                                                                                                                                                                                                                                               | 10 mins       | May 8                  | D         |
| 34      | Functionality: Create the video                                                                            | Create video that demonstrates the functionality and extensibility of the program                                                                                                                                                                                            | 15 mins       | May 10                 | D         |
## Test Table
| Instruction                                                  | Category               | Input/example code                                          | Description                                                                                                         | Expected output                                                                                                                                                                                                      | Success criteria |
|--------------------------------------------------------------|------------------------|-------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| Test registration function-success                           | Unit testing           | Username, Email, Password, Password confirmation, Biography | Register an account, input username, email, password, password confirmation, and biography, all information correct | Users input successfully stored in the database, password hashed, and user is redirected to the 'login' page                                                                                                         | 1                |
| Test registration function - user already registered         | Unit testing           | Username, Email, Password, Password confirmation, Biography | Input username or (and) email which is already stored in the database                                               | If email/username is already used error message displays "User with this email/username is already registered."                                                                                                      | 1                |
| Test registration function - Password error                  | Unit testing           | Username, Email, Password, Password confirmation, Biography | Input password which has less than 8 characters or the password and password confirmation do not match              | If passwords do not match or are less than 8 characters long error message displays "Passwords do not match or are not at least 8 characters long."                                                                  | 1                |
| Test registration function - username formatting             | Unit testing           | Username, Email, Password, Password confirmation, Biography | Input username which contains space                                                                                 | If username contains spaces, error message displayed "Username must not contain spaces"                                                                                                                              | 1                |
| Test login function                                          | Unit testing           | Email, Password                                             | Input the correct email and password/Input wrong email and (or) password                                            | The user logs in if the email and password are correct. Error message displays when the email is not registered, or when the passwords do not match                                                                  | 1                |
| Test registration and login function                         | Integrated testing     | Username, Email, Password, Password confirmation, Biography | Register with the account, than login                                                                               | The user successfully registered, than redirected to login page, user successfully logged in and redirected to the page where he can post reviews                                                                    | 1                |
| Log out system                                               | Unit test              | n/a                                                         | User clicks 'log out' button on the top navigation bar                                                              | 'Login' screen will appear                                                                                                                                                                                           | 1                |
| Test posting - no input                                      | Unit testing           | n/a                                                         | No input for title, rate or content                                                                                 | The user is unable to post an empty post and error message displays "You must fill out all fields"                                                                                                                   | 2                |
| Test posting - success                                       | Unit testing           | Title,  rating,  review                                     | Input all the fields required                                                                                       | The user is able to view the post with the time it was created, posts arranged from the newest (on the top) to the oldest                                                                                            | 2                |
| Delete post                                                  | Unit testing           | n/a                                                         | Click the button delete on the post created                                                                         | Post will be removed from the screen, and the database. The numbers of the posts on the 'statistics' page will also change                                                                                           | 2, 4             |
| 'All - posts' page display                                   | Non functional testing | n/a                                                         | User clicks 'view reviews' button on the top navigation bar                                                         | Button redirects user to the 'all-posts' page on which user can see all the posts posted by the other users, along with the user id of the user who posted                                                           | 3, 6             |
| 'Statistics' page display                                    | Non functional testing | n/a                                                         | User clicks 'statistics' button on the top navigation bar                                                           | Button redirects user to the 'statistics' page on which user can see number of the users registered and the total number of posts on the application                                                                 | 4                |
| Test statistics, create, delete, login and register function | Integrated             | n/a                                                         | Register multiple users and create/delete multiple posts                                                            | Statistic page updates according to the number of users registered, number of posts dereased if the post is deleted and increased if the post is added                                                               | 1, 2, 4          |
| Test the likes function                                      | Unit testing           | n/a                                                         | User clicks like button on the post                                                                                 | If user clicks the like button on the posts number of likes increases, if user clicks the button again, number of likes decreases, user can not like one post multiple times, number of likes stored in the database | 5                |
| Test the visibility of likes                                 | Non functional testing | n/a                                                         | Display of the number of likes                                                                                      | User being able to see the number of likes on their own post                                                                                                                                                         | 5                |
| Navigation bar                                               | Unit testing           | n/a                                                         | Click on each section title                                                                                         | When click on each section title, goes to the respective page                                                                                                                                                        | 6                |
# Criterion C
## Existing tools
| Software/development tools | Coding Structure tools | Libraries |
|----------------------------|------------------------|-----------|
| PyCharm                    | Encryption             | Flask     |
| Relational databases       | Functions              | SQLite3   |
| SQLite                     | If statements          | passlib   |
| Python                     | For loops              |           |
| Chrome (testing)           |                        |           |

## List of techniques used

1. Get/Post methods
2. Functions
3. If statements
4. For loops
5. Interacting with databases
6. Lists
7. Password hashing
8. Cookies

### Success criteria 1: The social network has a login and register system.
```.py
@app.route('/login', methods=['GET', 'POST'])
def login():
    error_message = None
    if request.method == 'POST':
        email = request.form['email']
        passwd = request.form['password']
        if len(email) > 0 and len(passwd) > 0:
            db = database_worker('social_net.db')
            user = db.search(f"SELECT id,email,password from users where email='{email}'")
            existing_user = db.get(f"SELECT * from users where email = '{email}'")
            if not existing_user:
                error_message = "User with this email is not registered"
            elif user:
                user = user[0]  # search returns a list, so here I select one
                id, email, hash = user
                if check_password(hashed=hash, user_password=passwd):
                    # create cookie with logged-in user
                    # 1-create the response webpage (redner template)
                    resp = make_response(redirect('post'))
                    resp.set_cookie('user_id', f"{id}")
                    print("password is correct")
                    return resp
                else:
                    error_message = "Password incorrect"

    return render_template('login.html',error_message=error_message)
```

Here, I developed an algorithm that makes use of If statements to determine whether the user credentials are accurate and connected to any existing users, in response to a request for login and registration system from my client. 

This algorithm is first checking the HTTP request method to determine whether is user visiting the login form (’GET’) or submitting the form (’POST’). 

If the request method is ‘POST’ function will check the user input and validate it. If a user tried to log in without providing any input, an error message will be displayed. The user must be already registered, and the password must match the one stored in the database for the ‘login’ function to work. If a user passes validation of all the inputs the function sets a cookie with the user's ID and redirects the user to a ‘post’ page.

However, the request method is ‘GET’, and the function will return the “login” page to the user.

In this piece of code, I have used abstraction and stored functions for working with database as well as the ones for encrypting and comparing passwords in file my_lib.py, which enabled me to encapsyle repeating patterns and reuse functions whenever I need them. This makes my code more readable and efficient, reducing the number of errors by repeating the same code at multiple places.

### Success criteria 2: The user must be able to input their reviews of a product, rate them, and delete them.

```.py
@app.route('/post', methods=['GET', 'POST'])
def post_review():
    # here you can read the cookie
    print("hello")
    error_message = None
    if request.cookies.get('user_id'):
        user_id = request.cookies.get('user_id')
        db = database_worker("social_net.db")
    if request.method == 'POST':
        title = request.form['title']
        rate = request.form['rate']
        content = request.form['content']
        if len(title) > 0 and len(content) > 0 and len(rate)>0:
            new_post = f"""INSERT into posts(title, rate, content, user_id) values
                ('{title}','{rate}','{content}',{user_id})"""
            db.run_save(new_post)
            return redirect(url_for("post_review", user_id=user_id))
        else:
            error_message = "You must fill out all fields"

    user, posts = None, None
    user = db.search(f"SELECT * from users where id={user_id}")
    if user:
        posts = db.search(f"SELECT * FROM posts WHERE user_id={user_id} ORDER BY created_at DESC")
        user = user[0]  # remenber db.search returns a list

    return render_template("profile.html", user_id=user_id, posts=posts, user=user, error_message=error_message)
```

Here, I developed an algorithm which allows user to post their own reviews with properties including title, rating and content because that was one of the requests from my client, as she wanted to be able to share her own opinions about makeup she tries. 

The code starts by checking if there is a user_id cookie in the request, and if there is forms a connection with the database. If there is no user_id cookie, the code simply returns the profile.html template with no user or posts displayed.

If the request method is ‘POST’ code checks whether the some of the fields in the form are empty, and if so displays an error message. If all the fields are filled out function creates a post in the database with properties previously mentioned.

When forming this code I divided the task of posting a review into smaller steps, such as checking whether the user is logged in, getting the user ID from a cookie, or inserting the review into the database and therefore used decomposition as the part of computational thinking.

# Succes criteria 3: Users must be able to view the review posted by other users.

The code shown below is response to one of my success criterias which will allow user to view posts posted by other users. It was quite easy to made, since the only thing that had to be done was to make a query which will display everything from table posts, in a reverse chronological order (the newest one being at the top of the page). The harder part was making a visually appealing like button, but I have found CSS template using OpenAI [^5].

```.py
@app.route('/all-posts')
def allposts():
    db = database_worker("social_net.db")
    posts = db.search(f"select * from posts ORDER BY created_at DESC")
    return render_template("all-posts.html", posts=posts,users=users)
```

### Success criteria 4: Users must be able to view basic statistics.

This is the code for simple function statistics which allowed me to display number of posts and number of users registered on a separate page. I have made two queries, one counting the number of the users by counting the rows of the ‘users’ table, and another one counting the number of the posts by counting the rows form the ‘posts’ table.

```.py

@app.route('/statistics')
def statistics():
    db = database_worker("social_net.db")
    no_user = db.get(f"SELECT count(*) from users")
    no_post = db.get(f"SELECT count(*) from posts")
    return render_template("statistics.html", no_user = no_user[0], no_post=no_post[0])
```

### Success criteria 5: Users must be able to like reviews posted by other users. 

Adding the like function was the most challenging task for me in the whole project. The hardest part of making that function was to make likes compatible with multiple users, meaning that the first time I have developed the function one user would remove another users like, not adding a new one. I overcome that challenge by adding this line of code which checks whether has user previously liked the post or not by checking the rows in the likes table.
```.py
likes_query = f"SELECT * FROM likes WHERE post_id={post_id} AND user_id={user_id}"
user_like = db.search(likes_query)
```
This block of code will remove the like on the post if the user has already liked it by constructing a query which will delete the corresponding row from the ‘likes’ table.
```.py
if user_like:
    # If the user has already liked the post, remove their like
    delete_like_query = f"DELETE FROM likes WHERE post_id={post_id} AND user_id={user_id}"
    db.run_save(delete_like_query)
```
Accordingly, this block of code will add the like on the post if the user hasn’t previously liked it by constructing a query which will add the row in the ‘likes’ table.
```.py
else:
    # If the user hasn't liked the post yet, add their like
    add_like_query = f"INSERT INTO likes(post_id, user_id) VALUES ({post_id}, {user_id})"
    db.run_save(add_like_query)
```
To finish off this function will construct the query to count the numbers of likes of a specific post and another one to update the number of likes in the table.
```.py
likes_query = f"SELECT COUNT(*) FROM likes WHERE post_id={post_id}"
likes_count = db.search(likes_query)[0][0]
update_post_query = f"UPDATE posts SET likes={likes_count} WHERE id={post_id}"
db.run_save(update_post_query)
print(likes_count)

db.close()
```
#### The whole like_post function:
```.py
@app.route('/all-posts/<int:post_id>/like', methods=['POST'])
def like_post(post_id):
    if request.cookies.get('user_id'):
        user_id = int(request.cookies.get('user_id'))
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

        db.close()

        return redirect(url_for("allposts"))
    else:
        return redirect(url_for("login")
```
I have again used abstraction as I have used functions and modules to abstract away complex tasks, making the code easier to understand and reuse.

### Success criteria 6: The social network includes a top navigation bar that is visible on pages so it guides users to each page. 

My 6th success criteria requires a navigation bar that is present in pages so it guides the users through the pages and make it look more organized. After noticing that the bar appeared repeatedly throughout all of the sites, I used pattern recognition and made a base template (base.html) that could be applied to and extended over all of the pages. 

Because I constructed a new template that can be reused and expanded as necessary, rather than duplicating the code for the navigation bar on every page, I also used abstraction as a computational skill in this case. This strategy encourages efficiency and maintainability because any modifications made to the base template will spread to all the pages instantly. Therefore, if I need to change the structure by, for example, adding another page, there won't be a requirement for particular adjustments within each HTML file. Future developers would also find it simpler if they wanted to expand the website's page count.

```.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    {% if title %}
    <title>{{ title }} </title>
    {% else %}
    <title>Welcome</title>
    {% endif %}
    <link rel="stylesheet" href = "/static/mystyle.css">
</head>

<div class="banner">
        <div class="navbar">
            <img src="/static/hellacutetransparent.png" class="logo">
            <ul>
                <li><a href="/post">Create a post</a></li>
                <li><a href="/statistics">Statistics</a></li>
                <li><a href="/account">My profile</a></li>
                <li><a href="/login">Logout</a></li>
            </ul>
        </div>
    </div>
<body>

{% block content %} {% endblock %}

</body>

</html>
```

# Criterion D: Functionality and Extensibility

# Criterion E: Evaluation

## Client (Record of this is in the appendix)

| Criteria                                                                                                      | Met or Not? | Feedback                                                                  |
|---------------------------------------------------------------------------------------------------------------|-------------|---------------------------------------------------------------------------|
| 1. The social network has a login and register system.                                                        | Met         | Client has no additional feedback                                         |
| 2. The user must be able to input their reviews of a product, rate them, and delete them.                     | Met         | Ratings could be formatted differently, instead of text box maybe slider  |
| 3. Users must be able to view reviews posted by other users.                                                  | Met         | Would be nice if there were pictures of the products                      |
| 4. Users must be able to view basic statistics such as number of users registered and number of posts.| Met         | Client has no additional feedback                                         |
| 5. Users must be able to like posts.                                                                          | Met         | Client has no additional feedback                                         |
| 6. The social network includes a top navigation bar that is visible on pages so it guides users to each page. | Met         | Client has no additional feedback                                         |

## Other user (Record of this is in the appendix)
| Criteria                                                                                                      | Met or Not? | Feedback                                |
|---------------------------------------------------------------------------------------------------------------|-------------|-----------------------------------------|
| 1. The social network has a login and register system.                                                        | Met         | User has no additional feedback         |
| 2. The user must be able to input their reviews of a product, rate them, and delete them.                     | Met         | User has no additional feedback                     |
| 3. Users must be able to view reviews posted by other users.                                               | Met         | Would be nice if user can comment on the post         |
| 4. Users must be able to view basic statistics such as number of users registered and number of posts.                                                              | Met         | Add feature to see most famous products |
| 5. Users must be able to like posts.                                                                          | Met         | User has no additional feedback         |
| 6. The social network includes a top navigation bar that is visible on pages so it guides users to each page. | Met         | User has no additional feedback         |

## Suggestions for future development

For future development the first suggestion was to make the formatting of the rating different, making it into a slider for example. This feature will ensure that the numbers are the only thing that is imputed when it comes to rating products. Right now the rating is just a regular text field that allows users to rate the product in whichever form they want.

Another suggestion for future development would be to allow users to post images of the product they are reviewing in order for users to visualize the product which is being described. Currently, users can leave a review of the product but not an image.

The third suggestion was to allow users to comment on other people's posts, which will increase the engagement and popularity of an application. For now, the user is able to like the post and engage with the content in that way, but not comment on it.

The last suggestion was to update the statistics page and show the most popular product (the one with the highest ratings). Currently, the statistics page displays the number of users registered and the total number of posts on the social network.

# Appendix
## Appendix 1: Client interview - Purpose and requirements
![Screen Shot 2023-05-08 at 1 13 49](https://user-images.githubusercontent.com/111895127/236689365-00a6da4e-139c-45c8-9ab0-cc0649e3da41.png)

Fig 11 shows my notes from the first interview with the client

## Appendix 2: 
![Screen Shot 2023-05-08 at 22 22 01](https://user-images.githubusercontent.com/111895127/236835335-83b651e5-a185-4bc8-9508-64fb82ec8b9f.png)

Fig 12 shows my notes after interview with the client and another user after the development of social network
[^1]: Coursera. “What Is Python Used For? A Beginner’s Guide.” Coursera, 22 Sept. 2021, www.coursera.org/articles/what-is-python-used-for-a-beginners-guide-to-using-python.

[^2]: “Python vs C++: What’s the Difference?” Www.guru99.com, www.guru99.com/python-vs-c-plus-plus.html.

[^3]: “Flask vs Django: What’s the Difference between Flask & Django?” Www.guru99.com, www.guru99.com/flask-vs-django.html.

[^4]: “SQLite Documentation.” Sqlite.org, sqlite.org/docs.html.

[^5]: ChatGPT. “ChatGPT.” Chat.openai.com, 2023, chat.openai.com/.

[^6]: “Top Advantages of Python over Other Programming Languages.” Edoxi Training, www.edoxi.com/studyhub-detail/advantages-of-python-over-other-programming-languages.
