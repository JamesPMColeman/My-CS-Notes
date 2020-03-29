import time
import logging
import concurrent.futures


class FakeDatabase:
	def __init__(self):
		self.value = 0

	def update(self, name):
		""" race_conditions.FakeDatabase.update()
		Simulates reading a value from FakeDatabase
		adds 1 to the value then writes the value back
		to FakeDatabase
		"""
		logging.info("Thread %s: starting update", name)
		local_copy = self.value
		local_copy += 1
		time.sleep(1)
		self.value = local_copy
		logging.info("Thread %s: finishing update", name)


if __name__ == "__main__":
	format = "%(asctime)s: %(message)s"
	logging.basicConfig(format=format, 
			    level=logging.INFO,
			    datefmt="%H:%M:%S")
	
	database = FakeDatabase()
	logging.info("Testing update. Starting value is %d." , database.value)
	
	# two threads are going run .update() at the same time
	with concurrent.futures.ThreadPoolExecutor(max_workers=2) as needle:
		for index in range(2):
			# .submit() allows both positional and named arguments 
			# to be passed the function running in the thread
			needle.submit(database.update, index)
	
	logging.info("Testing update Dending value is %d.", database.value)

