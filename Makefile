all: lzmat_enc.c lzmat_dec.c
	gcc -c -Wall -Werror -fpic lzmat_dec.c
	gcc -c -Wall -Werror -fpic lzmat_enc.c
	gcc -shared -o liblzmat_dec.so lzmat_dec.o lzmat_enc.o

