def pyParseComplex(data):
	if len(data) == 5 :
		if data[0] == 'F' and data[1] == 'U' and data[2] == 'Z' and data[3] == 'Z' and data[4] == 'I' and data[5] == 'T':
			return True
	return False
