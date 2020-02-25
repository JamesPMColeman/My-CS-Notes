### Non-Functional  requirements Examples

#### Analysis
* Static 
	- Everything pre-run
	- PyLint Sonar Cloud radon, Checkstyle
	- Linters, Cyclomatic complexity method length
* Dynamic 
	- Analyzing a running program
	- Spotbugs, Valgrind Purify
	- Is it eating memory?
	- Is it slow?
		* profilers find the slow spots
		* we are bad at guessing what will be slow
		* Slowness happens from disk and networks
	- CPUs are fast, they are not slowing us down
		* if we scale .3 ns to a second (don't invest in cpu speed, DRAM is more valuable)
			> level 3 catch 43s
			> main memory 6 m in
			> SSD 2 - 6 days
			> network San Fran to UK 8 years
			> Physical system reboot 32 millennia
		* keep data close to cpu
		* don't miss on cache hits
		* mock databases for testing
#### Testing
* many types frameworks
	- Acceptance 
	_ Unit test: methods
		* most important
		* TDD!!!!
		* if you cant test you can't code
		* This will put you in the right frame of mind
	- Integration: class
	_ System - test the whole thing
* Implementation
	- SE tends to focus on requirements, design, and processes
###### Guideline 
	* Style
		- Follow language styles 
			> The Elements of Java Style - Scott Ambler and Trevor Misfeldt
			> (Get your self a style guide)
	* Naming
		- Use good descriptive names 
			> What they do not what type they are
	* Tests
	* Use Libraries
		- Write stuff that has already been written
		- comment where you find it
		- sight in read me
		- Are you allowed to take it?
			> is it public domain
	* Reviews
		- Always do retrospective
		- Others know things you don't 
		- Everything builds on everything else
	* Do not repeat yourself
	* Others

### Agile
	* Many different things
	* Old way doesn't work (waterfall)
	* Agile focuses on short release cycles
	* Allow changes in design
	* Focus on human and team aspects
	* Incremental design
	* User involvement 
	* Lightweight documentation
	* Informal communication
	* change
		- Users change their minds and thats a good thing
##### Why agile
	* lengthy development times can feel shorter
	* better product
	* more predictable product
	* All requirements are not known at the beginning
	* it cuts down the 'heroic effort'
	* insists on 40 hour works
	* Processes too complex
		- RUP: 100 Tasks and 30 roles
	* Too much waste and duplication 
	* Now: Source code is the truth 
		- Code and test are your design
##### Agile Promises
	* Finished product always available 
	* Normal effort by team
	* deal with change 
###### What really matters
	* Interpersonal stuff
###### What to do 
	* Process is not the answer to good software
	* process can cause more problems than it solves
#### Agile Manifesto
	* We are uncover better ways of development software by doing it and helping others do it. thorough this work we have come to value
	
###### Individuals and interactions over processes and tools 
	* Good process wont fix bad team members
	* bad process will hinder good team members	
	* Everyone must work together to succeed
	* Strong team members not necessarily strongest programmer, designer, etc.
		- communication and inter action
	* Start small with tools !!!!!!!
	* Don't create the environment first
		- some IDEs are better for different situations
	* Create the  and then let them create the environment
###### Working software over comprehensive documentation
	* cant have doc with out program
	* Need to describe system and document design decisions
	* Large amounts of documentation can become cumbersome and of sync
	* Knowledge transferred in the team bu direct interaction
	* Produce no document unless its need is immediate and significant!
###### Customer collaboration over contact negotiation
	* Successful projects get customer feedback early and often 
	* Best contracts specify how team and customers interact
###### Responding to change over following a plan
	* Things changes
	* Team and customer gains knowledge about solution 
	*  detailed plans for next two weeks, rough plans for three months crude after that

