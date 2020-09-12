{\rtf1\ansi\ansicpg1252\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Write your code here.\
import unittest\
\
def code_is_valid(text):\
	d = \{'\{': 1, '\}': -1, '[': 2, ']': -2, '(': 3, ')': -3\}\
	l = [d[val] for val in list(text) if val in d]\
	\
	queue = []\
	\
	for val in l:\
		if val > 0:\
			queue.append(val)\
		else:\
			if len(queue) < 1:\
				return False\
			old_val = queue.pop()\
			if val + old_val != 0:\
				return False\
				\
	return len(queue) == 0\
	\
	\
class ExampleTest(unittest.TestCase):\
	def test(self):\
		self.assertEqual(code_is_valid('\{[a + b](c*d)\}'), True)\
		self.assertEqual(code_is_valid('foo[\{]'), False)\
		self.assertEqual(code_is_valid('\{[(])\}'), False)\
		self.assertEqual(code_is_valid('\{\}'), True)\
		self.assertEqual(code_is_valid('['), False)\
		self.assertEqual(code_is_valid('\{(\{[]\})\}'), True)\
\
\
if __name__ == '__main__':\
	unittest.main()\
\
}