
# Testing

## Manual Testing

### Navigation Bar

#### Hotel-Naif

| # | User Actions                             | Expected Results            | Y/N | Comments                              |
|---|------------------------------------------|------------------------------|-----|---------------------------------------|
| 1 | Click on **Hotel-Naif** in the navbar.   | Redirected to the home page. | Y   | View available rooms and book a room. |

#### About Us

| # | User Actions                         | Expected Results              | Y/N | Comments                         |
|---|--------------------------------------|--------------------------------|-----|----------------------------------|
| 1 | Click on **About Us** in the navbar. | Redirected to the About Us page. | Y   | Read information about the hotel. |

#### Contact

| # | User Actions                           | Expected Results                | Y/N | Comments                                      |
|---|----------------------------------------|----------------------------------|-----|-----------------------------------------------|
| 1 | Click on **Contact** in the navbar.    | Redirected to the Contact page.  | Y   | View contact information and send a message. |

### User Signup

| # | User Actions                                | Expected Results              | Y/N | Comments                 |
|---|---------------------------------------------|--------------------------------|-----|--------------------------|
| 1 | Click on **Signup (User)** in the navbar.   | Redirected to the User Signup page. | Y   | Fill in the signup form. |

### User Login

| # | User Actions                                | Expected Results              | Y/N | Comments                 |
|---|---------------------------------------------|--------------------------------|-----|--------------------------|
| 1 | Click on **Login (User)** in the navbar.    | Redirected to the User Login page. | Y   | Fill in the login form.  |

### Staff Signup

| # | User Actions                                | Expected Results               | Y/N | Comments                 |
|---|---------------------------------------------|---------------------------------|-----|--------------------------|
| 1 | Click on **Signup (Staff)** in the navbar.  | Redirected to the Staff Signup page. | Y   | Fill in the signup form. |

### Staff Login

| # | User Actions                                | Expected Results               | Y/N | Comments                 |
|---|---------------------------------------------|---------------------------------|-----|--------------------------|
| 1 | Click on **Login (Staff)** in the navbar.   | Redirected to the Staff Login page. | Y   | Fill in the login form. |

## Room Booking

### Book a Room

| # | User Actions                             | Expected Results            | Y/N | Comments                              |
|---|------------------------------------------|------------------------------|-----|---------------------------------------|
| 1 | Click on **Book a Room**.                | Redirected to the room booking page. | Y   | - |
| 2 | Fill in the location field.              | Location is filled.         | Y   | - |
| 3 | Select a date for Check-in.              | Date is selected.           | Y   | - |
| 4 | Select a date for Check-out.             | Date is selected.           | Y   | - |
| 5 | Enter the number of persons.             | Number of persons is entered. | Y   | - |
| 6 | Click on **Check Availability**.         | View available rooms.       | Y   | - |
| 7 | Click **Book** for your selected room.   | Confirmation message for the booked room. | Y   | - |

## Contact Page

### Contact Information

| # | User Actions                             | Expected Results            | Y/N | Comments                              |
|---|------------------------------------------|------------------------------|-----|---------------------------------------|
| 1 | Click on **Contact** in the navbar.      | Redirected to the Contact page. | Y   | - |
| 2 | View the address on the Contact page.    | Address is displayed.       | Y   | - |
| 3 | View the phone number on the Contact page.| Phone number is displayed.  | Y   | - |
| 4 | View the Instagram page link.            | Instagram link is displayed.| Y   | - |
| 5 | View the email address on the Contact page.| Email address is displayed.| Y   | - |

### Send Message Form

| # | User Actions                             | Expected Results            | Y/N | Comments                              |
|---|------------------------------------------|------------------------------|-----|---------------------------------------|
| 1 | Fill in your name in the form.           | Name is filled.             | Y   | - |
| 2 | Fill in your email address in the form.  | Email address is filled.    | Y   | - |
| 3 | Fill in your message in the form.        | Message is written.         | Y   | - |
| 4 | Click on **Submit**.                     | Confirmation message that your message has been sent. | Y   | - |

## Staff Dashboard

### Room Management

#### Edit Room

| # | User Actions                             | Expected Results            | Y/N | Comments                              |
|---|------------------------------------------|------------------------------|-----|---------------------------------------|
| 1 | Log in as staff.                         | Redirected to the staff dashboard. | Y   | - |
| 2 | Click on **Rooms** in the Django administration page.| Redirected to the room management page. | Y   | - |
| 3 | Click on the room to edit.               | Redirected to the edit form for the selected room. | Y   | - |
| 4 | Modify the room status.                  | Status is updated.          | Y   | - |
| 5 | Modify the room price.                   | Price is updated.           | Y   | - |
| 6 | Click on **Save**.                       | Changes are saved, and confirmation message is received. | Y   | - |

#### View Dashboard Statistics

| # | User Actions                             | Expected Results            | Y/N | Comments                              |
|---|------------------------------------------|------------------------------|-----|---------------------------------------|
| 1 | Log in as staff.                         | Redirected to the staff dashboard. | Y   | - |
| 2 | View the total number of rooms.          | Total rooms count is displayed. | Y   | - |
| 3 | View the number of available rooms.      | Available rooms count is displayed. | Y   | - |
| 4 | View the number of unavailable rooms.    | Unavailable rooms



# Automated testing


- To run the tests for this project, execute the following commands : **python manage.py test**

  - [Testing](assets/images/testing.png)






# Validation

## HTML Validation:

- HTML validation was done by using the official W3C validator. This checking was done manually by copying the view page source code (Ctrl+U) and pasting it into the validator.






## CSS Validation:

- No errors or warnings were found when passing through the official W3C (Jigsaw) validator.











## Python Validation:

- 





# Lighthouse Report


