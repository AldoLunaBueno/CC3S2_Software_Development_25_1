# CHANGELOG

bd500a9 Add requirements, and done
8ec5339 Green: Add inyection of email service to the initialitation, and implement the logic for send email after add a new user.
134ae86 Iteration 6. Red: Test welcome email sending with a mock for the email service.
02def35 Green: Implement inyection of repo for store users and query for them, and elimination of test for avoid user duplication, because now with the repo it doesn't make sense
61e5820 Iteration 5. Red: Test in-memory user repository that is inyected to UserManager
ac2259e Green: Specify validation of user existance from the method user_exists instead of do it directly from self.users. This lets us mock successfully the existance of the user forcing it.
4daa379 Iteration 4. Red: Test user duplication by adding a user that alredy exists raises an exception.
f5db36c Iteration 3. Red: Test hash method from inyected hashing service to be called once in our add_user method of UserManager.
60d47e1 Green: Implement inyection of hash service dependency and default hash service (trivial, just for avoid braking code)
d42f7a5 Iteration 2. Red: Test user authentication with a fake hash to save the user's password
e071408 Green: Implement method to add user, and a extra method to know if the user exists
8a4a3a9 Iteration 1. Red: Test successful addition of a user
fec6842 First Commit
c84548e Initial commit