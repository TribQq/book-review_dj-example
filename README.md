# Book Review django application
###### Heroku [link](https://djbookreview.herokuapp.com/)

## Main purpose:
Provide an opportunity for users to read and write reviews on the books of interest.
## Key concepts:
* Books are added to the database by the admin;
* Every book has a detail page with info, description and reviews sections;
* All books are divided into two categories: anticipated and published;
* List of anticipated books is shown on the main page below greeting section. Anticipated books are not available for reviewing. On the date of publication anticipated book moves to "published" category;
* Published books can be found at "Recent", "Popular" and "Best rated" pages. Every page contains list of published books sorted by appropriate key. Published books can be reviewed;
* Besides that, every book (anticipated or published) can be found via site search. Searching system can be used in 2 ways:
  * By typing a request into the search bar. In this case the search is carried out in all categories (book title, author name, genre and publication year). It means that, if "1984" is typed, list of results will contain all books having "1984" in it's title or published in 1984 year (assuming that such request does not match the name of the author or genre);
  * By clicking author, genre or publication year links. In this case search is carried out in a specific category. For example, if some book is published in 1984 year, and "1984" year link is clicked, list of results will only contain books published in this year (and will not contain Ray Bradbury "1984" titled book!);
* Non-authenticated users can read books info, description and reviews, but they can't write reviews;
* Authenticated users can write reviews, edit or delete them. Every authenticated user has a limit of maximum one review per book;
* After any authentication action (registration, login or logout) user will be redirected to his previous page;
* Review contains its title, body and book rating from 1 to 5. Every book has its average rating affecting its position on the "Best rated" page;
* Authenticated user has a personal page with all written reviews. This page is accessible via "My reviews" link from the main page or by clicking on username link at navigation bar.
## To run application on local machine:
#### 1. Clone the repository:
`git clone https://github.com/TribQq/book-review_dj-example.git && cd book-review`
#### 2. Create a virtual environment:
`virtualenv book_review_env -p python3.10`
#### 3. Activate the virtual environment:
`source book_review_env/bin/activate`
#### 4. Install all required dependencies:
`pip install -r requirements.txt`
#### 5. Collect static files or enable DEBUG in mysite/settings:
`python manage.py collectstatic`
#### 6. Apply the migrations:
`python manage.py migrate`
#### 7. Create superuser:
`python manage.py createsuperuser`
#### 8. Run server:
`python manage.py runserver`
#### 9. From now local version is available at http://localhost:8000
## Testing:
All tests are written with **pytest** framework and **pytest-django** plugin.<br>
To run tests locally use `pytest` command in terminal.

#### Heroku verison [link](https://djbookreview.herokuapp.com/):
##### /admin: 
###### username: adm 
###### password: adm
######  all other users paswords: Password123#