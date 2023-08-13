class Rods():	
	@classmethod
	def select(self):
		path = "rods/"
		select = int(input("Виберіть вудку:\n1. Дерев'яна\n2. Посилена\n3. Ловець душ\n4. Ловець плоті\n5. Приманювач приманки\n6. Склопластикова\n7. Скарабея\n8. Механіка\n9. Легкої здобичі\n10. Вогняна\n11. Золота\n--> "))
		if select == 1:
			rod = "wooden.png"
		elif select == 2:
			rod = "iron.png"
		elif select == 3:
			rod = "soul_catcher.png"
		elif select == 4:
			rod = "meat_catcher.png"
		elif select == 5:
			rod = "bait_baiter.png"
		elif select == 6:
			rod = "glassplastic.png"
		elif select == 7:
			rod = "skarab.png"
		elif select == 8:
			rod = "mecatic.png"
		elif select == 9:
			rod = "easy_catcher.png"
		elif select == 10:
			rod = "fire.png"
		elif select == 11:
			rod = "golden.png"
		return path + rod