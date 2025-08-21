

class file_writer():
	def edit(self,file_name,place,text):
		if not os.path.isfile(file_name):
			pass
		else:
			with open(file_name,"r") as file:
				lines=file.readlines()

				for i in range(len(lines)):
					if lines[i].strip().startswith(place):
						divide=lines[i].split(":")
						lines[i] = f"{divide[0]} : {text}\n"

			with open(file_name,"w") as file:
				file.writelines(lines)



