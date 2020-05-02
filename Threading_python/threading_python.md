# Threading Python 
## Notes on the article 'An Intro to Threading in Python'
## by Jim Anderson
### from Real Python 
### https://realpython.com/intro-to-python-threading/

-----------------------------------------------------------------------

##### This article is accompanied by a video tutorial and a quiz

-----------------------------------------------------------------------

#### What is a thread?

	* Threads make use of processors multiple cores
	* Python 3 threads don't run at the same time they just appear to
	* Threads still run one at a time
	* Tasks that wait for I/O activity are ideal for threading
	* Multiprocessing may be better if your program asks a lot of the CPU
	* Threading may have clarity benefits beyond just performance benefits

#### Starting a Thread

	* Import <threading>
	* <Thread> is a module in <threading>
	* <Thread> encapsulates threads 
	* A new thread can be created with a <Thread> instance and .start()
	* <Thread> takes a function to be threaded and an argument list as parameters
	* The argument list functions as a naming device?
	* <threading.git_ident()> will produce a unique name for each thread

	* A daemon is a process that runs in the background
		- In python daemons cease when it's program exits
		- Non-daemon threads will cause the program to wait for the thread to finish before exiting
		- Daemons are created as .Thread parameter <daemon=True>
	* .join() tells one thread to wait for another thread to finish
		- Thread.join() is now the priority and will finish before any other thread continues

#### Working with many Threads

	* The order in which threads are created has nothing to do with the order that they are run or the order that they will terminate.
	* The order of when threads are run may be different each time a program is executed

#### Using a ThreadPoolExecutor 

	* <ThreadPoolExecutor> can be found in concurrent.futures, its a better way to run many threads
	* It can be created as a context manager and a <with> statement
	* .map() can be used to pass each item in a list of tasks into its own thread
	* Using <ThreadPoolExecutor> as a context manager means .join() will be called for you
	* Bugs
		- if functions that don't take parameters are passed in to a thread through .map() with a parameter the exception will be hidden
		- the result will just be no out put instead of an error making the bug hard to locate

#### Race Conditions

	* Race conditions can occur when two or more threads access a shared piece of data
	* They are not always obvious and they can cause harmful problems
	* .submit() can be called on the threads of a <ThreadPoolExecutor>
		- .submit() has a signature tat allows both positional and named arguments to be passed to the function running in the thread
		- .submit(function, *args, **kwargs)

	* One Thread (the author notes that things are simplified in this section in a way that may not be accurate but helpful to understand. I personally looked over my Comp Org 2 notes about threading and it was very helpful)
		- A <ThreadPoolExecutor> is run with .submit()
		- .submit() takes a function and what parameter to pass that function as parameters
		- A thread run with .submit() will execute the first parameter with the second parameter as its argument
		- Each thread has its own version of data local to the passed function
		- Function variables are thread-safe

	* Two Threads
		- Two threads are run concurrently but not strictly at the same time
		- They will have their own copy of the function but will both point to the same object that function works on
		- This shared object is where problems will arise
		- These issues can manifest in many ways but they all stem from different threads taking similar actions with out the other threads knowledge

#### Basic Synchronization Using Lock
	
	* To avoid race conditions allow only one thread at a time to perform read-modify-write operations
	* This can be achieved with <Lock> or mutex in other languages
	* <Lock> can only be held by one thread at a time
	* Threads use .acquire() and .release() on <Lock>
	* If a thread does not give <Lock> up the program will freeze
	* <Lock> can be used as a context manager in a with statement, this will automatically drop the <Lock> if the with statement ends 
	* <Lock> is an object (though the article does not say this explicitly) that belongs to the object that could cause race conditions

#### Deadlock

	* Deadlocks occur when <Lock> is not released properly
	* THis can be avoided by using context managers
	* Deadlocks occur as a result of design issue
		- if a utility function needs to be called by functions that may or may not have the lock???? (item 2 in the list under Deadlock)
		- this can be avoided using <rLock>
		- <rLock>s can be .acquire()d many times
		- <rLock>s must be released the same number of times it is called
		??? (I did not find the article to be very clear on <rLock> or the condition requiring their use)

#### Producer-Consumer Threading

	* Producer-Consumer problem is a scenario used to teach threading or process synchronization issues
	* Scenario, massages come in over a network at odd intervals and must be written to a disk
		- The network is the Producer
		- The disk writer is the Consumer
		- The Consumer can keep up with the average pace of the produced messages but not the bursts of messages
		- In between these two is a Pipeline (programmers threading logic)

	* Producer-Consumer Using Lock
		- Producer and Consumer each have their own <Lock>
		- As one <lock> is released the other is acquired
		- This ensures that the producer can not send the consumer a message until the consumer has processed the previous message and released its <Lock>

	* Producer-Consumer Using Queue
		- A queue allows for more than one item in the pipeline at a time
		- threading.Event is a different primitive that can stop threads (similar to <Lock>)
		- <Event> can signal an occurrence in one thread to other threads
		- Other threads could wait for this event before executing a task
		- event.set() causes it
		- <Event>s can be checked with event.is_set()
		- Queue has <Lock>s built in so queues are thread safe

#### Threading Objects
	
	* Semaphore 
		- threading.Semaphore is a counter
		- its counting is atomic, meaning it can not be interrupted 
		- it counts +1 for .release() and -1 for .decremented()
		- The counter will always be zero of positive
		- If .acquire() is called and the count is 0. That thread will be paused until .release() is called by another thread
		- Semaphores are used to protect resources that have limited capacity

	* Timer
		- threading.Timer can call a function after a certain amount of time
		- <Timer>'s parameters are (the amount of time to wait in seconds, then the function)
		- To activate use .start()
		- .cancel() will cancel it 🤯

	* Barrier
		- threading.Barrier can keep a fixed number of threads in sync
		- it must be called with specific number of threads
		- if any thread calls .wait() on the <Barrier> then all of the threads will be blocked until all have also called .wait()
		- This allows threads to catch up to one another

	


