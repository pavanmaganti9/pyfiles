#rename the files at a time in a folder

import os

os.chdir('path of files')
for f in os.listdir():
  file_name, file_ext = os.path.splitext(f)
  
  #to remove white spaces
  f_title = f_title.strip()
  f_course = f_course.strip()
  
  # [1:] is to remove hash before name begin from number
  # zfill(2) - if number starts from zero -- 01,02,03.....,09,10,11....
  f_num = f_num.strip()[1:].zfill(2)
  
  f_title, f_course, f_num = file_name.split('-')
  
  print('{}-{}-{}{}'.format(f_num, f_course, f_title file_ext))
  
  new_name = '{}-{}-{}{}'.format(f_num, f_course, f_title file_ext)
  
  os.rename(f, new_name)
