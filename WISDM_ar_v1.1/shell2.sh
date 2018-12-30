a=`cat random`

for b in $a
do
	
	echo `awk -v var="$b" '{if($var==$1) print}' data.txt`

done

