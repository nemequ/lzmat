from ctypes import *
import binascii


lzmat = cdll.LoadLibrary('./liblzmat_dec.so')

def MAX_LZMAT_ENCODED_SIZE(sz):
	return ((sz)+(((sz)+7)>>3)+0x21)

def main():
	buf = create_string_buffer("This is a test")
	cb = c_int(len(buf))
	cbOut = MAX_LZMAT_ENCODED_SIZE(len(buf))
	buf1 = create_string_buffer(cbOut)
	cbOut = c_int(cbOut)
	retval = lzmat.lzmat_encode(byref(buf1), byref(cbOut), byref(buf), len(buf))
	if retval == 0:
		print("Compression SUCCESS!\nCompressed Data: ")
		print(buf1.raw[:cbOut.value])
		buf2 = create_string_buffer(cb.value)
		retval = lzmat.lzmat_decode(byref(buf2), byref(cb), byref(buf1), len(buf1))
		if retval == 0:
			print("Decompress SUCCESS!\nDecompress Data: ")
			print(buf2.raw)



main()
