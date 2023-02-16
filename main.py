import pyautogui as pg 
from time import sleep
from rods import Rods

class Autofish:
	@classmethod
	def search(self):
		self.rod = Rods.select()
		self.count = input("Введіть скільки зарів ловити, після вводу у вас буде 5 секунд.\nКількість: ")		
		self.i = 0
		sleep(5)
		while self.i!=int(self.count):
			if pg.locateOnScreen(self.rod) is None:
				Autofish.catch()
	@classmethod
	def catch(self):
		print(str(self.i+1)+".", "catch")
		pg.mouseDown(button="left")
		pg.mouseUp(button="left")
		self.i+=1
		sleep(0.1)
		pg.mouseDown(button="left")
		pg.mouseUp(button="left")
		sleep(2)

if __name__ == '__main__':
	Autofish.search()