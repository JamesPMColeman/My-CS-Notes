# Mocking Python
## Notes on the article 'Mocking External APIs in Python'

### from Real Python
### https://realpython.com/testing-third-party-apis-with-mocks/

-----------------------------------------------------------------------------

#### Mocking

	* The logic behind external libraries is uncontrollable
	* To ensure that your program interacts with third-party APIs in a predictable manner their functionality must be tested
	* Testing live data from a third party is unfeasible, unstable and slow
	* Mocks fake the functionality of external code
	* Mocks are objects that look and act like real data and can be substituted for a third party object
	* Use mocks when your app:
		- needs to communicate with an external server
		- involves user data
		- relies on the success of an external technology to use its APIs
		- uses authentication 

#### First steps
	(coding instructions omitted)

	* When testing the acquisition of out side data the first test should verify an <OK> response not the data its self

#### Refactoring your code into a service

	* Calls to external APIs are common
	* All logic associated with those calls should be encapsulated
	* This allows us to see every aspect of the logic worth testing
	* Consider putting your global constants in their own file

#### Your first mock

	* Mock exactly the function that communicates with an external source
	* Mocks must be instructed to behave the way the replaced function would act. If there are multiple ways that function could act then multiple tests may need to be run
	* an @patch() decorator located a line above the a test, instructs a mock object in the test what it should be mocking

#### Other ways to patch

	* A context manager can also set up a mock object using with patch('method.location') as mock_method
	* There is also a patcher that is initiated explicitly and needs to be .start()ed and .stop()ed

	* Patch with a decorator when all of the code in your test function uses a mock
	* Patch with a context manager when only some of the code in your test function uses a mock and other code references the actual function
	* Patch with a patcher if you need to explicitly start and stop mocking, setUp() and tearDown()s for instance

#### Mocking the complete service behavior

	* The @patch() provides a path to the function you want to mock
	* When using a @patch() you have to pass the mock_function name into the test as a parameter
	* If the function being mocked calls an external library and the test checks for the response object so the mock must be told to return the same type of object
	* If a mock method is set to return an object, that object is also a mock object
	* If the your are testing for a property on that returned object then your mock object needs to have a parallel mock property
	* Fundamental functions can be called on the mock objects when applicable

#### Mocking integrated function

	* If you are testing a function that calls a function that calls a third-party then, instead of mocking the function closest to the third-party you can mock the function that houses it. 
	* It is important to consider all possible results of a function when your testing

#### Refactoring tests to use classes

	* When multiple tests test the same function they should be grouped into a class
		- This makes it easier to test them as a group
		- Similar tests may have similar data that needs to be created and destroyed
		- If tests reuse logic it can be abstracted into a helper function
	* an @classmethod over <setup> and <teardown> functions easily allow mocks to be reused

#### Testing for updates to the API data

	* It is crucial that the data you mock is the same type as the third party you are replacing
	* Though third party data doesn't change frequently it could change at some point
	* Eventually all code deprecates
	* When comparing external data to expected type, compare the data structure rather than the actual data

#### Conditionally testing scenarios

	* A test of third party content should not be treated the same as other unit tests
	* A failure of these tests does not necessarily mean your code is broken
	* Tests can be skipped with an @skipIf() decorator
	* @skipIf() takes a condition and a response as parameters



