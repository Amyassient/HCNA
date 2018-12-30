#!/bin/bash
train_random=`cat random`
test_random=`cat random1`
if false
then
for i in $test_random
do
a=`awk -v var1="$i" '{if ($2=="Walking" && $1==var1) print($2)}' temp1_test_data | wc -l`
b=`awk -v var1="$i" '{if ($2=="Jogging" && $1==var1) print($2)}' temp1_test_data | wc -l`
c=`awk -v var1="$i" '{if ($2=="Standing" && $1==var1) print($2)}' temp1_test_data | wc -l`
d=`awk -v var1="$i" '{if ($2=="Sitting" && $1==var1) print($2)}' temp1_test_data | wc -l`
e=`awk -v var1="$i" '{if ($2=="Upstairs" && $1==var1) print($2)}' temp1_test_data | wc -l`
f=`awk -v var1="$i" '{if ($2=="Downstairs" && $1==var1) print($2)}' temp1_test_data | wc -l`
echo "$a" "$b" "$c" "$d" "$e" "$f"
A=`expr $a / 100 \* 100`
B=`expr $b / 100 \* 100`
C=`expr $c / 100 \* 100`
D=`expr $d / 100 \* 100`
E=`expr $e / 100 \* 100`
F=`expr $f / 100 \* 100`
echo "$A" "$B" "$C" "$D" "$E" "$F"
echo "\n"
`awk -v var1="$i" '{if ($2="Walking" && $1==var1) print}' temp1_test_data | head -n $A >> temp2_test_data`
`awk -v var1="$i" '{if ($2="Jogging" && $1==var1) print}' temp1_test_data | head -n $B >> temp2_test_data`
`awk -v var1="$i" '{if ($2="Standing" && $1==var1) print}' temp1_test_data | head -n $C >> temp2_test_data`
`awk -v var1="$i" '{if ($2=="Sitting" && $1==var1) print}' temp1_test_data | head -n $D >> temp2_test_data`
`awk -v var1="$i" '{if ($2=="Upstairs" && $1==var1) print}' temp1_test_data | head -n $E >> temp2_test_data`
`awk -v var1="$i" '{if ($2=="Downstairs" && $1==var1) print}' temp1_test_data | head -n $F >> temp2_test_data`
done
fi
for abc in $train_random
do
echo $abc
g=`awk -v var2="$abc" '{if ($2=="Walking" && $1==var2) print}' temp1_train_data | wc -l`
h=`awk -v var2="$abc" '{if ($2=="Jogging" && $1==var2) print}' temp1_train_data | wc -l`
i=`awk -v var2="$abc" '{if ($2=="Standing" && $1==var2) print}' temp1_train_data | wc -l`
j=`awk -v var2="$abc" '{if ($2=="Sitting" && $1==var2) print}' temp1_train_data | wc -l`
k=`awk -v var2="$abc" '{if ($2=="Upstairs" && $1==var2) print}' temp1_train_data | wc -l`
l=`awk -v var2="$abc" '{if ($2=="Downstairs" && $1==var2) print}' temp1_train_data | wc -l`
echo "$g" "$h" "$i" "$j" "$k" "$l"
G=`expr $g / 100 \* 100`
H=`expr $h / 100 \* 100`
I=`expr $i / 100 \* 100`
J=`expr $j / 100 \* 100`
K=`expr $k / 100 \* 100`
L=`expr $l / 100 \* 100`
echo "$G" "$H" "$I" "$J" "$K" "$L"
echo "\n"
`awk -v var2="$abc" '{if ($2=="Walking" && $1==var2) print}' temp1_train_data | head -n $G >> temp2_train_data`
`awk -v var2="$abc" '{if ($2=="Jogging" && $1==var2) print}' temp1_train_data | head -n $H >> temp2_train_data`
`awk -v var2="$abc" '{if ($2=="Standing" && $1==var2) print}' temp1_train_data | head -n $I >> temp2_train_data`
`awk -v var2="$abc" '{if ($2=="Sitting" && $1==var2) print}' temp1_train_data | head -n $J >> temp2_train_data`
`awk -v var2="$abc" '{if ($2=="Upstairs" && $1==var2) print}' temp1_train_data | head -n $K >> temp2_train_data`
`awk -v var2="$abc" '{if ($2=="Downstairs" && $1==var2) print}' temp1_train_data | head -n $L >> temp2_train_data`
done
if false
then
VAR1=`expr $A / 100`
VAR2=`expr $B / 100`
VAR3=`expr $C / 100`
VAR4=`expr $D / 100`
VAR5=`expr $E / 100`
VAR6=`expr $F / 100`
VAR7=`expr $G / 100`
VAR8=`expr $H / 100`
VAR9=`expr $I / 100`
VAR10=`expr $J / 100`
VAR11=`expr $K / 100`
VAR12=`expr $L / 100`

#test_labels
`awk '{if ($2=="Walking") print("1 0 0 0 0 0")}' temp1_train_data | head -n $VAR1 >> test_labels`
`awk '{if ($2=="Jogging") print("0 1 0 0 0 0")}' temp1_train_data | head -n $VAR2 >> test_labels`
`awk '{if ($2=="Standing") print("0 0 1 0 0 0")}' temp1_train_data | head -n $VAR3 >> test_labels`
`awk '{if ($2=="Sitting") print("0 0 0 1 0 0")}' temp1_train_data | head -n $VAR4 >> test_labels`
`awk '{if ($2=="Upstairs") print("0 0 0 0 1 0")}' temp1_train_data | head -n $VAR5 >> test_labels`
`awk '{if ($2=="Downstairs") print("0 0 0 0 0 1")}' temp1_train_data | head -n $VAR6 >> test_labels`
#train_labels
`awk '{if ($2=="Walking") print("1 0 0 0 0 0")}' temp1_train_data | head -n $VAR7 >> train_labels`
`awk '{if ($2=="Jogging") print("0 1 0 0 0 0")}' temp1_train_data | head -n $VAR8 >> train_labels`
`awk '{if ($2=="Standing") print("0 0 1 0 0 0")}' temp1_train_data | head -n $VAR9 >> train_labels`
`awk '{if ($2=="Sitting") print("0 0 0 1 0 0")}' temp1_train_data | head -n $VAR10 >> train_labels`
`awk '{if ($2=="Upstairs") print("0 0 0 0 1 0")}' temp1_train_data | head -n $VAR11 >> train_labels`
`awk '{if ($2=="Downstairs") print("0 0 0 0 0 1")}' temp1_train_data | head -n $VAR12 >> train_labels`
fi





