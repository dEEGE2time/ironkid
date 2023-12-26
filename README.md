# IronKid

IronKid is a re-selling website for clothes & accessories. The app is a shop for users to buy, via a "Contact Seller" form. The UI provides admins with a simple and effective ways to create, update and deletion of products.

![Mock Up](docs/readme_images/mockup.png)

## Table of Contents
- [Ironkid](#ironkid)
    - [Table of Contents](#table-of-contents)
- [User Experience and Design](#user-experience-and-design)
    - [The Strategy Plane](#the-strategy-plane)
        - [Site Goals](#site-goals)
        - [User Stories](#user-stories)
            - [User](#user)
            - [Site Owner](#site-owner)
                - [UI](#ui)
                - [Admin Panel](#admin-panel)
    - [The Scope Plane](#the-scope-plane)
    - [The Structure Plane](#the-structure-plane)
        - [Features](#features)
        - [Features to Implement](#features-to-implement)
    - [The Skeleton Plane](#the-skeleton-plane)
    - [The Surface Plane](#the-surface-plane)
    

# User Experience and Design
## The Strategy Plane
### Site Goals
The goal of this project is to create a reselling site with specific styles in fashion from various underground brands. The UI is simple and easy for the owner to create new products, also for the customer to navigate through the website.

### User Stories
#### User
1. As a **user**, I can sign up so that ...
2. As a **user**, I can log in so that ...
3. As a **user**, I can log out so that ...
4. As a **user**, I can browse products so that I can see whats available
5. As a **user**, I can browse products through categories so that I can filter out products
6. As a **user**, I can click on products so that I can view product details
7. As a **user**, I can click click buy so that I get redirected to the cart, where I will verify the product
8. As a **user**, I can contact seller via form so that I can ask questions about the product or show interest.

#### Site Owner
##### UI
1. As a **site owner**, I can create products so that customers can order
2. As a **site owner**, I can view products so that I keep track of stock
2. As a **site owner**, I can update products so that customers receive the right details
3. As a **site owner**, I can delete products so that I can keep the store up to date

##### Admin Panel
1. As a **site owner**, I can view orders so that I can see customer information and product
2. As a **site owner**, I can create categories so that I can sort my products
3. As a **site owner**, I can view categories so that I can see which categories are availabe
4. As a **site owner**, I can update categories so that the categories are correct
5. As a **site owner**, I can delete categories so that the categories are up to date

## The Scope Plane
1. Responsive Design
2. Perform CRUD functionality on products
3. Features with restricted roles to access
4. Home Page with all products
5. Product page with all details of the product
6. Contact form for communication between owner and buyer
7. Hamburger menu for mobile devices

## The Structure Plane
### Features
- [Navbar](#navbar)
- [Footer](#footer)
- [Home-Shop Page](#home-shop-page)
- [Categories Page](#categories-page)
- [Product Detail Page](#product-detail-page)
- [Cart Page](#cart-page)
- [Contact Seller Page](#contact-seller-page)
<hr>

#### Navbar
*recides in base.html*

The navbar remains consistent through all pages of the site and contains allauth options. Navbar will change depending on the user role.

* Logo
    * Visible to all
    * Link to home
* Home
    * Visible to all
    * Link to home
* Shop (Dropdown)
    * Visible to all
    * Dropdown menu to browse categories
* Add Product
    * Visible to owner
    * Link to add product page
* Sign Up
    * Visible to logged out users
    * Link to sign up page
* Login
    * Visible to logged out users
    * Link to login page
* Logout
    * Visible to logged in users
    * Link to logout confirmation page

<details>
    <summary>Mobile</summary>
    <img src="#">
</details>
<details>
    <summary>Authenticated</summary>
    <img src="#">
</details>
<details>
    <summary>Unauthenticated</summary>
    <img src="#">
</details>
<hr>

#### Footer
*recides in base.html*

The footer includes links of all the categories in the shop as well as 3rd party platforms.

<details>
    <summary>Footer</summary>
    <img src="#">
</details>
<hr>

#### Home-Shop Page
*recides in shop.html*

The home page is the shop, this is where the hero image and all available products will display. Each product is displayed as cards in a grid format up to 4 columns. The whole card is clickable for the user to view the product.
Also the implementation of site pagination to prevent the  page from getting too long.

<details>
    <summary>Shop</summary>
    <img src="#">
</details>
<hr>

#### Categories Page
*recides in category.html*

The category page is similar to the home page, difference is that it filters products to the selected category, as well as page title. The url for which category you are in will have a slug.

<details>
    <summary>Tops Category</summary>
    <img src="#">
</details>
<hr>

#### Product Detail Page
*recides in product_detail.html*

The product detail page contains information relevant to the user about the product they clicked on.
<br>
<br>

Product detail fields:
* Name
* Price
* Description
* Size
* Buy Button

From here on out, the user can choose to return to home back via a back button, or can proceed to buy the product.

<details>
    <summary>Product Details</summary>
    <img src="#">
</details>
<hr>

#### Cart Page
*recides in cart_current.html*

The cart page is a simple version of what's to be implemented in the future. For the moment it only holds 1 product. Other than that, it displays the product details for the user to verify. There are two buttons available in this page

* Contact Seller
    * Proceed to contact form
* Back
    * Return to [Product Detail Page](#product-detail-page) of the correct item

<details>
    <summary>Cart</summary>
    <img src="#">
</details>
<hr>

#### Contact Seller Page
*recides in contact_seller.html*

This is the contact form the user has to fill out if they are interested in buying a product. The user will be required to fill in the following information:

* First Name
* Last Name
* Email
* Message
    * A message for showing interest or asking questions about the product

Clicking "Send" will post the user information and their chosen product to the database for the owner to review.

<details>
    <summary>Contact Form</summary>
    <img src="#">
</details>
<hr>

### Features to Implement

add product > manage product in navbar (inside show all crud functionality, remove edit delete from product detail)

profile page

shopping cart for multiple

admin icon when logged in as superuser

contact form auto add profile details

confirm contact form sent to the user