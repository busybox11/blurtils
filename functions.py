# Stolen from https://stackoverflow.com/questions/8924173/how-do-i-print-bold-text-in-python
class color:
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	END = '\033[0m'

def help():
	print('blurtils')
	print('A collection of useful image blur utilities')
	print()
	print(color.BOLD + 'HOW TO USE' + color.END)
	print()
	print(color.BOLD + '-i' + color.END + ' / ' + color.BOLD + '--input' + color.END + ' [FILE]')
	print('Input file')
	print(color.BOLD + 'Required parameter' + color.END)
	print()
	print(color.BOLD + '-o' + color.END + ' / ' + color.BOLD + '--output' + color.END + ' [FILE]')
	print('Output file')
	print('Optional parameter')
	print()
	print(color.BOLD + '-h' + color.END + ' / ' + color.BOLD + '--help' + color.END)
	print('Show this help menu')
	print('\n')
	print(color.BOLD + 'WHAT TO BLUR' + color.END)
	print('Choose one of the following two parameters')
	print()
	print(color.BOLD + '-f' + color.END + ' / ' + color.BOLD + '--full' + color.END)
	print('Full image blur')
	print()
	print(color.BOLD + '-a' + color.END + ' / ' + color.BOLD + '--area' + color.END + ' [TOP] [LEFT] [HEIGHT] [WIDTH]')
	print('Selected area image blur')
	print('Parameters:')
	print('  [TOP]    : Top padding of the selected image area')
	print('  [LEFT]   : Left padding of the selected image area')
	print('  [HEIGHT] : Height of the selected image area')
	print('  [WIDTH]  : Width of the selected image area')