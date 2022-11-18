# Josie Annes Patisserie Ecommerce Website
Ecommerce website for the business Josie Anne's Patisserie.

[Link to live site](https://josie-annes-patisserie.herokuapp.com/)

## Feature Choice

There are lots of features I'd like to add, but I am under a time crunch so feature ranking will be used to prioritize.

### List of all Features Wanted

All the features wanted for the site and a sub list stating what is involved if more than one thing.

1. Order cake

    a. Admin – confirm order

    b. User – order

2. Noticeboard

    a. User – Add notice

    b. Admin – Approve notice

3. Book table

    a. Book table

    b. Set days tables aren’t available

4. CRUD shop items

    a. Create

    b. Read

    c. Update

    d. Delete

5. Navigation

    a. Navbar

    b. Footer

6. View user details

    a. Personal

    b. Past orders

    c. Table booking status

    d. Cake order Status

7. Edit user details

    a. Personal

8. Rate a product

9. Leave a review

10. Check out and pay for items

11. Shopping cart

    a. Visitor/User - Add items

    b. Visitor/User - Remove items

12. Authentication

    a. Registration

    b. Sign in

    c. Sign out

13. Sign up for newsletter

14. View items

    a. Detailed view

    b. List of items

    c. Filter items

### Feature Ranking

| Feature No. | Feature                     | Importance | Feasibility |
|-------------|-----------------------------|------------|-------------|
| 1           | Order cake                  | 3          | 2           |
| 2           | Noticeboard                 | 3          | 2           |
| 3           | Book table                  | 2          | 3           |
| 4           | CRUD shop items             | 5          | 5           |
| 5           | Navigation                  | 5          | 5           |
| 6           | View user details           | 4          | 5           |
| 7           | Edit user details           | 3          | 5           |
| 8           | Rate a product              | 3          | 4           |
| 9           | Leave a review              | 2          | 3           |
| 10          | Check out and pay for items | 5          | 5           |
| 11          | Shopping cart               | 5          | 5           |
| 12          | Authentication              | 5          | 5           |
| 13          | Sign up for newsletter      | 5          | 5           |
| 14          | View items                  | 5          | 5           |


![Image highlighting feature rankings](media/readme-images/feature-rankings.png)

#### Final ranking
| Feature No. | Feature                      |
|-------------|------------------------------|
| 12          | Authentication               |
| 4           | CRUD shop items              |
| 5           | Navigation                   |
| 10          | Check out and pay for items  |
| 11          | Shopping cart                |
| 13          | Sign up for newsletter       |
| 14          | View items                   |
| 6           | View user details            |
| 7           | Edit user details            |
| 8           | Rate a product               |
| 1           | Order cake                   |
| 2           | Noticeboard                  |
| 3           | Book table                   |
| 9           | Leave a review               |


## User Stories

### Visitors User Stories
- As a visitor I want to be able to view all the items for sale 
- As a visitor I want to be able to view the Homepage
- As a visitor I want to be able to filter all the items by price, category, and ingredients
- As a visitor I want to be able to view an item in detail so I can read a description, view the image larger, see the ingredients and all other relevant details of the item.
- As a visitor I want to be able to sign up for a newsletter
- As a visitor I want to be able to register as a user 
- As a visitor I want to be able to add items to my shopping cart
- As a visitor I want to be able to check out and pay for items in my shopping cart
- As a visitor I want to be able to navigate through the site

### User Stories
- As a user I want to be able to sign in 
- As a user I want to be able to sign out
- As a user I want to be able to select items and add them to my shopping cart
- As a user I want to be able to select items and remove them to my shopping cart
- As a user I want to be able to check out and pay for items in my shopping cart
- As a user I want to be able to add a notice to noticeboard for review
- As a user I want to be able to leave a review
- As a user I want to be able to rate a product
- As a user I want to be able to book a table
- As a user I want to be able to order a cake
- As a user I want to be able to view my details
- As a user I want to be able to edit my details

### Admin User Stories
- As admin I want to be able to CRUD items for shop
- As admin I want to be able to approve notices
- As admin, I want to be able to approve booking of a table
- As an admin I want to be able to confirm the order of a cake
- As an admin I want to be able to set the days that tables are available

## Data Models

### Product Model

| Key         | Name        | Type         | Extra Info      |
|-------------|-------------|--------------|-----------------|
| ForeignKey  | category    | Category     |                 |
|             | sku         | CharField    |                 |
|             | name        | CharField    |                 |
|             | description | TextField    |                 |
|             | price       | DecimalField |                 |
|             | rating      | DecimalField |                 |
|             | image_url   | URLField     |                 |
|             | image       | ImageField   |                 |
|             | hidden      | BooleanField |                 |
|             | ingredients | TextField    |                 |
|             | allergens   | Allergens    | ManyToManyField |

### Allergen Model

| Key | Name    | Type       | Extra Info |
|-----|---------|------------|------------|
|     | allergy | CharField  | choices    |

### Category Model

| Key | Name          | Type       | Extra Info |
|-----|---------------|------------|------------|
|     | name          | CharField  |            |
|     | friendly_name | CharField  |            |

### Order Item Model

| Key        | Name           | Type         | Extra Info |
|------------|----------------|--------------|------------|
| ForeignKey | order          | Order        |            |
| ForeignKey | product        | Product      |            |
|            | quantity       | IntegerField |            |
|            | lineitem_total | DecimalField |            |

### Order Model

| Key         | Name            | Type          | Extra Info |
|-------------|-----------------|---------------|------------|
|             | order_number    | CharField     |            |
| Foreign Key | user_profile    | UserProfile   |            |
|             | full_name       | CharField     |            |
|             | email           | EmailField    |            |
|             | phone_number    | CharField     |            |
|             | country         | CountryField  |            |
|             | eircode         | CharField     |            |
|             | town_or_city    | CharField     |            |
|             | street_address1 | CharField     |            |
|             | street_address2 | CharField     |            |
|             | county          | CharField     |            |
|             | date            | DateTimeField |            |
|             | delivery_cost   | DecimalField  |            |
|             | order_total     | DecimalField  |            |
|             | grand_total     | DecimalField  |            |
|             | original_bag    | TextField     |            |
|             | stripe_pid      | CharField     |            |

### Afternoon Tea booking Model

| Key | Name           | Type                 | Extra Info        |
|-----|----------------|----------------------|-------------------|
|     | booking_number | CharField            |                   |
|     | full_name      | CharField            |                   |
|     | email          | EmailField           |                   |
|     | phone_number   | CharField            |                   |
|     | date           | DateField            |                   |
|     | time           | CharField            |                   |
|     | notes          | TextField            |                   |
|     | under_review   | BooleanField         |                   |
|     | no_of_people   | PositiveIntegerField | limit to 6 people |

### Cake Order Model

| Key | Name              | Type         | Extra Info |
|-----|-------------------|--------------|------------|
|     | cake_order_number | CharField    |            |
|     | full_name         | CharField    |            |
|     | email             | EmailField   |            |
|     | phone_number      | CharField    |            |
|     | date              | DateField    |            |
|     | notes             | TextField    |            |
|     | under_review      | BooleanField |            |

### User Profile Model

| Key | Name                    | Type         | Extra Info     |
|-----|-------------------------|--------------|----------------|
|     | user                    | User         | OneToOneField  |
|     | default_phone_number    | CharField    |                |
|     | default_street_address1 | CharField    |                |
|     | default_street_address2 | CharField    |                |
|     | default_town_or_city    | CharField    |                |
|     | default_county          | CharField    |                |
|     | default_eircode         | CharField    |                |
|     | default_country         | CountryField |                |

## Design choices

### Sitemap

![Sitemap](media/readme-images/wireframes/site-map-first-draft.jpg)

### Wireframes

#### Header

![Header](media/readme-images/wireframes/navbar.jpg)

#### Homepage

![Homepage](media/readme-images/wireframes/homepage.jpg)
![Homepage 2](media/readme-images/wireframes/homepage-2.jpg)

#### Footer

![Footer](media/readme-images/wireframes/footer.jpg)

#### Booking Afternoon Tea

![Booking Afternoon Tea](media/readme-images/wireframes/)

#### Order Cake

![Order Cake](media/readme-images/wireframes/)


## Features

### Navbar

#### Navbar desktop

![Navbar](media/readme-images/features/navbar.png)
![Navbar](media/readme-images/features/navbar2.png)

#### Navbar mobile

![Navbar Mobile](media/readme-images/features/navbar-mobile.png)

## Homepage

#### Links to stores

![Links to stores](media/readme-images/features/links-to-shop.png)

#### Product Card Homepage

![Product Card Homepage](media/readme-images/features/product-card-homepage.png)

#### Newsletter Sign Up

![Newsletter Sign Up](media/readme-images/features/newsletter-signup.png)

#### Afternoon Tea Link on Homepage

![Afternoon Tea Link on Homepage](media/readme-images/features/link-to-afternoon-tea.png)

## Footer

### Footer Nav

![Footer Nav](media/readme-images/features/footer-nav.png)

### Footer Social Media Links

![Footer Social Media Links](media/readme-images/features/footer-social-media.png)

## Store

### Product Search Bar

![Product Search Bar](media/readme-images/features/product-search-bar.png)

### Product Filters

![Product Filters](media/readme-images/features/product-filters.png)

### Product Card in Products page

![Product Card in Products page](media/readme-images/features/product-card-shop.png)

## Booking Afternoon Tea Form

![Booking Afternoon Tea Form](media/readme-images/features/booking-afternoon-tea.png)

## Order Cake Form

![Order Cake Form](media/readme-images/features/order-cake.png)

## Product Detail Page Quantity, Keep Shopping, and Add to Cart

![Product Detail Page Quantity, Keep Shopping, and Add to Cart](media/readme-images/features/product-detail.png)

## Messages

### Success Pop Up

![Success Pop Up](media/readme-images/features/success-pop-up.png)

### Successful Checkout

![Successful Checkout](media/readme-images/features/successful-checkout.png)

## Cart Functionality

![Cart Functionality](media/readme-images/features/cart-functionality.png)

## Secure Checkout

### Checkout Form

![Secure Checkout](media/readme-images/features/checkout1.png)
![Secure Checkout 2](media/readme-images/features/checkout2.png)

### Loading Screen

![Loading Screen](media/readme-images/features/loading-screen.png)

###

![Navbar](media/readme-images/features/)
![Navbar](media/readme-images/features/)



## Things I used to help

- [ShareX](https://getsharex.com/): Screenshots
- [TableConvert](https://tableconvert.com/markdown-generator): README table generation
- [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/): Styling
- [Google Fonts](https://fonts.google.com/specimen/Sacramento): Sacramento font
- [CUFON Fonts](https://www.cufonfonts.com/font/glacial-indifference): Glacial Indifference Font
- [flaticon](https://www.flaticon.com/): Icons
- [LUNAPIC](https://www12.lunapic.com/editor/): Image editing
- [Django](https://www.djangoproject.com/): Python web framework
- [SQlite3](https://www.sqlite.org/index.html): Database used in production
- [PostgreSQL](https://www.postgresql.org/): Database used in development
- [FontAwesome](https://www.bootstrapcdn.com/fontawesome/): Icons
- [jQuery](https://jquery.com/): Common JS library for web development
- [Heroku](https://dashboard.heroku.com/apps): Free hosting
- [PyCharm](https://www.jetbrains.com/pycharm/): IDE for Python development
- []():
- []():
- []():