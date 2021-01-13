while true;
do
	# get number of connections from "contador" file
	n=$(cat ~/SSI/examen-tunneling/contador)
	n=$(($n + 1))	
	echo $n > ~/SSI/examen-tunneling/contador

	echo "HTTP/1.1 200 OK" > index
	echo >> index
	echo "<!doctype html><html><body><h1>Connections: $n</h1></body></html>" >> index

	cat index | nc -q 1 -l 2000;
	

done
