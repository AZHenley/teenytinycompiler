PYTHON="python3"
COMPILER="teenytiny.py"
CC="gcc"

function comp {
	BN=$(basename -s .teeny $1)
	TTOUTPUT=$(${PYTHON} ${COMPILER} $1 2>&1)
	if [ $? -ne 0 ]; then
		echo "${TTOUTPUT}"
	else
		mv out.c ${BN}.c
		CCOUTPUT=$(${CC} -o ${BN} ${BN}.c)
		if [ $? -ne 0 ]; then
			echo "${CCOUTPUT}"
		else
			echo "${TTOUTPUT}"
		fi
	fi
}

if [ $# -eq 0 ]; then
	for i in $(ls examples/*.teeny); do
		comp $i
	done
else
	comp $1
fi