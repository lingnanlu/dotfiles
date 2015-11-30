import ctypes
import os
import shutil
import errno

kdll = ctypes.windll.LoadLibrary("kernel32.dll")

SOURCES_PREFIX = r'C:\Users\Administrator'
TARGETS_PREFIX = r'D:\dotfiles'

sources_to_targets = [
	(r'\AppData\Roaming\Sublime Text 2\Packages', r'\Sublime Text 2\Packages'),
	(r'\Documents\NetSarang\Xshell', r'\Xshell'),
	(r'\AppData\Roaming\Mozilla\Firefox', r'\Firefox'),
	(r'\.WebIde80\config', r'\.WebIde80\config'),
	(r'\.AndroidStudio1.4\config', r'\.AndroidStudio1.4\config'),
]

for item in sources_to_targets:
	source = SOURCES_PREFIX + item[0]
	target = TARGETS_PREFIX + item[1]
	print item[0] + " : " + item[1]

	if (os.path.exists(source)):
		try:
			os.rmdir(source)
		except OSError as ex:
			if ex.errno == errno.ENOTEMPTY:
				print source + " not empty "
				shutil.rmtree(source)

	kdll.CreateSymbolicLinkA(source, target , 1)





