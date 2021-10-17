import glob
import os
import json

all_files = glob.glob("c:\\code\\*.txt")
data = dict()
for each_file in all_files:
	try:
			with open(each_file) as fp:
				fn = os.path.basename(each_file)
				fn = fn.replace(".txt","")
				lines = fp.readlines()
				enemy_name = None
				HP = None
				LV = None
				STR = None
				DEF = None
				XP = None

				for each_line in lines:
					if "No. " in each_line:
						parse_data = each_line
						parse_data = each_line.split(" | ")
						enemy_name = parse_data[0]

					if "LV " in each_line:
						parsedata = each_line
						parsedata = parsedata.split("|")
						if parsedata[0][0:2].upper() == "LV":
							parsedata[0] = parsedata[0].replace("LV ","")
							LV = parsedata[0]
						parsedata = each_line
						parsedata = parsedata.split("|")
						if parsedata[1][0:4].upper() == " HP ":
							parsedata[1] = parsedata[1].replace(" HP ","")
							HP = parsedata[1]
					if "STR " in each_line:
						parsedata = each_line
						parsedata = parsedata.split("|")
						if parsedata[0][0:3].upper() == "STR":
							parsedata[0] = parsedata[0].replace("STR ","")
							STR = parsedata[0]
						parsedata = each_line
						parsedata = parsedata.split("|")
						if parsedata[1][0:5].upper() == " DEF ":
							parsedata[1] = parsedata[1].replace(" DEF ","")
							DEF = parsedata[1]
					if "EXP:" in each_line:
						parse_data = each_line
						parse_data = parse_data.split("|")
						parse_data = parse_data[1]
						parse_data = parse_data.replace(" ","")
						XP = parse_data
			data[fn] = dict()
			data[fn]["enemy_name"] = enemy_name
			LV = LV.replace(" ","")
			STR = STR.replace(" ","")
			DEF = DEF.replace(" ","")
			HP = HP.replace(" ","")
			XP = XP.replace(" ","")
			
			if LV.isdecimal() == False:
				LV = None
			if HP.isdecimal() == False:
				HP = None
			if STR.isdecimal() == False:
				STR = None
			if DEF.isdecimal() == False:
				DEF = None
			if XP.isdecimal() == False:
				XP = None
				
			data[fn]["LV"] = LV
			data[fn]["HP"] = HP
			data[fn]["STR"] = STR
			data[fn]["DEF"] = DEF
			data[fn]["EXP"] = XP
	except Exception as ExMsg:
		print (str(ExMsg))
		print ("Couldn't parse "+each_file)
with open ("c:\\code\\CV_SOTN_Enemy_Data.json",'w') as fo:
	try:
		json.dump(data, fo)
		print ("Successfully dumped c:\\code\\CV_SOTN_Enemy_Data.json")
	except Exception as ExMsg:
		print (str(ExMsg))
		print ("Couldn't write JSON file.")	