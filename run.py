import os

full_path = os.getcwd()

path = full_path + "/result_text"
files = os.listdir(path)
files.remove('.gitignore')

for n in range(len(files)):
  f = open(full_path + "/result_text/" + 'flame_{}.txt'.format(str(n)), 'r', encoding='UTF-8')
  data = f.read()
  print(data)
  #time.sleep(0.001)
  os.system('cls')
  f.close()



  