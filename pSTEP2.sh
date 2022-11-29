source pSTEP0.sh

for file in ${NAME}_*;do
    echo 'DIR=''"'$DIR'/'${file}'"' >> STEP0.sh;
    echo 'IN=''"'${file}'.vcf"' >> STEP0.sh;
    echo 'NAME=''"'${file}'"' >> STEP0.sh;
    cp STEP0.sh ./"${file}";
    rm STEP0.sh;
done;
