PYTHON="python3"
COMPILER="teenytiny.py"
CC="gcc"
for i in $(ls examples/*.teeny); do
	BN=$(basename -s .teeny ${i})
	TTOUTPUT=$(${PYTHON} ${COMPILER} ${i} 2>&1)
	if [ $? -ne 0 ]; then
		echo "Error compiling $i: ${TTOUTPUT}"
	else
		mv out.c ${BN}.c
		CCOUTPUT=$(${CC} -o ${BN} ${BN}.c)
		if [ $? -ne 0 ]; then
			echo "Error compiling C output for $i: ${CCOUTPUT}"
		else
			echo "TEENY $i"
		fi
	fi
done


