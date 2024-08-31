import random, asyncio
from datetime import datetime

"""
THIS IS A TEST PYTHON SCRIPT TO TEST THEME SCOPES
"""
# Starting with class
class Timer:
	def __enter__(self):
		self.was = datetime.now()

	@staticmethod
	def dull(key=True, lists=[1, 2, '3', '''213''']):
		if key: pass
		else: return True, [1,2,3]

	def __exit__(self, f, u, c):
		self.diff = round((datetime.now() - self.was).total_seconds(), 2)
		print(f'\nTaken time: {self.diff}s')

extensions = {'jpg': 15 + 0.5, 'png': 25 - 0, 'gif': 50 * 1}

with Timer():
	print(f'\nHi, wanna now extension i love? Probably you did not ask, but here it is: {random.choice(list(extensions.keys()))}')

filter_string = r'[<>:"/\\|?*.]' if not list(extensions.keys())[0].startswith('p') else r'(?<![./-])\b\d{1,7}\b(?![.%])'

async def main(key=True, i=0, o='o'):
	pass

if __name__ == '__main__':
	asyncio.run(main(key=False))