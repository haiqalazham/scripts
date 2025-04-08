import re
import subprocess
import sys

def replace_with_full_block(text):
	# Define the full block Unicode character
	full_block = "\u2588"
	# Replace all alphanumeric characters with the full block
	replaced_text = re.sub(r"[a-zA-Z0-9]", full_block, text)
	return replaced_text

def copy_to_clipboard(text):
	# Copy to clipboard using platform-specific commands
	if sys.platform == "darwin":  # macOS
		subprocess.run("pbcopy", universal_newlines=True, input=text)
	else:
		print("Clipboard copy not supported on this platform.")

if __name__ == "__main__":
	# Prompt the user to input the string
	user_input = input("Enter the text to transform: ")
	# Transform the input string
	result = replace_with_full_block(user_input)
	# Copy the result to the clipboard
	copy_to_clipboard(result)
	# Print the result
	print("\nTransformed text (also copied to clipboard):")
	print(result)
