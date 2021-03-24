import sys
import json

def flatten(d):
	result = {}

	def helper(o, name, first_run=False):
		if type(o) == dict:
			for key in o.keys():
				helper(o[key], key if first_run else name + "." + key)
		else:
			result[name] = o

	helper(d, "", True)
	return result

if __name__ == "__main__":
	input_json = ""
	for line in sys.stdin:
		input_json += line

	result = flatten(json.loads(input_json))
	print(json.dumps(result, indent = 4, sort_keys=True))