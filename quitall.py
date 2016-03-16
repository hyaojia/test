from __future__ import print_function
import os

## This script is from http://www.mackungfu.org/quitting-everything

script_0 = '''
/usr/bin/env osascript <<-EOF
tell application "System Events" to set quitapps to name of every application process whose visible is true and name is not "Finder" and name is not "iTerm"
repeat with closeall in quitapps
	try
		tell application closeall to close every window
	end try
	quit application closeall
end repeat
EOF
'''

script_1 = '''
/usr/bin/env osascript <<-EOF

tell application "iTerm"

	close (every window whose name does not contain "1")

end tell
EOF
'''

print('Quitting all apps...')
os.system(script_0)
os.system(script_1)
