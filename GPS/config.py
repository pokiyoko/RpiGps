out = open('config.dat','w')

out.write(raw_input('Gmail Account: ')+",")
out.write(raw_input('Gmail Passworld: ')+",")
out.write(raw_input('Speed Limit: ')+",")

destination = int(raw_input('Number of persons to send Warning: '))

out.write(str(destination)+",")

for dest in range(destination):
	out.write(raw_input("Destination E-mail:" )+",")

out.close()
