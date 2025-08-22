
#-----------Import Zone------------------------>>>

import os
import stat

#---------Import Zone END---------------------->>>


class file_writer():
	def edit(self,file_name,place,text):

		old_status = os.stat(file_name).st_mode & 0o777

		if not os.path.isfile(file_name):
			pass
		else:

			if not os.access(file_name,os.R_OK):
				read_flag = False
				os.chmod(file_name,old_status | stat.S_IRUSR)
			if not os.access(file_name,os.W_OK):
				write_flag = False
				os.chmod(file_name,old_status | stat.S_IWUSR)


			with open(file_name,"r") as file:
				lines=file.readlines()

				for i in range(len(lines)):
					if lines[i].strip().startswith(place):
						divide=lines[i].split(":")
						lines[i] = f"{divide[0]} : {text}\n"

			with open(file_name,"w") as file:
				file.writelines(lines)

			os.chmod(file_name,old_status)

