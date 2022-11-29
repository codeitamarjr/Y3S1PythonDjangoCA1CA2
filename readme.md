# Django Project

This is an assessment mini-project of Back-End Web Development as part of a BSc in Computing at Dorset College. 11/2022

## Features

- Polls: See the list of polls, vote and see the results, part I of the project ( I have used the Django tutorial as a base for this project), on this task I performed the application of the following concepts: Create the pull model

  Create the pull view ( Showing the results and the total number of votes for each choice)

  Create the pull template

  Create the pull URL

  Create the pull admin

  Create, read, update and delete the pull model

- Log in, log out, create a user, and recover the password, part II of the project, on this task I performed the application of the following concepts:

  Create the user model

  Create the user view

  Create the user template

  Create the user URL

  Create the user admin

  Create, read, update and delete the user model

  Added the login, logout, password reset and password change views

  Implemented the login, logout, password reset and password change templates

  Added the login, logout, password reset and password change URLs

  Added the NAVBAR to the base template, and the login, logout, password reset and password change links

## Roadmap

The main screen is showing the welcome page:
This section uses a file base.html in the templates folder to be the base template of all HTML files.
I am using Bootstrap to save time on the CSS, and the CSS is loaded from an official CDN.
All the remaining pages are extensions of the base.html file.
On this page, the user is required to log in to see polls and vote(The user can see the link but it is protected by one if statement checking if the user is logged in).

- Index page: This page is the home page of the website. It is showing the welcome message and the login form that is saved in the home.html file in the templates folder.

- Log-in system
  The log-in system uses the built-in user authentication system provided by Django, with custom log-in, log-out, create and recovery password pages merged with the Bootstrap template, this HMTL file is located inside registration in the templates folder, the log-in form is customized to be more user-friendly.

- Polls system
  The poll system shows the user the polls and their answer, the user can vote and see the results, also the total number of votes.
  This last method is using the built-in Django aggregation method to get the total number of votes, which sums the number of votes for each poll.
  The poll templates are saved inside the polls folder in the templates folder and they use the base.html file as the base template, as per the Log-in system.

- Top Bar
  This bar is from the Bootstrap examples and the icons changes based on the session( If the user is logged in the menu changes showing the log-out option and the user name, alongside a profile example picture, if the user is not logged in it shows the log-in button and the sign-up button).

## Project

Create a Django-Python-MySQL app to allow users to choose answers from a question database.

## Screenshots

- Welcome screen
  ![Main screen](https://github.com/codeitamarjr/Y3S1djangoAuthExercise/blob/master/screens/1-mail%20screen.png?raw=true)
- Login Page
  ![Login screen](https://github.com/codeitamarjr/Y3S1djangoAuthExercise/blob/master/screens/3-login%20screen.png?raw=true)
- Welcome User
  ![User Welcome screen](https://github.com/codeitamarjr/Y3S1djangoAuthExercise/blob/master/screens/4-welcome%20screen.png?raw=true)
- List of Polls
  ![Polls screen](https://github.com/codeitamarjr/Y3S1djangoAuthExercise/blob/master/screens/1-polls%20screen.png?raw=true)
- Polls Result's
  ![Polls Result screen](https://github.com/codeitamarjr/Y3S1djangoAuthExercise/blob/master/screens/6-result%20screen.png?raw=true)

## Author

- [@codeitamarjr](https://www.github.com/codeitamarjr)

## License

Feel free to use this app under the MIT license.
[MIT](https://choosealicense.com/licenses/mit/)
