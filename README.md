# Josie Annes Patisserie Ecommerce Website

Ecommerce website for the business Josie Anne's Patisserie.

[Link to live site](https://josie-annes.onrender.com//)

## Feature Choice

There are lots of features I'd like to add, but I am under a time crunch so feature ranking will be used to prioritize.

### List of all Features Wanted

All the features wanted for the site and a sub list stating what is involved if more than one thing.

1. Order cake a. Admin – confirm order b. User – order

2. Noticeboard a. User – Add notice b. Admin – Approve notice

3. Book table a. Book table b. Set days tables aren’t available

4. CRUD shop items a. Create b. Read c. Update d. Delete

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
- As a visitor I want to be able to view an item in detail so I can read a description, view the image larger, see the
  ingredients and all other relevant details of the item.
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

## Web Marketing

### Facebook Business Page

Link to created page: https://www.facebook.com/profile.php?id=100087897433792

![Navbar](media/readme-images/fb_marketing/fb1.png)
![Navbar](media/readme-images/fb_marketing/fb2.png)
![Navbar](media/readme-images/fb_marketing/fb3.png)

## Errors

### Reverting all migrations

I tried to revert all migrations near the beginning and ran into this error:

![Reverting all migrations](media/readme-images/errors/revert_migrations.png)

I was able to solve it
with [Instructions found on Stack Overlflow](https://stackoverflow.com/questions/50346326/programmingerror-relation-django-session-does-not-exist)
and running migrations again when I had made changes.

### Internal Server Error 500

I wasn’t getting an error when running locally, and it built fine on Heroku. There were no errors in the console on the
on Heroku. All I was getting as “Internal Server Error 500” (see image below). So I created a new branch from the last
commit and hosted that instead. That actually worked when built in Heroku so from that I knew it was something in the
last commit that was causing the error. After comparing the code to the tutorial I realized I wasn’t missing anything.
So after thinking further I thought it might be something that my local environment had that my Heroku one didn’t. Turns
out I hadn’t added stripe to requirements.txt

![Internal Server Error 500](media/readme-images/errors/internal_server_error_500.png)

### Custom Widget Template does not exist

After checking the paths were all correct I went searching online for a solution. I found
[this solution](https://stackoverflow.com/questions/45844032/django-templatedoesnotexist-in-case-of-a-custom-widget)
on Stack Overflow by user3763125.

![Custom Widget Template does not exist](media/readme-images/errors/internal_server_error_500.png)

### Page Not Found

This was an interesting one. I realized the path I want the app to take wasn't in the list of urls in the below image.
This led me to guess moving my url up in the list would help it be found first and it worked.

![Page Not Found](media/readme-images/errors/url-ranking.png)

## Testing

### Manual Testing

- Responsiveness was tested using Chrome Dev Tools. The site was tested for mobiles, tablets, laptops and desktop
  responsivity.

| Feature Tested                       | Testing Method                                                                                                       | Example                                                            | Result |  
|--------------------------------------|----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|--------| 
| Registration - Blank Field           | - Each mandatory field was left blank intentionally to ensure alert appeared                                         | ![](media/readme-images/testing/empty-field.png)                   | Pass   |
| Registration - Invalid Email Field   | - An invalid email address was tested to ensure error message appeared                                               | ![](media/readme-images/testing/invalid-email.png)                 | Pass   |
| Registration - Common Password       | - A common password was tested to check security                                                                     | ![](media/readme-images/testing/common-password.png)               | Pass   |
| Registration - Short Password        | - A short password was tested to check that an error appears if less than 8 characters entered                       | ![](media/readme-images/testing/password-too-short.png)            | Pass   |
| Registration - Short Username        | - A short username was tested to check that an error appears if less than 4 characters are entered                   | ![](media/readme-images/testing/short-username.png)                | Pass   |
| Registration - Email Verification    | - When new account is set up user should be asked to verify the email address before logging in for the first time.  | ![](media/readme-images/testing/verify-email.png)                  | Pass   |
| Registration - Email Confirmation    | - When new account is set up user should be sent a verification email to the email address used during registration. | ![](media/readme-images/testing/registration-email.png)            | Pass   |
| Sign-In - - Blank Field              | - Each mandatory field was left blank intentionally to ensure alert appeared                                         | ![](media/readme-images/testing/password-blank.png)                | Pass   |
| Sign in - Incorrect Username Field   | - Tested with incorrect spelling and capitalisation of some letters to ensure account security                       | ![](media/readme-images/testing/incorrect-username.png)            | Pass   |
| Sign in - Incorrect Password Field   | - Tested with incorrect spelling and capitalisation of some letters to ensure account security                       | ![](media/readme-images/testing/incorrect-password.png)            | Pass   |
| Non-Signed in user - Profile menu    | - Only logged in users have access to full profile menu options                                                      | ![](media/readme-images/testing/profile-only-on-signin.png)        | Pass   | 
| Signed in user - review              | - User can update their profile information when signed in.                                                          | ![](media/readme-images/testing/update-profile.png)                | Pass   | 
| Signed in user - update profile      | - The product details page contains correct information about the product.                                           | ![](media/readme-images/testing/product-detail.png)                | Pass   | 
| *Signed in user - Profile menu Admin | - Only admin can see the link to admin site                                                                          | ![](media/readme-images/testing/.png)                              | Pass   |
| Signed in user - Checkout            | - Correct details are displayed on checkout screen and payment details not stored                                    | ![](media/readme-images/testing/correct-deatils-at-checkout.png)   | Pass   |
| Site Alert - sign in                 | - Alert to confirm User successfully signed in.                                                                      | ![](media/readme-images/testing/sign-in-success.png)               | Pass   |
| Site Alert - sign out                | - Alert requests user to confirm choice before logging out of site.                                                  | ![](media/readme-images/testing/sign-out-confirm.png)              | Pass   | 
| Site Alert - sign out                | - Alert to confirm successful signing out.                                                                           | ![](media/readme-images/testing/sign-out.png)                      | Pass   |
| Newsletter                           | - Signs up email to newsletter                                                                                       | ![](media/readme-images/testing/newsletter.png)                    | Pass   |
| Cart - product added                 | - Alert displayed with correct details when product added to cart                                                    | ![](media/readme-images/testing/product-added-to-cart.png)         | Pass   | 
| Cart - quantity updated              | - Alert displayed with correct details when cart is updated                                                          | ![](media/readme-images/testing/quantity-updated.png)              | Pass   |
| Cart - product removed               | - Alert displayed with correct details when product is removed from cart                                             | ![](media/readme-images/testing/product-removed.png)               | Pass   |
| Checkout incomplete details          | - Checkout does not process if all mandatory details with * are filled in.                                           | ![](media/readme-images/testing/checkout-incomplete-details.png)   | Pass   |
| Checkout - save details              | - Save details to profile option works correctly when selected                                                       | ![](media/readme-images/testing/details-updated-from-checkout.png) | Pass   |
| Stripe - incorrect number            | - Only cards with completed and valid card numbers can be accepted for payments                                      | ![](media/readme-images/testing/incorrect-card-number.png)         | Pass   |
| Stripe - incomplete date             | - Only cards with completed valid date can be accepted for payments                                                  | ![](media/readme-images/testing/incomplete-stripe-date.png)        | Pass   |
| Stripe - expired card                | - Only cards with expiry date in the future can be accepted for payments                                             | ![](media/readme-images/testing/expired-stripe-date.png)           | Pass   |
| Stripe - incomplete security code    | - Only cards with complete security code can be accepted for payments                                                | ![](media/readme-images/testing/incomplete-stripe-sec-code.png)    | Pass   |
| Stripe - incomplete ZIP code         | - Only cards with completed and valid ZIP code can be accepted for payments                                          | ![](media/readme-images/testing/incomplete-stripe-zip.png)         | Pass   |
| User Profile - Order History         | - Order history available on profile page.                                                                           | ![](media/readme-images/testing/order-history.png)                 | Pass   |
| Order Confirmation - notification    | - Alert is displayed correctly with users email and order number.                                                    | ![](media/readme-images/testing/order-confirm-notification.png)    | Pass   |
| Order Success Page                   | - This page provides the user with a summary of their order, the shipping details, and the overall cost.             | ![](media/readme-images/testing/order-confirm-page.png)            | Pass   | 
| Admin CRUD functionality             | - The admin account has access to create, update and delete products, user information, newsletter subscribtions etc | ![](media/readme-images/testing/admin-crud.png)                    | Pass   | 
| Admin - restricted access            | - Only the admin account can log into the admin view panel.                                                          | ![](media/readme-images/testing/admin-no-access.png)               | Pass   |
| Error404 - Display                   | - Page displayed when incorrect url is searched for and redirect to home page works.                                 | ![](media/readme-images/testing/page-not-found.png)                | Pass   |
| Afternoon Tea Form - Blank field     | - All fields are needed to submit form for afternoon tea                                                             | ![](media/readme-images/testing/error-afternoon-tea.png)                | Pass   |
| Afternoon Tea Form - Success         | - Successfully submitted form for afternoon tea                                                                      | ![](media/readme-images/testing/afternoon-tea.png)                | Pass   |
| Cake Form - Blank field              | - All fields are needed to submit form for ordering cake                                                             | ![](media/readme-images/testing/order-cake-error.png)                | Pass   |
| Cake Form - Success                  | - Successfully submitted form to order cake                                                                          | ![](media/readme-images/testing/cake-order.png)                | Pass   |

#### Validation Testing:

| Resource Used                                                                            | Code Tested                        | Example                                              | Result |  
|------------------------------------------------------------------------------------------|------------------------------------|------------------------------------------------------|--------| 
| <a href="https://jshint.com/">JSHint </a>                                                | JavaScipt files                    |                                                      | Pass   |
| <a href="https://jigsaw.w3.org/css-validator/#validate_by_input"> W3C CSS Validator </a> | All CSS files                      | ![](media/readme-images/testing/css-validation.png)  | Pass   | 
| <a href="https://validator.w3.org/nu/#textarea"> Html Checker  </a>                      | All HTML source code was validated | ![](media/readme-images/testing/html-validation.png) | Pass   | 
| pycodestyle                                                                              | all files containing Python code   |                                                      | Pass   | 

#### Lighthouse Testing

- Lighthouse was used to check perfomance and accessiblitiy. Performance surfers from initial server response time being
  on render.
  ![](media/readme-images/testing/lighthouse.png)

#### Security

- All SECRET access keys are stored safely in the env.py file to prevent unwanted connections to the database.
- Django’s setting DEBUG was set to False after development for deployment to prevent access to error screens revealing
  code or database entries.
- Django allauth was used to set up user registration and Django’s LoginRequiredMixin and UserPassesTestMixin were used
  to ensure only signed-in users and authors can edit and delete their product reviews.
- Cross-Site Request Forgery (CSRF) tokens were used on all forms throughout this site to prevent valid requests to the
  backend server from being created for malicious purposes.

## Deployment

**Josie Anes Patisserie** was developed using the **PyCharm IDE**, and using **Git** and **GitHub** for version control.
It is hosted on **Heroku** and all media files are hosted in **Cloudinary**.

Before deploying the application, install the following:

- Python 3
- PIP
- Git
- Heroku CLI

### Local Deployment

To deploy josie-annes-patisserie locally, take the following steps:

1. From the applications' [repository](https://github.com/sean-meade/josie-annes-patisserie), click the *code* button
   and download the zip file.

   Alternatively, you can clone the repository using the following line in your command prompt:

```terminal
git clone https://github.com/sean-meade/josie-annes-patisserie
```

2. Access the folder in your terminal window and install the application's required modules with the following command:

```terminal
pip3 install -r requirements.txt
```

3. Create the following environmental variables on your machine:

```
DATABASE_URL = YOUR_DATABASE_URL
SECRET_KEY = YOUR_DJANGO_SECRET_KEY
CLOUDINARY_URL = YOUR_CLOUDINARY_KEY
DEBUG = True (False for production)
STRIPE_PUBLIC_KEY = YOUR_STRIPE_PUBLIC_KEY
STRIPE_SECRET_KEY = YOUR_STRIPE_SECRET_KEY
STRIPE_WH_SECRET = YOUR_STRIPE_WH_SECRET

```

4. In your IDE terminal, migrate the models to create the database using the following commands:

```terminal
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser to access the admin panel using the following command:

```terminal
python manage.py createsuperuser
```

Then follow the instructions to create the superuser.

6. After you login to the admin panel, you can add data to be displayed in your app. Refer
   to [database modeling](#database-modelling).


7. To initiate the application, type the command `python manage.py runserver` in your terminal. The application is now
   available in your browser at the address: `http://127.0.0.1:8000/`

[Back to content](#contents)

### Deployment to Heroku

To deploy the app to Heroku, use the following steps:

3. Clone the repository like above.
4. Push these newly created files to your repository master.
5. Login to Heroku and create a new app.
6. In Heroku dashboard of the new app, click **deploy**, then **deployment** method and select **GitHub** to connect
   your app to your github repository for automatic deployment.
7. In Heroku Resources tab, navigate to **Add-Ons** section and search for **Heroku Postgres**. I recommend you choose
   hobby level for this application. You should also search for **Cloudinary - Image and Video Management** to ensure
   your media files load to Cloudinary.
8. In settings tab, navigate to **Reveal Config Vars** and add the following variables:

| **KEY**           | **VALUE**               |
|-------------------|-------------------------|
| CLOUDINARY_URL    | YOUR_CLOUDINARY_URL     |
| DATABASE_URL      | YOUR_DATABASE_URL       |
| DEBUG_BOOL        | YOUR_DEBUG_BOOL         |
| SECRET_KEY        | YOUR_DJANGO_SECRET_KEY  |
| STRIPE_PUBLIC_KEY | YOUR_STRIPE_PUBLIC_KEY  |
| STRIPE_SECRET_KEY | YOUR_STRIPE_SECRET_KEY  |
| STRIPE_WH_SECRET  | YOUR_STRIPE_WH_SECRET  |

9. In settings.py in your IDE, temporarily comment out the database and use below code instead (make sure you do not
   commit!):

```python
DATABASES = {
    'default': dj_database_url.parse('POSTGRESS URL')
}
```

10. In terminal, migrate the models to create the Postgress database using the following commands:

```terminal
python manage.py makemigrations
python manage.py migrate
```

11. Create a superuser to access the admin panel using the following command:

```terminal
python manage.py createsuperuser
```

Then follow the instructions to create the superuser.

12. After you login to the admin panel, you can add data to be displayed in your app if required.

13. Remove the temporary database from settings.py and uncomment the original code, then push the code to origin.
14. Back to in **Heroku dashboad**, deploy the application.
15. To view the site, click on **View App**.

## Technology Used

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