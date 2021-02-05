# Important!
# Dont edit this file!

import os
import struct
check = os.listdir()
if 'bit_version' not in check: exit(os.system('xdg-open https://github.com/ZXRID/PPxGuard'))
elif 'threetwo' in os.listdir('bit_version') and 'sixfour' in os.listdir('bit_version'):
	if (struct.calcsize("P") * 8) == 32:
		from bit_version.threetwo import shield
	else: from bit_version.sixfour import shield
else: exit(os.system('xdg-open https://github.com/ZXRID/PPxGuard'))
