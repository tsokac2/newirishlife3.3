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

### [Python Unit Testing Framework](https://docs.python.org/3/library/unittest.html)
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

### [Jasmine](https://jasmine.github.io/)
Behaviour-driven development framework for testing JavaScript code.

#### Testing DOM Events Using jQuery and Jasmine 2.0
1. STEP: Create **testing** folder in project root folder - **../testing**

2. STEP: Create **cardsSpec.js** file in to **../testing/spec** folder

3. STEP: Create **cardstest.html** file in **testing** folder

4. STEP: In **cardstest.html** create basic **<!DOCTYPE html>** structure with **`<html>`**, **`<head>`** opening and closing tags

5. STEP: In the **`<head>`** element place **CDN** links in the following order - **CDN SOURCE:** https://cdnjs.com/libraries/jasmine :
  * `<script src="https://cdnjs.cloudflare.com/ajax/libs/jasmine/3.6.0/jasmine.js"></script>`
  * `<script src="https://cdnjs.cloudflare.com/ajax/libs/jasmine/3.6.0/jasmine-html.js" ></script>`
  * `<script src="https://cdnjs.cloudflare.com/ajax/libs/jasmine/3.6.0/boot.js"></script>`
  * `<script src="https://code.jquery.com/jquery-3.5.1.js"></script>`
  * `<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/jasmine/3.6.0/jasmine.css"/>` **SOURCE:** https://code.jquery.com/
  * `<script src="../testing/libraries/jasminejquery.js"></script>` external library **SOURCE:** https://bowercdn.net/c/jasmine-jquery-2.1.1/lib/jasmine-jquery.js  

6. STEP: Import custom scripts for Jasmine testing under imported **CDN's** in the following order:
  * `<script src="../testing/scripts/cards.js"></script>`
  * `<script src="../testing/spec/cardsSpec.js"></script>`





