from subprocess import call, DEVNULL
import os, sys

def logo():
	logo = """
   _____ __    ____             __     
  / ___// /_  / __ )_______  __/ /____ 
  \\__ \\/ __ \\/ __  / ___/ / / / __/ _ \\
 ___/ / / / / /_/ / /  / /_/ / /_/  __/
/____/_/ /_/_____/_/   \\__,_/\\__/\\___/
nopebee7 [@] skullxploit	
	"""
	print(logo)

def opt():
	filename = input(" [+] target file > ")
	if not os.path.exists(filename):
		print(" [-] target file not found")
		exit()
	wordlist = input(" [+] wordlist > ")
	if not os.path.exists(wordlist):
		print(" [-] wordlist file not found")
		exit()
	wordlist = open(wordlist, "r+").readlines()
	return filename, wordlist

def out(msg: str):
    last_msg_length = len(out.last_msg) if hasattr(out, 'last_msg') else 0
    print(' ' * last_msg_length, end='\r')
    print(msg, end='\r')
    sys.stdout.flush()
    out.last_msg = msg

def tesPass(word, target, output):
	out(" [+] trying with pass : "+word)
	cmd = 'steghide extract -sf {0} -p {1}'.format(target, word)
	if call(cmd.split(), stdout=DEVNULL, stderr=DEVNULL) == 0:
		out("")
		open(output, "a").write(word)
		print(" [#] found password : "+word)
		exit()


if __name__ == "__main__":
	logo()
	sx = opt()
	if "." in sx[0]: output = sx[0].split('.')[0] + "_pass.txt"
	else: output = sx[0] + "_pass.txt"
	for word in sx[1]:
		word = word.replace("\n", "").replace("\r", "")
		tesPass(word, sx[0], output)