# **SeedLink** - by Planters

# [SeedLink](https://seed-link.herokuapp.com/)

## **Deployed site**
The live website can be found at the following link; [SeedLink](https://seed-link.herokuapp.com/).

![SeedLink Mockup](assets/images/seedlink-responsive.png)

## 1. **UX**
This project is part of the Code Institue Hackaton for Earth Day.
The Planters team have decided to build this Seedlink project to encourage people to do their part for the enviroment and their local community. Seedlink is a site for ordering seeds and sharing produce with the aim of promoting plant based eating, helping the environment and local community. Users are encourage to orders seeds and start growing in their own home to fight climate change. They are able to donate any excess produce to the marketplace and share with the local community to reduce foodwaste.

### **User Stories**

-	I want to be able to log on and order seeds easily.
-	I want to be able to donate my surplus vegetables easily
-	I want to be able to quickly see when the next market day is
-	I want it to be easy to sign in.
-	I want to be able to give back to my local community
-	I want to be able to grow a tree in my back garden

#### Users

- SeedLink is aimed at people who want to do their bit for the environment and their local community. The users of this site will have an interest in plant-based eating and growing their fruit and vegetables at home.  They will have an interest in swapping vegetables with other growers and sharing with others in need.

#### Site Owner Goals
-	I want the site to be intuitive and easy to use
-	I want the users to be able to log in easily 
- I want to encourage repeat visits to the site

#### General
- As a user I want to receive clear feedback for my actions on the site, so I know they are complete or if further steps are needed.

### **Structure**
Overview of site and page structure, explaining functionality and purpose.

#### Home Page:
  * **Navigation Bar/Footer**: For easy navigation across the site and to external resources such as social media pages.
  * **Website Logo**: To easily identify the 'SeedLink’' site branding.
  * **Site Features**: To easily provide users with an overview of the website’s features.
  
#### Order Seeds Page
 * **Name Input**: Text input box, allowing users to enter their Name.
 * **Address Input**: Text input box, allowing users to enter their address.
 * **Seed category Input**: Text input box, allowing users to choose seed category.
 * **Quantity Input**: Text input box, allowing users to enter their desired quantity of the seeds.
 * **Order Now Button**: To allow users to submit entered information and order the seeds.
 
#### Sign In Page:
 * **Username Input**: Text input box, allowing users to enter their username.
 * **Password Input**: Text input box, allowing users to enter their password.
 * **Sign In Button**: To allow users to submit entered information, and if correct credentials will be directed to the profile page.
 * **Sign Up  Button**: To allow users to be directed to the registration page.

#### Sign Up Page:
 * **First Name Input**: Text input box, allowing users to enter their First Name.
 * **Last Name Input**: Text input box, allowing users to enter their Last Name.
 * **Username Input**: Text input box, allowing users to enter their username.
 * **Email Input**: Text input box, allowing users to enter their email address.
 * **Password Input**: Text input box, allowing users to enter their password.
 * **Sign Up Button**: To allow users to submit entered information and register for an account.

#### Profile Page:
 * **Profile Card**: To easily provide users key information of their own profile, including visual image, type of member, full name, birthday, location and date joined.
 * **Update Profile Button**: To allow users to edit their profile with easy access.

#### Donation Page:
 * **Produce category Input**: List of selectoion allowing users to choose produce category.
 * **Produce Name Input**: Text input box, allowing users to enter the name of the produce.
 * **Quantity Input**: Text input box, allowing users to enter the quantity they are willing to donate.
 * **Expiry date Input**: To allow users to enter the expiry date of the produce. 
 * **Donate Button**: To allow users to submit entered information and donate their produce.

#### Marketplace:
 * **Marketplace info**: To provide users details of the marketplace
 * **Produce cards**: To provide key information of the produce, including quantiy and expiry date.
 
### **Skeleton**

At this point I began creating wireframes, using the above structure considerations. I used [Balsamiq](https://balsamiq.com/) these below;

* [Home Page](assets/README/wireframes/wireframe-index.html.png)
* [Profile Page](assets/README/wireframes/wireframe-profile.html.png)
* [Login / Registration Page](assets/README/wireframes/wireframe-register-login.html.png)

### **Surface**

This is the sensory design section of a website, or how it looks, feels and sounds.

![Seedlink Logo](static/images/logo.gif)

#### **Colour & Styling**


The resulting palette is below;

![Seedlink Color Scheme](assets/README/images/color-palette.png)

##### Colour Palette



#### **Language/Tone**


#### **Styling Considerations**

During the pre-development phase, I listed out some styling ideas that I thought would be beneficial to the website. Many of these can be found in wireframes.

* Font Awesome Icons : with hover effects to highlight key info 
* Navigation
* Sticky top
* Mobile Side Nav: 'Burger' menu icon, expanding into side navbar on click
* Logo: Navigates to the index page on click


## 2. **Features**
The site allows users to register for an account. They are then able to login and logout of the site. They can create and update their own profiles. Registered users are able to upload their donations onto the marketplace database. Any site users can view what produce is available on the marketplace.

### CRUD Functionality

Users can :

- Add their profile
- Edit their profile
- Add Donations
- Add seeds order request

### **Existing Features**
#### The Header:
* **Website Logo**: Builds brand awareness and identity amongst users.
* **Navigation Bar**: Enable users to navigate the site easily and intuitively, as well as login/register their account.

#### The Footer:
* **Copyright**: Copyright information for brand awareness.
* **Social Links**: Links to Social Media for brand awareness.

Both the Header and Footer are present and consistent on all website pages.

#### Home page:
* **Website Logo**: Visually pleasing design, allowing users to immediately identify the site brand.
* **Sign Up Button**: Allows users to be directed to the registration page to sign up for an account.
* **Site Features**: Brief content showing site features.
* **Recent Produce**: Cards showing recent produce donated to the marketplace.

#### My Profile:
* **Profile Card**: Card showing relevant information on users profile, allowing users to quickly identify if they are using their desired account.
* **Add Profile Button**: To allow users to create their profile.
* **Update Profile Button**: To allow users to edit their profile with easy access.

#### Add Profile page:

* **Input areas for below profile data points**:
    * **Full name** - Text
    * **Birthday** - Date
    * **Location** - Text
    * **Profile Image** - Url or default img

#### Edit Profile page:

* **Input areas for below profile data points**:
    * **Full name** - Text
    * **Birthday** - Date
    * **Location** - Text
    * **Profile Image** - Url or default img

#### Sign Up Page:

* **Input areas for below registration data points**:
  * **First Name** - Text
  * **Last Name** - Text
  * **Username** - Text
  * **Enail** - Text
  * **Password** - Text


#### Order Seeds Page:

* **Input areas for below seeds ordering data points**:
  * **Name** - Text
  * **Address** - Text
  * **Seed Category** - Text
  * **Quantity** - Selector

 
#### Donation Page:

 * **Input areas for below seeds donation points**:
 * **Produce Category** - Selector
 * **Quantity** - Text
 * **Expiry Date** - Date


#### Marketplace:
 * **Marketplace info**: To provide users details of the marketplace
 * **Produce cards**: To provide key information of the produce, including quantiy and expiry date.

### **Features to consider implementing in future**

  * **Image Upload**: Use Cloudinary to support image upload
  * **Reservation**: Implement a reservation / ticketed system for users to reserve produce at the marketplace to avoid disappointments
  * **Contact US**: Add a contact us page to allow users to communicate with Seedlink and implement with EmailJs.
* **Social Media Sharing** - Allow users to share available produce on the marketplace directly to their social media accounts.
* **Chat functionality** - Allows registered users to private message individual members and order surplus produce directly.
* **Advanced User Profile** - Allow users to customize their own profile with custom information they wish to provide and share with other members.

## 3. **Database Design**
MongoDB was the database solution used for the website development, using the below, structured plan.

**Users Collection**

| **Key**        |  **Type**     | **Purpose**|
|-------------- |-------------- |-------------|
| _id           |  ObjectId     | ObjectId of this document
| firstname     |   String      | stores the first name of the user 
| lastname      |   String      | stores the last name of the user 
| username      |   String      | stores the username of the user 
| email         |   String      | stores the email address of the user 
| password      |   String      | stores the hashed password of the user 
| date_created  |   String      | stores the date the document was created 

**Profiles Collection**

| **Key**        |  **Type**     | **Purpose**|
|-------------- |-------------- |-------------|
| _id           |  ObjectId     | ObjectId of this document
| fullname      |   String      | stores the full name of the user 
| birthday      |   String      | stores the birthday of the user 
| location      |   String      | stores the location of the user 
| image         |   String      | stores the image of the user
| created_by    |   String      | stores the username who created the profile 
| date_created  |   String      | stores the date the document was created 

**Donation Collection**

| **Key**        |  **Type**     | **Purpose**|
|-------------- |-------------- |-------------|
| _id           |  ObjectId     | ObjectId of this document
| produce_category      |   String      | stores the produce category
| produce_name      |   String      | stores the produce name
| expiary_date      |   String      | stores the expiary date of produce
| quantity      |   String      | stores the quantity of produce
| image         |   String      | stores the image of the user
| created_by    |   String      | stores the username who created the profile 
| date_created  |   String      | stores the date the donation form was submitted 


**Order Seeds Collection**

| **Key**        |  **Type**     | **Purpose**|
|-------------- |-------------- |-------------|
| _id           |  ObjectId     | ObjectId of this document
| name      |   String      | stores the name of the user
| address      |   String      | stores the address of the user
| seed_name      |   String      | stores the name of the seed
| quantity      |   String      | stores the quantity of seeds
| date_ordered      |   String      | stores the date of the order


## 4. **Technologies Used**

### Languages
<ul>
<li><a href="https://en.wikipedia.org/wiki/HTML">HTML</a> - Programming language providing content and structure of the website.</li>
<li><a href="https://en.wikipedia.org/wiki/CSS">CSS</a> - Programming language providing styling of the website.</li>
<li><a href="https://en.wikipedia.org/wiki/Python_(programming_language)">Python</a> - Programming language used to drive core site functionality including user login and push/retrieving database information.</li>
<li><a href="https://en.wikipedia.org/wiki/Jinja_(template_engine)">Jinja</a> - Used to generate HTML from site templates</li>
</ul>

### Libraries
<ul>
<li><a href="https://fontawesome.com/">Font Awesome</a> - Library used for icons, such as social links and other images.</li>
<li><a href="https://fonts.google.com/">Google Fonts</a> - Font style library.</li>
<li><a href="https://flask.palletsprojects.com/en/1.1.x/">Flask</a> - Micro-framework to simplify Python scripting and web server tasks.</li>
<li><a href="https://werkzeug.palletsprojects.com/en/1.0.x/">Werkzeug</a> - Python library to manage user management integrity.</li>


### Editors
<ul>
<li><a href="https://github.com/">GitHub</a> - Remote code repository.</li>
<li><a href="https://gitpod.io/">GitPod</a> - IDE (Integrated Development Environment), for writing, editing and saving code.</li>
<li><a href="https://balsamiq.com/">Balsamiq</a> - Wireframes for visual design testing.</li>
</ul>

### Tools
<ul>
<li><a href="https://developer.chrome.com/docs/devtools/">Chrome DevTools</a> - Chrome DevTools is a set of web developer tools built directly into the Google Chrome browser.</li>
<li><a href="http://ami.responsivedesign.is/">Am I Responsive?</a> - Responsive design demo in ReadMe summary.</li>
<li><a href="https://www.responsivedesignchecker.com/">Responsive Design Checker</a> - Check website response across device types.</li>
</ul>

### Database Management
<li><a href="https://www.mongodb.com/">MongoDB</a> - Cloud based database management system, used for storing user profile and recipe information.</li>
</ul>


### Deployment Platform 
<ul>
<li><a href="https://www.heroku.com/">Heroku</a> - Remote hosting platform, for hosting of python driven websites and applications.</li>
</ul>

## 5. **Testing**

The testing process can be seen in the [TESTING.md](testing.md) document.

## 6. **Deployment**

### Database Deployment

### Application Hosting
### **Heroku**

The site is hosted using [Heroku](https://www.heroku.com/), deployed directly from the master branch of GitHub. The deployed site will update automatically as new commits are pushed to the master branch.

#### Creating a Heroku app
- From the Heroku dashboard:
  - Select "New"
  - Select "Create new app"

- Add new app details to form:
  - Add app name (must be unique)
  - Select region
  - Click "Create App"

#### Setting Environmental Variables
- From the Heroku dashboard:
  - Select your app from the list

- Select "Settings" from the top menu:
  - Under 'Config Vars', select "Reveal Config Vars"
  - Add environment variables in key-value pairs, click "Add" to add additional pairings.

#### Deployment
- Create required deployment files in the repository:
  - requirements.txt
      - Lists the required python modules for Heroku to install.
    - To create:
      - In your IDE terminal, type: ``pip freeze > requirements.txt``

  - Procfile
      -  Tell Heroku the command to launch the app.
    - To create:
      - in your IDE terminal, type: ``python app.py > Procfile``

  - .gitignore (optional)
      - Lists files and directories which should be deployed to live app, such as files with environmental passkeys.
    - To create:
      - In your IDE terminal, type: ``touch .gitignore``
      - List the files and directories to be excluded from live deployment, within the .gitignore file.
      - Save in your repository root directory.

- From the application top menu:
  - Select 'Deploy'
  - Choose your Deployment method:
    - Github:
      - Select the correct Github account.
      - Type in the repository name you wish to deploy.
      - Choose the correct repository from search results.
      - Select "Connect"

    - Manual Deployment:
      - Choose the correct branch you wish to deploy from the drop-down.
      - Select "Deploy Branch"
      - Heroku will return "Your App has successfully deployed". If this shows an error, troubleshooting will be needed.

#### Automatic Deployment
- From the application top menu:
  - Select 'Deploy'
  - Ensure app is connected to correct repository
  - Under 'Automatic Deployment' section:
    - Select 'Enable Automatic Deployment"

### GitHub and GitPod repository management

### **How to clone 'Crypto Connect’' in GitHub, GitPod and setup on Heroku.**

To run a version of the site locally, you can clone this repository using the following steps;

In a code editor of your choice;

1. Go to [GitHub.com](https://github.com/)
2. Click on 'Repositories'.
3. Click on 'SeedLink’.'
4. Click on the 'Code' button.
5. Under 'HTTPS' click the clipboard icon to the right of the URL.
6. In your IDE of choice, open a repository or create a new repository.
7. Open Terminal \('Terminal' then 'New Terminal' from the top ribbon menu in GitPod.\)
8. Type 'git clone', paste URL link and press enter.

Additional information around these cloning steps can be found on [GitHub Pages Help Page](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).
&nbsp;

#### Installing Requirements
- Install all requirements modules to your local IDE with the following CL:

```
 pip3 install -r requirements.txt
```

#### Create Collections in MongoDB

- Login to your MongoDB account
- Create a Cluster

- Create a database using the following architecture;

**Users Collection**

| **Key**        |  **Type**     | **Purpose**|
|-------------- |-------------- |-------------|
| _id           |  ObjectId     | ObjectId of this document
| firstname     |   String      | stores the first name of the user 
| lastname      |   String      | stores the last name of the user 
| username      |   String      | stores the username of the user 
| email         |   String      | stores the email address of the user 
| password      |   String      | stores the hashed password of the user 
| date_created  |   String      | stores the date the document was created 

**Profiles Collection**

| **Key**        |  **Type**     | **Purpose**|
|-------------- |-------------- |-------------|
| _id           |  ObjectId     | ObjectId of this document
| fullname      |   String      | stores the full name of the user 
| birthday      |   String      | stores the birthday of the user 
| location      |   String      | stores the location of the user 
| image         |   String      | stores the image of the user
| created_by    |   String      | stores the username who created the profile 
| date_created  |   String      | stores the date the document was created 

**Donation Collection**

| **Key**        |  **Type**     | **Purpose**|
|-------------- |-------------- |-------------|
| _id           |  ObjectId     | ObjectId of this document
| produce_category      |   String      | stores the produce category
| produce_name      |   String      | stores the produce name
| expiary_date      |   String      | stores the expiary date of produce
| quantity      |   String      | stores the quantity of produce
| image         |   String      | stores the image of the user
| created_by    |   String      | stores the username who created the profile 
| date_created  |   String      | stores the date the donation form was submitted 


**Order Seeds Collection**

| **Key**        |  **Type**     | **Purpose**|
|-------------- |-------------- |-------------|
| _id           |  ObjectId     | ObjectId of this document
| name      |   String      | stores the name of the user
| address      |   String      | stores the address of the user
| seed_name      |   String      | stores the name of the seed
| quantity      |   String      | stores the quantity of seeds
| date_ordered      |   String      | stores the date of the order


### Setup Unique Identifies / Environment Variables

- Create a '.gitignore' file in the root directoy
- Add 'env.py' and '__pycache__/' to the file list within .gitignore
- Create a 'env.py' file
- In the 'env.py' file write the following code;

```
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "[UNIQUE ID]")
os.environ.setdefault("MONGO_URI", "[UNIQUE ID]")
os.environ.setdefault("MONGO_DBNAME", "[UNIQUE ID]")

```

Note: For each sectionedn noted as [UNIQUE ID], you will need to provide your own unique identifier. These must also be aligned to Heroku environmental variables.


#### SECRET_KEY

This is required when using flash() and session() functions in flask. The key can be of your own choice, but it's advisable to use a randomly generated secure key from websites such as [RandomKeyGen.com](https://randomkeygen.com/).

#### MONGO_URI

This is used to connect you application to your MongoDB cluster.

- Click 'Overview' tab from your Cluster, followed by 'Connect'.

- Select 'Connect your application' from following window.

- Select your correct version of Python and copy the connection string.

- Replace the 'username' and 'password' text, with the relevant criteria you setup in 'Database Access'.

#### MONGO_DBNAME

This is the name of your database in MongoDB. Which can be found under the 'Collections' tab, under your cluster.

#### Running Development Server
This command is only available in Gitpod.

To launch a Http server using the development mode code for the application, use the following command in your IDE:

```

python3 app.py http.server

```

The IDE will then open a port with an http address for you to access.


## 7. **Credits**

### **Technical**
* [w3Schools](https://www.w3schools.com/) -For checking proper syntax of HTML and CSS elements and codes for Profile Tabs functionality.
* [Slack](https://slack.com/intl/en-gb/) -Code function for flash messages.
* [Autoprefixer](https://autoprefixer.github.io/) - For generating CSS browser prefixes.
* [Stackoverflow](https://stackoverflow.com/) - For researching and troubleshooting JavaScript and Python code issues.
* [MongoDB Documentation](https://docs.mongodb.com/) - For researching and troubleshooting database code commands and issues.

### **Content**
All text content on the site were written by all team members of Planters.

### **Media**
The photos and images used for this site were obtained from :


### **Acknowledgements**

* Special Thank you to Stefan for his encouragement and support on the development of this project.
* Thanks to our kids for letting us neglect them whilst we were busy coding!
* Thanks to those on the Slack community for answering our many questions 24:7!


