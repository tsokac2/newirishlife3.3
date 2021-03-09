## Table of Contents
* [Cloud-Based-Validators](#Cloud Based Validators)
* [Test-Cases-Description-and-Results](#Test Cases Description and Results)
* [Local-Base-Validators](#Local Base Validators)

## Cloud Based Validators

### [W3C HTML Validator](https://validator.w3.org/#validate_by_uri)

* HTML [Home Result]() - No errors
* HTML [Trip Result]() - No errors
* HTML [Work Result]() - No errors
* HTML [Life Result]() - No errors
* HTML [Tips Result]() -  No errors
* HTML [Registration Result]() - No errors
* HTML [Login Result]() - No errors
* HTML [Add_Tip Result]() - No errors

### [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
* CSS [index.css Result]() - No errors

### [JSHint Validator](https://jshint.com/)
* JS file [emailnews.js Result]() - No errors
* JS file [maps.js Result]() - No errors
* JS file [cards.js Result]() - No errors

### [PEP8 Validator](http://pep8online.com/)
* Python file [app.py Result]() - No errors
* Python file [forms.py Result]() - No errors
* Python file [test.py Result]() - No errors

****

## Test Cases Description and Results

Full test results can be found in an excel document **[HERE]()**

![Test Results](https://github.com/tsokac2/newirishlife3.3/blob/main/static/wireframes/TC001.png)
![Test Results](https://github.com/tsokac2/newirishlife3.3/blob/main/static/wireframes/TC004.png)
![Test Results](https://github.com/tsokac2/newirishlife3.3/blob/main/static/wireframes/TC006.png)
![Test Results](https://github.com/tsokac2/newirishlife3.3/blob/main/static/wireframes/TC007.png)
![Test Results](https://github.com/tsokac2/newirishlife3.3/blob/main/static/wireframes/TC008.png)
![Test Results](https://github.com/tsokac2/newirishlife3.3/blob/main/static/wireframes/TC009.png)
![Test Results](https://github.com/tsokac2/newirishlife3.3/blob/main/static/wireframes/TC012.png)
![Test Results](https://github.com/tsokac2/newirishlife3.3/blob/main/static/wireframes/TC016.png)
![Test Results](https://github.com/tsokac2/newirishlife3.3/blob/main/static/wireframes/TC020.png)
![Test Results](https://github.com/tsokac2/newirishlife3.3/blob/main/static/wireframes/TC025.png)
![Test Results](https://github.com/tsokac2/newirishlife3.3/blob/main/static/wireframes/TC027.png)

****

## Local Base Validators

### [Unit Testing](https://docs.python.org/3/library/unittest.html)
Testing was processed to ensure that routing functionality is redirecting users to the requested page route.

#### Testing covered:
* Test **Home** page load response
* Test **Trip** page load response
* Test **Work** page load response
* Test **Life** page load response
* Test **Tips** page load response
* Test **Sign Up** page load response
* Test **Login** page load response
* Command line 8 [Tests Result]() 


### W3 Validator Error's and Solutions VALIDATOR ERROR's and SOLUTIONS

**ISSUE #1**
 _Error_: Duplicate ID username - `<input type="text" id="username" placeholder="Username or Email">`

 _SOLUTION_: Create unique  ID - `id="username"` for Sign Up form  - `id="username-log"` for Login form

**ISSUE #2**
_Error_: Bad value `public\img\Logo.png` for attribute src on element img: Backslash ("\") used as path segment delimiter.

`<img src="assets\img\Logo.png" width="100" alt="New Irish Logo"></a>`

_SOLUTION_: `<img src="assets/img/Logo.png" width="100" alt="New Irish Logo"></a>` - change "\" to "/"

**ISSUE #3**
_Error_: The `aria-labelledby` attribute must point to an element in the same document.

`<div class="modal fade" id="sing-in" data-backdrop="static" data-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">`

_SOLUTION_: ` <div class="modal fade" id="sing-in" data-backdrop="static" data-keyboard="false" tabindex="-1" aria-labelledby="sing-in" aria-hidden="true">`

_SOLUTION SOURCE_ -  [Stackoverflow](https://stackoverflow.com/questions/39831658/how-to-fix-the-aria-labelledby-attribute-must-point-to-an-element-in-the-same-d)

**ISSUE #4**
_Error_: Duplicate attribute class.

_SOLUTION_: Remove class duplicates in `<a href="https://www.jetcost.ie/" target="_blank" class="q-links a">FLIGHTS</a>`

**ISSUE #5**
_Error_: The type attribute is unnecessary for JavaScript resources

_SOLUTION_: Remove type attribute from`<script  src="assets/js/emailnews.js"></script>`

**ISSUE #6**
_Error_: No space between attributes

_SOLUTION_: Add space between `<script>` and `src=""` attribute in `<script  src="assets/js/emailnews.js"></script>`

**ISSUE #7**
_Error_: Start tag seen without seeing a doctype first. Expected `<!DOCTYPE html>`

_SOLUTION_: Add doctype before opening `<html>` DOM element

**ISSUE #8**
_Error_: `.section-home .quote p` 	Value Error : font-size only 0 can be a unit. You must put a unit after your number : 1.5

_SOLUTION_: Add unit type after font-size property value `font-size: 1.5rem;`

**ISSUE #9**
_Error_: `.section-home .intro-pitch .pitch-wrap .composition` Value Error : margin-top  2rem is not a margin-top value :  2rem

_SOLUTION_: Remove extra space in `margin-top:  2rem;` to `margin-top: 2rem;`
