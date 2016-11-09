#!/bin/bash
xyz=coord.xyz
lla=coordp07
echo -e "#!/usr/bin/env python\n\n
# Coordenadas Oficiales POSGAR07, geodésicas\n
posgar07 = {" > $lla
for ep in "${eps[@]}"
do
    :
    st=$(cat $xyz | grep $ep | awk '{ print $1 }')
    x=$(cat $xyz | grep $ep | awk '{ print $2 }')
    y=$(cat $xyz | grep $ep | awk '{ print $3 }')
    z=$(cat $xyz | grep $ep | awk '{ print $4 }')
    epoch=$(cat $xyz | grep $ep | awk '{ print $5 }')
    python xyz2lla.py $ep $x $y $z $epoch >> $lla
done
echo "}" >> $lla
mv $lla $lla.py

