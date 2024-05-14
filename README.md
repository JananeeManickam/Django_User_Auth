# Django_User_Auth
#TASK
Authenticating and signing up users: This involves building an API to sign up the users and store the user details in an appropriate database. The database will have to be designed by the applicant. Registration endpoint should accept all kinds of parameters. Bio fields like - Name, Email, Phone. Identification fields like - Username, Userld. Authentication fields like a password. Care must be taken that passwords should not be stored in plain text. The fields must be checked for validity (passwords must be 8 characters long, usernames should be unique, the name should not have letters, etc) and the API must return a valid error in case something is invalid. Should return a successful message, if everything is valid. Login endpoint • Should accept username and password. Returns a failed message if authentication fails Should return all the Biodata fields of the user in case the username and password match.

Main Components:
  1.Home Page
  2.Sign-up Page
  3.Login Page
  4.Profile Page

Upon arriving at the homepage, users are presented with the option to either sign in or sign up. When signing up, users are prompted to provide essential bio details such as their name, password, email, and phone number. Upon successful registration or login, users are redirected to their personalized profile page.

Here's a brief documentation of the endpoints:

Registration Endpoint:
URL: signup/
Method: POST
Parameters:
Username (string): User's name
Email (string): User's email address
Phone (string): User's phone number
Password(string): User's desired password
Confirm Password(string): Double-check the password.

The password is checked for validity (including all error checks) on signup.

Login Endpoint,
	URL: sign in/
Method: POST
Parameters:
Username (string): User's name
Password(string): User's password

Profile Endpoint,
	URL: profile/
Method: GET
Parameters:
Username (string): User's name
