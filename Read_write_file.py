allHostsUp = open('allhostsup.txt', 'a')
  for line in lines: # list from something else
    line = line.strip()
    allHostsUp.write("%s\n" % line)
 allHostsUp.close()
