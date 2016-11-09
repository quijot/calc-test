#!/bin/bash

sem=(1640 1650 1660 1670 1680 1690 1700 1710 1720 1730 1740 1750 1760 1770 1780 1790 1800 1810 1820 1830 1840 1850 1860 1870 1880 1890 1900 1909)
eps=(ALUM AZUL BCAR CATA EBYP ESQU IGM1 LHCL LPGS MA01 MZAC RWSN SL01 SRLP TUCU UCOR UNRO UNSA UYTA VBCA CORD GUAY MPL2 NESA PEJO PRNA RECO UYPA UYSO)

# convertir coordenadas xyz -> lla
source convert.sh

sol=sss/ibg
csv=csv
output=$csv/residuos.csv

echo -e "# ep\td_lat\td_lon\tfecha" > $output

for s in "${sem[@]}"
do
    :
    if [ ! -f $sol*P$s.crd ]; then
        wget ftp://ftp.sirgas.org/pub/gps/SIRGAS/$s/$sol*P$s.crd
    fi
    for ep in "${eps[@]}"
    do
        :
        ep_output=$csv/$ep.csv
        ep=$(cat $sol*P$s.crd | grep $ep | awk '{ print $2 }')
        x=$(cat $sol*P$s.crd | grep $ep | awk '{ print $4 }')
        y=$(cat $sol*P$s.crd | grep $ep | awk '{ print $5 }')
        z=$(cat $sol*P$s.crd | grep $ep | awk '{ print $6 }')
        epoch=$(cat $sol*P$s.crd | grep EPOCH | awk '{ print $6 }')
        if [ ! -z ${x+x} ]; then
            if [ ! -f $ep_output ]; then
                python correct.py $ep $x $y $z $epoch > $ep_output
            else
                python correct.py $ep $x $y $z $epoch >> $ep_output
            fi
            python correct.py $ep $x $y $z $epoch >> $output
        fi
    done
done

python makecharts.py

