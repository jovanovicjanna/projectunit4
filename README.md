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
Python is a computer programming language often used to build websites and software [^1]. It has built-in data structures, combined with dynamic binding and typing, which makes it an ideal choice for rapid application development [^2]. Python has a very simple syntax compared to languages such as Java, C, and C++, which makes it easier to write and maintain code and allows other programmers to comprehend and use my code for future development [^2]. Additionally, Python has an extensive range of libraries and frameworks for web development, such as Django, Flask, and Pyramid, which allows me to build up a social network that is visually appealing to users [^2]. Languages such as C++ are not primarily intended for web development and do not offer built-in features for web development, such as HTML or CSS. This implies that to create web apps, I would need to write additional code or make use of external libraries, which can be difficult and time-consuming. 

### Why Flask?
Flask is a micro framework offering basic features of web apps. This framework has no dependencies on external libraries [^3]. Flask support for secure cookies (client-side sessions). The usage of secure cookies to control client-side sessions is important when creating social networks or any other website that needs user identification. Secure cookies are more secure than plain text cookies because they are encrypted and can only be decrypted by the server that created them. Flask comes with built-in support for secure cookies, making it simple to build client-side sessions without having to write any additional code. Compared to the Django library, for example, Flask is a lightweight and more flexible framework. For smaller projects, Flask may be quicker and more effective because it has a lower footprint than Django. Due to its reduced size and fewer dependencies, Flask is simpler to deploy and maintain [^3].

### Why SQLite?

SQLite is a compact, file-based relational database, which doesn't need a separate server or installation procedure [^4]. This makes it an excellent option for small projects or applications where usability and simplicity are crucial. SQLite maintains data in a single file, simplifying usage, upkeep, and access [^4]. If we compare SQLite with other ways to store data, such as CSV files, which we used in Project Unit 1, SQLite stores data in a structured, orderly format that makes data retrieval and querying quick and easy. Contrarily, CSV saves data in a plain-text format that might be challenging to read and efficiently query. Additionally, data security is improved by SQLite's support for features like encryption and password protection whereas CSV files lack any built-in security protections and are easily readable and modifiable by anyone with access to the file.

### Why HTML and CSS?

HTML and CSS are the foundational languages used in website creation. The structure and content of the website can be created using HTML, and the styling and layout may be changed using CSS. They provide websites with their overall structure and aesthetics together. Additionally, they have been around for decades, which allows me as a developer to find a large number of recourses to help me create a social network.

## Design statement
I will design and make a social network for a client who is a student at a local school. The social network will be about sharing reviews of makeup products and is constructed using the software Python. It will take 3 weeks to make and will be evaluated according to the criteria listed below.

## Criteria for Success
1. The social network has a login and register system. *[issue tackled=” Other social networks ”]*
2. The user must be able to input their reviews of a product, rate them, and delete them. *[issue tackled=Moreover, she would like to make reviews of the makeup she tries and share her experience with others.]*
3. Users must be able to view the review posted by other users. *[issue tackled = she is not able to learn from people who know more than she does and view their reviews on products.]*
4. Users must be able to view basic statistics. [*issue tackled =  Other social networks are not well-established communities ]*
5. Users must be able to like reviews posted by other users. *[issue tackled = Other social networks are not well-established communities concentrated just on makeup.]*
6. The social network includes a top navigation bar that is visible on pages so it guides users to each page. *[issue tackled = Currently, she is exploring her area of interest through various social media apps but the information is too disorganized as it does not guide viewers to each page]*
# Criterion B: Design Overview
## System diagram
![unit4_systemdiagram](https://user-images.githubusercontent.com/111895127/236698521-34aaf592-8bc2-463d-95a5-9c256b90652c.png)

Fig x shows the system diagram for the Hellacute network which is a visual representation of the system, its parts, and how they relate to one another. 

## Flow diagrams for algorithms
![Blank diagram (1)](https://user-images.githubusercontent.com/111895127/236694225-fbee2249-5671-4c24-8fb2-128448e815b3.png)
Fig x shows the flow diagram for the login function

This ‘login’ function takes email and password as user input. The function checks if the user already exists in the database and if the password is correct, and if both statements are true it creates a cookie with the user's ID and redirects them to the ‘post’ page. If user input is not in the database or the password is incorrect, the function displays an error message and renders the ‘login’ page.

![likesflowchart](https://user-images.githubusercontent.com/111895127/236696274-aa0d1ecc-08c3-43fb-a7bd-9c2df114ae65.png)
Fig x shows the flow diagram for the like_post function

This ‘like_post’ function allows users to like or unlike posts. It checks whether has user already liked the post and accordingly adds or removes likes. It updates the likes count in the posts table in the database and redirects the user to the ‘allposts’ page.

![postreviewflowchart](https://user-images.githubusercontent.com/111895127/236698406-f8310ed7-0fb0-4ebd-a724-e8c58b30eb2b.png)
Fig x shows the flow diagram for the post_review function

This ‘post_review’ function allows the user who is logged in to make a post by entering properties such as title, rating, and content. The user must fill out all the fields or else an error message will be displayed. Posts will be displayed in reverse chronological order (the newest one being at the top of the page).

## Wireframe diagram
![unit4wireframe_diagram (1)](https://user-images.githubusercontent.com/111895127/236603515-cd3ae0de-7d4a-4526-a44a-8713f5bf001d.png)
Fig x shows the wireframe diagram for the Hellacute network

This wireframe diagram's objective is to provide a visual representation of the user interface design that outlines the application's structure and layout. The wireframe also shows how various screens will be accessed via various buttons. The user can see which screen will open when they press and release the button according to the arrows that extend from the button to the screen.

## ER diagram
![unit4_erdiagram](https://user-images.githubusercontent.com/111895127/236603554-a630ea69-0334-4f8d-bfdf-9f51f76515b2.png)
Fig x shows the ER diagram for the database that the client requires

This is the ER diagram for the database illustrating the relationship between the “users”, “posts” and “likes” table from the “social_net” database. In the “users” table, there are 5 different columns including id, username email, password, and bio. Each column will have the specific data type after the column name. The second table “posts” has 7 columns which are id, title, rate, content, likes, created_at, and user_id. The third table “likes” has 3 columns id, post_id, and user_id. This diagram also shows that one user can have multiple posts which can have multiple likes.

## Example of the database

![Screen Shot 2023-05-08 at 5 30 23](https://user-images.githubusercontent.com/111895127/236701264-76e3a714-f29c-4beb-9468-19b1762b59f7.png)

Fig x shows the example of the data stored in the "users" table in the "social_net" database

![Screen Shot 2023-05-08 at 5 35 50](https://user-images.githubusercontent.com/111895127/236701422-8ce56a55-12b1-43ff-923f-7b26f0ae07a1.png)

Fig x shows the example of the data stored in the "posts" table in the "social_net" database

![Screen Shot 2023-05-08 at 5 36 52](https://user-images.githubusercontent.com/111895127/236701458-2a1cab37-05ca-4f88-a9b9-3e841a713254.png)

Fig x shows the example of the data stored in the "likes" table in the "social_net" database

## Record of Task
## Internal Structure (Design)
## Test Table
# Criterion C
#Appendix
## Appendix 1: Client interview - Purpose and requirements
![Screen Shot 2023-05-08 at 1 13 49](https://user-images.githubusercontent.com/111895127/236689365-00a6da4e-139c-45c8-9ab0-cc0649e3da41.png)

Fig x shows my notes from the first interview with the client

[^1]: Coursera. “What Is Python Used For? A Beginner’s Guide.” Coursera, 22 Sept. 2021, www.coursera.org/articles/what-is-python-used-for-a-beginners-guide-to-using-python.

[^2]: “Python vs C++: What’s the Difference?” Www.guru99.com, www.guru99.com/python-vs-c-plus-plus.html.

[^3]: “Flask vs Django: What’s the Difference between Flask & Django?” Www.guru99.com, www.guru99.com/flask-vs-django.html.

[^4]: “SQLite Documentation.” Sqlite.org, sqlite.org/docs.html.
