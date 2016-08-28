
import sys
import os
import glob
import struct

code = '';
addrdb = {};


def findNearestMFLRR0(code, pos):
	pos = (pos // 4) * 4;
	term = pos - 0x1000;
	if term < 0:
		term = 0;
	while (pos >= term) :
		if (code[pos: pos + 4] == '\x7C\x08\x02\xA6'):
			return pos;
		pos -= 4;
	return 0;
	
def findFunction(code, sig):
	
	t = code.find(sig);
	if (t == -1):
		return 0;
	return  findNearestMFLRR0(code, t);


def parseHexStr(s):
	t = '';
	for i in s.split(' '):
		if (len(i) > 0): 
			t += chr(int('0x' + i, 0));
	return t;


with open(sys.argv[1], 'rb') as f:
	code = f.read();

cfgGetLanguage = findFunction(code, parseHexStr('28 00 00 01 41 82 00 24  28 00 00 10 41 82 00 28'));

cfgGetRegion = findFunction(code, parseHexStr('94 21 FF A8 93 E1 00 54  7C 7F 1B 78 90 01 00 5C 38 00 00 23 39 60 00 00  7C 09 03 A6 39 81 00 06 B5 6C 00 02 42 00 FF FC'));


print("cfgGetLanguage: %08x, cfgGetRegion: %08x" % (cfgGetLanguage, cfgGetRegion));