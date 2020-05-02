# Command Line Interface with Python
## Notes on 'How to Build Command Line Interfaces in Python with argparse'
## By Davide Mastromatteo
### from Real Python
### https://realpython.com/command-line-interfaces-python-argparse/

-------------------------------------------------------------------

#### What is a Command Line Interface

	* Alias CLI
	* It's Pythons standard command line interface library
	* Replaced <getopt> and <optparse>
	* <argparse>
		- has positional arguments
		- customized prefix chars
		- multiple parameters per option
		- subcommands in some circumstances

	(brief run down of how to use terminal)

	* Argument - single part of a command line
	* Option - modifies the behavior of the command line
	* Parameter - provides additional information to a single option or command

#### When to Use a Command Line Interface
	
	* Command Line interface is user-friendly (computer scientist-friendly)
	* Allows user to specify how your program runs

#### How to Use the Python argparse Library to Create a Command Line Interface

	* Four steps
		- Import argparse
		- create parser
		- add options and position args
		- execute .parse_args()
	* .parse_args() returns a Namespace object that contains the argument received

	(example of a non-argparse command line program)

	* Using sys can function but it is lacking the standard flavor of the command line
	* The if statements make it clunky

	(example of argparse command line program)

	* A library checks for the argument now instead of if statements
	* argparse automatically enable -h for help info
	* The Namespace object will have a property for each argument you have defined.

## The Advanced Use of the Python argparse Library

#### Setting the Name of the Program

	* If you don't use argparse, sys.argv[0] will set the name of your program
	* with argparse <prog> will set the name of your program
		- <prog> is accepted as a parameter of .ArgumentParser
		- (prog='myProgram')
	* This change will show up when you use -h

#### Displaying a Custom Program Usage Help

	* Use <usage> in the same way you used <prog>
	* The string associated with it will show up with -h or with no command

#### Displaying Text Before and After the Arguments Help

	* <description> text shows before help text
	* <epilog> shows after

#### Customizing the Allowed Prefix Chars

	* You can change the (-) in -h or -m to (/) of any character (BUT WHY WOULD YOU WANT THAT?)
	* Use <prefix_chars>
	* Apparently this is helpful if you are coding for Windows 

#### Setting Prefix Chars for Files That Contain Arguments to be Included

	* If you have to many arguments, python will help you store them
	* fromfile_prefix_chars forces you to use a prefix
	* Now you can use the arguments from a txt file instead of typing them in manually

#### Allowing or Disallowing Abbreviations

	* <argparse> makes handling abbreviation easy
	* meaning --input, --inpu, --inp all do the same thing unless there is a collision with another argument
	* Upon a collision the an error message will specify what arguments collided
	* This feature can be removed with <allow_abbrev> set to false as a .ArgumentParser parameter 

#### Using Auto Help
