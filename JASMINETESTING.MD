## JASMINE - https://jasmine.github.io/

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
