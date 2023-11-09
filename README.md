# Hotel-Naif

![Hotel-Naif](assets/images/screen-view.png)



## Description

[Hotel-Naif]() is a modern hotel booking and reservation website that provides users with a seamless experience for reserving rooms in a hotel. It offers a user-friendly interface with features like user sign-up, login, room selection, booking .
Staff members have access to a management panel where they can oversee reservations, add or remove rooms, and control room availability.
This project is built using Python, Django, HTML, JavaScript, and Bootstrap, ensuring a reliable and responsive web application. With a focus on a hassle-free booking experience, Hotel-Naif caters to both users and staff members, simplifying the hotel reservation process.



------------------------------------------------------------------------------


## Technology Used

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Django](https://en.wikipedia.org/wiki/Django_(web_framework))
- [HTML](https://en.wikipedia.org/wiki/HTML)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Bootstrap](https://en.wikipedia.org/wiki/Bootstrap_(front-end_framework))



------------------------------------------------------------------------------

## Installation

1. Install Poetry, a Python dependency management and packaging tool:
- pip install poetry

2. Install project dependencies using Poetry:
- poetry install


--------------------------------------------------------------------------------


## Running the Website

1. Navigate to the project directory: 
- cd hotel

2. Apply database migrations to set up the database:
- python manage.py migrate

3. Start the development server:
- python manage.py runserver


4. Access the website in your browser at:
- 

5. Staff login use :
- Username: naif
- Password: Test 



---------------------------------------------------------------------------------



## User Features

#### As a User, you can:

- Sign up and log in to your account.
- Choose your check-in and check-out dates.
- Specify the number of guests.
- Check room availability based on your preferences.
- Browse different types of rooms, each with its own features and pricing.
- Easily book a room.


#### About Us Page

- Explore information about our hotel and team.
- Learn more about the people behind the scenes and our vision.



#### Contact Us Page
- Contact the hotel easily through the "Contact Us" page.
- Send us a message using the contact form.
- Find our contact details for alternative communication.





## Staff Features

#### As a Staff member, you can:

- Login to your staff account.
- Secure staff login with authentication.
- Staff members can create accounts via a user-friendly signup process.
- Manage reservations and room availability.
- Add or remove new rooms and locations.
- Add new rooms with room types, capacity, price, and availability status.




-------------------------------------------------------------------------------



## Room Types


1. Quad Bedroom
- Price: $55/day
- Size: 30 ft
- Allowed Guests: Max 3 persons
- Amenities: Free Wifi, TV, Private Bathroom, Hair Dryer
- Nearby: Cinema, Restaurants, Shopping Mall, Sea View

2. Penthouse
- Price: $100/day
- Size: 250 ft
- Allowed Guests: Max 3 persons
- Amenities: Free Wifi, TV, Private Bathroom, Hair Dryer
- Nearby: Cinema, Restaurants, Shopping Mall, Sea View

3. Suite
- Price: $200/day
- Size: 400 ft
- Allowed Guests: Max 5 persons
- Amenities: Free Wifi, TV, Private Bathroom, Hair Dryer
- Nearby: Cinema, Restaurants, Shopping Mall, Sea View



-----------------------------------------------------------------------------------



## Bugs and Remaining Bugs


#### Bugs 


1. **Bug Description:** There was an issue with incorrect room availability being displayed to users. The bug caused rooms to be shown as available even when they were already reserved.



* **How bug solved:**



  - In the **'home'** view function, I needed to correct the logic that checks room availability. I was using a list of room reservations, but we needed to check each reservation to see if it overlapped with the user's requested check-in and check-out dates.

 
   - `for each_reservation in Reservation.objects.all():
    if (
        each_reservation.check_in_date < request.POST["cin"]
        and each_reservation.check_out_date < request.POST["cout"]
    ):
        pass
    elif (
        each_reservation.check_in_date > request.POST["cin"]
        and each_reservation.check_out_date > request.POST["cout"]
    ):
        pass
    else:
        room_reservations.append(each_reservation.room.id)`
        

   - Once I identified reserved rooms, I used the exclude method to exclude them from the query set of      available rooms.


 
   - `rooms = (
    Rooms.objects.all()
    .filter(
        hotel=hotels, max_capacity=int(request.POST["capacity"])
    )
    .exclude(id__in=room_reservations))`

   - By applying these changes to the code, I fixed the bug that was causing incorrect room availability to be displayed. Users now see accurate room availability based on their requested check-in and check-out dates.






2. **Bug Description:** There was an issue with editing room details on the staff panel. The bug caused the changes made to room details not to be saved.




* **How bug solved:**



  - In the **'edit_room'** view function, I identified the issue in the code that updates the room details. 
    The problem was that the wrong variable names were being used in the code.


  - `old_room = Rooms.objects.all().get(id=int(request.POST["roomid"]))
   hotel = Hotels.objects.all().get(id=int(request.POST["hotel"]))`


  - These lines should be changed to use the correct variable names:


  -  `old_room = Rooms.objects.all().get(id=int(request.POST["room_id"]))
    hotel = Hotels.objects.all().get(id=int(request.POST["hotel"]))`


  - By making these changes to the code, I fixed the bug that was causing incorrect room edits on the staff panel. Staff members can now successfully update room details, and the changes are saved as expected.





#### Remaining Bugs

- None 




------------------------------------------------------------------------------------







