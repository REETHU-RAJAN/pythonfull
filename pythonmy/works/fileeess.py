# with open('may batch.txt','x')as fileff:
#
#     fileff.close()
with open('may batch.txt', 'r') as fileff:
     x=fileff.readlines()
     #print(x[0])
#      # x.pop(2)
#      # print(x)
#      # e=x[1]
#      # x.remove(e)
#      # x.remove('lkclkkcd')
#      # print(x)
# #
# # import os
# # file='may batch.txt'
# # os.remove(file)
# # print(x)
# import fileinput
# file='may batch.txt'
# lines_to_del=[2,4]
# def delete_lines(file,lines_to_del):
#      with fileinput.input(file,inplace=True) as file:#file input.input is used to open the file in place,
#           # inplace=true chasnges are written back to the same file incase false then file there is no change
#
#           for i in file:
#                if file.lineno() not in lines_to_del:
#                     print(i.rstrip())# rstrip to remove space when delete lines there be space so
# delete_lines(file,lines_to_del)
#

#using strip method delete
# def del_lines(file_path,line_to_del):
#      with open(file_path,'r')as file:
#           lines=file.readlines()
#      lines=[line for line in lines if line.strip() not in line_to_del]
#      with open(file_path,'w')as file:
#           file.writelines(lines)
# file_path="may batch.txt"
# line_to_del=['line2','line4']
# del_lines(file_path,line_to_del)



