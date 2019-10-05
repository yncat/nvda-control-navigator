# -*- coding: utf-8 -*-
# アドオンを再読み込みさせるバッチ的なもの
# Copyright (C) 2019 Yukio Nozawa <personal@nyanchangames.com>
import distutils.dir_util
import os
import sys
import subprocess

NVDA_ADDONS_PATH="C:\\Users\\nyanchan\\AppData\\Roaming\\nvda\\addons"
NVDA_EXECUTABLE_PATH="\"C:\\Program Files (x86)\\NVDA\\nvda_slave.exe\""

if not os.path.isdir(NVDA_ADDONS_PATH):
	print("アドオンディレクトリのパスがおかしいです。")
	sys.exit()
#end addon path
if not os.path.isdir(NVDA_ADDONS_PATH+"\\controlNavigator"):
	os.mkdir(NVDA_ADDONS_PATH+"\\controlNavigator")
#end making folder
distutils.dir_util.copy_tree("controlNavigator", "%s\\controlNavigator" % NVDA_ADDONS_PATH)
subprocess.run(NVDA_EXECUTABLE_PATH + " launchNVDA -r", shell=True)
