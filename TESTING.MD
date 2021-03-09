## Table of Contents
* [JASMINE](#UX)



# CLOUDE BASE VALIDATORS

### [W3C HTML Validator](https://validator.w3.org/#validate_by_uri)
* HTML [Home]() Result
* HTML [Trip]() Result
* HTML [Work]() Result
* HTML [Life]() Result
* HTML [Tips]() Result
* HTML [Registration]() Result
* HTML [Login]() Result
* HTML [Add_Tip]() Result

### [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
* CSS [index.css] Result

### [JSHint Validator](https://jshint.com/)
* JS file [emailnews.js] Result
* JS file [maps.js] Result
* JS file [cards.js] Result

### [PEP8 Validator](http://pep8online.com/)
* Python file [app.py] Result
* Python file [forms.py] Result
* Python file [test.py] Result




# TEST CASES DESCRIPTION AND RESULTS

Full test results can be found in an excel document **[HERE]()**

![Test Results](testing/test_results_1.JPG)
![Test Results](testing/test_results_2.JPG)
![Test Results](testing/test_results_3.JPG)
![Test Results](testing/test_results_4.JPG)
![Test Results](testing/test_results_5.JPG)
![Test Results](testing/test_results_6.JPG)
![Test Results](testing/test_results_7.JPG)
![Test Results](testing/test_results_8.JPG)
![Test Results](testing/test_results_9.JPG)
![Test Results](testing/test_results_10.JPG)
![Test Results](testing/test_results_11.JPG)
![Test Results](testing/test_results_12.JPG)
![Test Results](testing/test_results_13.JPG)


# LOCAL BASE VALIDATORS

### [Unit Testing](https://docs.python.org/3/library/unittest.html)
* Testing was processed to ensure that routing functionality is redirecting users to the requested page route.
* Command line [test.py] Result


### JASMINE - https://jasmine.github.io/

Jasmine is a behavior-driven development framework for testing JavaScript code

## Testing DOM Events Using jQuery and Jasmine 2.0

### IMPLEMENTATION
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

### Testing that **DOM** Event was triggered

#### Testing code source **`<script src="testing/scripts/cards.js"></script>`**

* Card element in trip.html on line 260 with following structure
```
  <div id="Card1" class="wrap">

    Card content...

    <div class="showLinks1-grid hideLinks1-grid text-center">

      Quick links content...

    </div>
  </div>
```

* jQuery DOM Events for `#showLinks1`

```
describe("Testing DOM Elements - Triggering .on('click') Event in trip.html, work.html and life.html", function(){

    it("Should invoke the jQuery click event when elements #showLinks1 and #hideLinks1 are clicked", function(){
        setFixtures('<button id="showLinks1" class="load-links-btn">Quick Links...<i class="fas fa-sort-down"></i></button>');
        $('#showLinks1').on('click', function (){
            var thisCardLinkShow = "." + this.id + "-grid";
                $(thisCardLinkShow).show(300);
                $(".blur").fadeIn(400);
                $(thisCardLinkShow).addClass("rel-card");
                $("#Card1").addClass("wrap-rel");
        });

        var spyEventShow = spyOnEvent('#showLinks1', 'click');
        $('#showLinks1').trigger('click');
        expect(spyEventShow).toHaveBeenTriggered();
    });
});

```

#### Test STEPS

* `setFixtures('<button id="showLinks1"</button>');`        - mimicking `<button>` element on line 265 in trip.html
* `$('#showLinks1').on('click', function (){...}`           - referencing jQuery DOM events applied to `<button>` element
* `var spyEventShow = spyOnEvent('#showLinks1', 'click');`  - creating variable var `var spyEventShow;`for invoking `spyOnEvent` on to `<button>` element
* `$('#showLinks1').trigger('click');`                      - triggering DOM event
* `expect(spyEventShow).toHaveBeenTriggered();`             - including `spyEventShow` variable in to `.toHaveBeenTriggered()` test instance

Test was replicated for all 12 `<button>` elements with unique ID's attributes starting from `id="showLinks1"`and `id="hideLinks1"` element `<button>`

**FULL SOURCE CODE:** JASMINE TESTING SCRIPT [cardsSpec.js](https://github.com/tsokac2/newIrishLife.2.0/blob/main/testing/spec/cardsSpec.js)

**Live Version of the Jasmine Test** - [Jasmine Test](https://tsokac2.github.io/newIrishLife.2.0/testing/cardstest.html)

## Testing Validation Functions for EMAILJS API Newsletter services

### IMPLEMENTATION
1. STEP: Create **testing** folder in project root folder - **../testing**

2. STEP: Create **emailnewsSpec.js** file in to **../testing/spec** folder

3. STEP: Create **emailnewstest.html** file in **testing** folder

4. STEP: In **emailnewstest.html** create basic **<!DOCTYPE html>** structure with **`<html>`**, **`<head>`** opening and closing tags

5. STEP: In the **`<head>`** element place **CDN** links in the following order - **CDN SOURCE:** https://cdnjs.com/libraries/jasmine :
  * `<script src="https://cdnjs.cloudflare.com/ajax/libs/jasmine/3.6.0/jasmine.js"></script>`
  * `<script src="https://cdnjs.cloudflare.com/ajax/libs/jasmine/3.6.0/jasmine-html.js" ></script>`
  * `<script src="https://cdnjs.cloudflare.com/ajax/libs/jasmine/3.6.0/boot.js"></script>`
  * `<script src="https://code.jquery.com/jquery-3.5.1.js"></script>`
  * `<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/jasmine/3.6.0/jasmine.css"/>` **SOURCE:** https://code.jquery.com/

6. STEP: Import custom scripts for Jasmine testing under imported **CDN's** in the following order:
  * `<script src="../testing/scripts/emailnews.js"></script>`
  * `<script src="../testing/spec/emailnewsSpec.js"></script>`

### Testing `return` values of call-back validation functions

#### Testing code source **`<script src="testing/scripts/emailnews.js"></script>`**

```
describe("Testing Callback functions for Validation process against Input Elements Values", function(){

      describe("Validate Name", function(){
        it("validateName() function should exist", function(){
            expect(validateName).toBeDefined();
        });

        it("validateName should return TRUE", function(){
            var testPass = validateName("Tom");
            expect(testPass).toBe(true);
        });

        it("validateName should return FALSE", function(){
            var testFaild = validateName("T");
            expect(testFaild).toBe(false);
        });

      });
  });
```

#### Test STEPS
* Testing if `validateName()` function exist

  ```
  describe("Validate Name", function(){
    it("validateName() function should exist", function(){
        expect(validateName).toBeDefined();
    });
  ```
* Testing if `validateName()` function return **TRUE** if input `value.length` is > that 2

  ```
  it("validateName should return TRUE", function(){
      var testPass = validateName("Tom");
      expect(testPass).toBe(true);
  });
  ```

* Testing if `validateName()` function return **FALSE** if input `value.length` is < that 2

  ```
  it("validateName should return FALSE", function(){
      var testFaild = validateName("T");
      expect(testFaild).toBe(false);
  });
  ```

**FULL SOURCE CODE:** JASMINE TESTING SCRIPT [emailnewsSpec.js](https://github.com/tsokac2/newIrishLife.2.0/blob/main/testing/spec/emailnewsSpec.js)

**Live Version of the Jasmine Test** - [Jasmine Test](https://tsokac2.github.io/newIrishLife.2.0/testing/emailnewstest.html)

****

##  ISSUES AND RESOLUTIONS

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


## FireFox and Chrome Developer Tools Console

**ISSUE #1**
Error:  CSS background property - bad path property `background-image: url("../img/rent_fav.png");`

SOLUTION: `background-image: url("../img/rent_fav.png");` - no quotes

SOLUTION SOURCE: [Stackoverflow](https://stackoverflow.com/questions/21374534/css-background-image-not-loading)

**ISSUE #2**
Error:  jQuery .show() and .hide() - not applicable on DOM elements

SOLUTION: Implement jQuery Core 3.5.1 - uncompressed version - [jQuery](https://code.jquery.com/)

**ISSUE #3**
Error: Uncaught TypeError: Cannot read property 'querySelector' of null - selector does not return any elements at the stage when the script is executed

SOLUTION: Confirm that all DOM has a unique ID selector - if element in header section has same ID like element in footer section `document.getElementById("footer-element-id")` will have value of null

**ISSUE #4**
Error:
> Google Maps API - "We have detected a publicly accessible Google API key associated with the following Google Cloud Platform project"
SOLUTION:
1. If this key is intended to be public (or if a publicly accessible key isn’t preventable):
	- Log in to the Google Cloud Console and review the API and billing activity on your account, ensuring the usage is in line with what you expected.
	- Add API key restrictions to your API key, if applicable.
2. If this key was NOT meant to be public:
	- Regenerate the compromised API key: Search for Credentials in the cloud console platform, Edit the leaked key, and use the Regenerate Key button to rotate the key. For more details, review the instructions     on handling compromised GCP credentials.
	- Take immediate steps to ensure that your API key(s) are not embedded in public source code systems, stored in download directories, or unintentionally shared in other ways.
	- Add API key restrictions to your API key, if applicable.
The security of your Google Cloud Platform account(s) is important to us.