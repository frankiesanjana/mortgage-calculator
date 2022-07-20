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
- As a new visitor, I want to create a username that is unique to me and that I can use to store my details for future use.
- As a returning visitor, I want to quickly and simply retrieve my details.
- As a new or returning visitor, I want any details that I store to be stored securely.
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

### Plane 5: Surface

The aims at the surface level are to make the program straightforward and enjoyable to read and use. The following points were designed with this in mind:

#### Colours

Colours for text have been imported from the Python library [Colorama](https://pypi.org/project/colorama/) and each colour used consistently for certain functions. For example, green is used to greet the user or at the start of a menu; yellow is used for error messages (red was considered but decided to be too harsh). 

#### Media

The only media that has been incorporated into the project is ASCII art of a house, which appears on the introductory screen. This adds some interest but also helps to make immediately clear to the user what the program is for.

#### Presentation

The program generally aims for consistency. For example, menu options for the user are kept in as similar an option as possible, and where it makes sense to do so the same key is used for the same option throughout the program. For example, if the user wants to exit the program they will always select ‘z’ to do this, whichever menu they are choosing this option from.
There are also several extra line breaks inserted into the code, with the aim of breaking up the text printed to the terminal to make it more readable.

## Features

### UX Features

## Data Model

class / OOP

Google Sheet

Notes on the code

## Technologies Used
- explain why each library is used, what it does
- incl excel and ppt for test model and logic flow diagram

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