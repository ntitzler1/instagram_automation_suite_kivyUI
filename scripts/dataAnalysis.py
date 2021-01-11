

def main():
	print("hello data")


	with open("../csvFiles/clientFiles/titzandfriends/fullUserList.txt", "r") as f:
		lines = f.readlines()

	
	item = lines[0].split(",")
	print(len(item))


	#figure out how many followers from the fullUserList have followed the account
if __name__ == '__main__':
	main()