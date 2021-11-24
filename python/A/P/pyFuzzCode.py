def BadCatcher(data):
	if data == b"OH YOU FUZZED ME!":
		raise RuntimeError("Entered Restricted Space")
