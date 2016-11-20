def run_command(command):
	launchresults = subprocess.check_output(command, shell=True)
	return launchresults
