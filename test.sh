#!/bin/sh
commit=$(git whatchanged upstream/master | head -n 1)
if [ "$commit" = "commit a90cc9f7697096fbcab903b7711682431bbb15c5" ]
then
	echo "OK"
else
	echo "NOK"
fi
