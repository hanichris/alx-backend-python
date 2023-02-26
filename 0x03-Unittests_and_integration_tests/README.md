# Unittests and Integration Tests
## Description
Unit testing is the process of testing that a particular function returns the expected results for different sets of inputs. A unit test tests standard inputs and corner cases. It only test the logic within the tested function. Any calls to additional functions should be mocked, especially for the case of network or database calls.
<br>
Integration tests aim to test a code path end-to-end. Only low-level functions that make external calls such as HTTP requests, file I/O, database I/O etc. are mocked. These tests test interaction between every part of your code.