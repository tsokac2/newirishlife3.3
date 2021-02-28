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

      describe("Validate Email", function(){
        it("validateEmail() function should exist", function(){
            expect(validateEmail).toBeDefined();
        });

        it("validateEmail should return TRUE", function(){
            var testPass = validateName("email@gmail.com");
            expect(testPass).toBe(true); 
        });

        it("validateEmail should return FALSE", function(){
            var testFaild = validateName("");
            expect(testFaild).toBe(false); 
        });

      });

      describe("Push Error .form-group error CLASS for INVALID name or email input value", function(){
        it("pushErrorFor() function should exist", function(){
            expect(pushErrorFor).toBeDefined();
        });
      });

      describe("Push Error .form-group error CLASS for VALID name or email input value", function(){
        it("pushErrorFor() function should exist", function(){
            expect(pushSuccessFor).toBeDefined();
        });
      });

      describe("Send Function - for final validation proccess and form submitin action", function(){
        it("send() function should exist", function(){
            expect(send).toBeDefined();
        });
      });

      describe("Reset Function - send() function was success, reset function resets inouts fields", function(){
        it("reset() function should exist", function(){
            expect(reset).toBeDefined();
        });
      });
      
      describe("TnxForSupport Function - send() function request was success, success message will be display", function(){
        it("TnxForSupport() function should exist", function(){
            expect(TnxForSupport).toBeDefined();
        });
      });

      describe("sendEmail Function - connection betwen EMAILJS API provider", function(){
        it("sendEmail() function should exist", function(){
            expect(sendEmail).toBeDefined();
        });
      });

});
