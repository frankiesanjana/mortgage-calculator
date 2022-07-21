# Mortgage Calculator

Mortgage Calculator is a program designed for users who are interested in taking out a mortgage. Users can enter the parameters of a potential mortgage and see what their monthly payment would be, as well as the total amount repaid over the lifetime of the mortgage. Users can choose to save these details and return to view them at a later date.
The program can equally be used to look at options for refinancing an existing mortgage, and also contains some examples of preset mortgages.

The program is written using Python, runs in a Command Line Interface and is deployed via Heroku. You can visit the live website [here](https://p3-mortgage-calculator.herokuapp.com/).

The program has been created for the third portfolio project for Code Institute's Diploma in Full Stack Software Development.

<img src="assets/images/amiresponsive.png" alt="Four screens showing the website's appearance on different sized screens">

## Concept

The program has been developed to provide a solution for the following user stories and owner goals. User stories are focused around specific needs that users of a mortgage calculator are likely to have. Owner goals take into account why a potential owner could be interested in developing such a program.

### User Stories

- As a new visitor, I want to understand quickly what the program is for.
- As a new or returning visitor who is interested in taking out a mortgage, I want to input my details and learn what my monthly repayment will be.
- As a new or returning visitor who is interested in taking out a mortgage, I want to input my details and learn what the total repaid over the lifetime of the mortgage will be. I am then able to choose a higher monthly repayment if I can afford to do so, in order to minimise the total amount that I will have to pay.
- As a new or returning visitor, I want the program to be simple to use and easy to understand.
- As a new or returning visitor, I want the program to work, even if I make a mistake in entering information.
- As a new or returning visitor, I want it to be easy to exit the app when I am done using it.
- As a new visitor, I want to create a username that is unique to me and that I can use to store my details for future use. When I return, I want my username to be quickly found so that I am recognised.
- As a returning visitor, I want to quickly and simply retrieve my details.
- As a new or returning visitor, I want to be able to save my details and for these details to be stored securely.
- As a user who is considering several mortgage options or considering refinancing an existing mortgage, I would like to view some examples that are similar but have some differences, so that I can better understand the implications of these differences on the monthly payment and lifetime repayments of a potential mortgage. (For example, extending the term of a mortgage will decrease the monthly payment but increase the total lifetime repayment.)

### Owner Goals

- As the owner, I want to provide a program that fulfils the users’ needs.
- As the owner, I want to make it immediately obvious what the program is for.
- As the owner, I want to provide clear and accurate information.
- As the owner, I want to create an experience that is pleasant for users.
- As the owner, I want the program to continue without crashing due to an error caused by user input.

## Design

The program has been designed based on the five planes of content strategy. Although it is a terminal application and therefore differs somewhat from web design, each plane still applies in some way.

### Plane 1: Strategy

The strategy of the program is largely defined by the user and owner goals listed above in the Concept section. The strategy is simply to provide solutions to the goals of the program’s users and owners.

### Plane 2: Scope

The program includes the following features:
- Introductory page
- Separate welcome screens for new and returning users
- Choice to view example mortgages
- Choice to enter details of a mortgage
- Choice to retrieve saved details of a mortgage
- Exit

One feature that I would have liked to include is the ability for users to use the program to send themselves an email containing the details they have entered and the resulting mortgage(s). This is not straightforward within the technologies used in this project, but could be incorporated into a future project.

### Plane 3: Structure

The structure of the program can be seen in the flowchart below, which was created using PowerPoint:

<img src="assets/images/logic.png" alt="Diagram showing the logic flow of the program">

### Plane 4: Skeleton

The user will experience the program as a series of multiple-choice menus. They will interact with the program by selecting their choice and pressing Enter.

Due to the nature of this project, the wireframes are extremely simple:

<img src="assets/images/wireframe.png" alt="Wireframe of the project as it appears in a browser window">

### Plane 5: Surface

The aims at the surface level are to make the program straightforward and enjoyable to read and use. The following points were designed with this in mind:

#### Colours

Colours for text have been imported from the Python library [colorama](https://pypi.org/project/colorama/) and each colour used consistently for certain functions. For example, green is used to greet the user or at the start of a menu; yellow is used for error messages (red was considered but decided to be too harsh). 

#### Media

The only media that has been incorporated into the project is ASCII art of a house, which appears on the introductory screen. This adds some interest but also helps to make immediately clear to the user what the program is for.

#### Presentation

The program generally aims for consistency. For example, menu options for the user are kept in as similar an option as possible, and where it makes sense to do so the same key is used for the same option throughout the program. For example, if the user wants to exit the program they will always select ‘z’ to do this, whichever menu they are choosing this option from.
There are also several extra line breaks inserted into the code, with the aim of breaking up the text printed to the terminal to make it more readable.

## Features

### UX and User Stories

"As a new visitor, I want to understand quickly what the program is for."  
"As a new or returning visitor, I want the program to be simple to use and easy to understand."

- The introductory page welcomes users to the mortgage calculator and briefly states its functionality. The ASCII art of a house provides an at-a-glance impression of the topic of the program.

<img src="assets/images/features-intro.png" alt="View of terminal on starting screen of the application">

"As a new or returning visitor who is interested in taking out a mortgage, I want to input my details and learn what my monthly repayment will be."  
"As a new or returning visitor who is interested in taking out a mortgage, I want to input my details and learn what the total repaid over the lifetime of the mortgage will be. I am then able to choose a higher monthly repayment if I can afford to do so, in order to minimise the total amount that I will have to pay."  
"As a new or returning visitor, I want to be able to save my details and for these details to be stored securely."

- The user is given an explanation and example showing how to input their details for the calculator to work.

<img src="assets/images/features-input-details.png" alt="View of terminal on screen requesting user details">

- When the details have been entered, the monthly payment and total repayment are calculated and displayed to the user.  
- The user is then offered the option of saving these details, which is done using a Google spreadsheet that is linked to the program via an API.

<img src="assets/images/features-input-result.png" alt="View of terminal on screen showing results details and offering save option">

"As a new visitor, I want to create a username that is unique to me and that I can use to store my details for future use. When I return, I want my username to be quickly found so that I am recognised."

- New visitors are asked to create a username and given the requirements for the username. This is checked against the database and rejected if it already exists.

<img src="assets/images/features-new-username.png" alt="View of terminal on screen showing new username creation and check against database">

"As a returning visitor, I want to quickly and simply retrieve my details."

- Returning visitors are taken to the main menu, from where they can select the option to view their saved details.

<img src="assets/images/features-view-saved.png" alt="View of terminal on screen showing retrieval of stored details">

"As a new or returning visitor, I want the program to work, even if I make a mistake in entering information."

- If a user enters an invalid input, they are informed of this and instructed to try again. The options are then repeated to them.

<img src="assets/images/features-invalid.png" alt="View of terminal on screen showing a user input error and the error message displayed">

"As a user who is considering several mortgage options or considering refinancing an existing mortgage, I would like to view some examples that are similar but have some differences, so that I can better understand the implications of these differences on the monthly payment and lifetime repayments of a potential mortgage. (For example, extending the term of a mortgage will decrease the monthly payment but increase the total lifetime repayment.)"

- The example mortgages saved in the calculator provide some examples of similar mortgages with small differences, which illustrate the impact that seemingly small changes can have on monthly and total repayments.
- Examples can be viewed singly or all together in a table.

<img src="assets/images/features-single-example.png" alt="View of terminal on screen showing a single example mortgage description">

<img src="assets/images/features-all-examples.png" alt="View of terminal on screen showing all example mortgages displayed in a table">

"As a new or returning visitor, I want it to be easy to exit the app when I am done using it."

- Menu screens have the option of exiting the program at multiple points; the user does not need to return to the main menu in order to exit, but can also exit from the main menu.
- When exiting, the user is thanked for using the program.

<img src="assets/images/features-goodbye.png" alt="View of terminal on screen showing user choice to exit and goodbye message">

## Data Model

### Object Oriented Programming

The program uses Object Oriented Programming in the main functionality of the calculator. The mortgage calculations are done by creating a class called MortgageCalculator. This takes the variables of interest rate, term and value of the mortgage, and uses the NumPy Financial function `pmt` to calculate the monthly repayment on that mortgage. From this, since we know the total duration of the mortgage, it is simple to calculate the total repayment over the lifetime of the mortgage.

The example mortgages used in the program are instances of this class, as are any mortgages entered by users.

### Google Sheet

A Google Sheet is used to store details entered by users and the mortgage information that is calculated by the MortgageCalculator class using these details. The sheet uses a single worksheet "database" to store these details:

<img src="assets/images/google-sheet.png" alt="View of Google Sheet storing user details">

## Technologies Used

### Python Libraries

- [colorama](https://pypi.org/project/colorama/) is used to print text to the terminal in different colours and styles.
- [gspread](https://pypi.org/project/gspread/) is used to communicate with Google Sheets.
- [google.oauth2.service_account](https://google-auth.readthedocs.io/en/stable/index.html) Credentials is imported from this library to validate credentials and grant access to Google service accounts.
- [numpy financial](https://pypi.org/project/numpy-financial/) is used to perform the calculations for the monthly mortgage payment via the `pmt`function.
- [pandas](https://pypi.org/project/pandas/) is used to display data in tables to make it clear for the user to read. This is done when retrieving stored user details from the database, as well as when displaying all the example mortgages together.

### Other Technologies

- [MS Excel](https://www.microsoft.com/en-ww/microsoft-365/excel): since I have vastly more experience with MS Excel than with Python, I built out the mortgage calculations in Excel quickly before starting to code. This helped to enable that the logic flow was clear in my mind before starting, and provided a cross-check for the financial calculations:

<img src="assets/images/calculator-excel.png" alt="View of mortgage calculation in MS Excel">

- [MS PowerPoint](https://www.microsoft.com/en-us/microsoft-365/powerpoint) was used to draw out the logic flow of the program.

- [Balsamiq](https://balsamiq.com/) was used to create wireframes for the project.

- [Amiresponsive](http://ami.responsivedesign.is/) was used to create the image at the top of this document.

- [Gitpod](https://www.gitpod.io/) is an online integrated development environment that was used to write my code.

- [Git](https://git-scm.com/) was used for version control by committing changes via Gitpod. Changes are then stored by pushing them to GitHub.

- [GitHub](https://github.com/) was used to store the project code after pushing it from Git.

- [Heroku](https://www.heroku.com/) is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud, and was used to deploy the live project.

- [Google Sheets](https://www.google.com/sheets/about/) was used to securely store user data entered in the project.

- [PEP8 online](http://pep8online.com/) was used to validate Python code.

## Testing

### Manual Testing
- note on how code was written with testing as I went along
- spreadsheet with all logic tests

### PEP8 Testing

### Lighthouse Testing

## Bugs

### Current Bugs

### Resolved Bugs

## Development

### GitHub

### GitPod

### Google Sheets
- incl sheet creation process and API Credentials

## Deployment

### Heroku

## Credits

### General Python skills

### Specific to the project 
- how to do the mortgage calculation in Excel

### Acknowledgements