#!/bin/bash                                                                                                   
atlas_sub="/usr/local/tool/fsl/data/atlases/HarvardOxford/HarvardOxford-sub-maxprob-thr25-2mm"
resultdir="/Users/xiaoqian/Projects/ROI/subcor/single"

n=`cat structure_sub.txt | wc -l`
echo $n
for ((i = 1; i <= $n; i++ ))
do
    num=`sed -n "${i} p" structure_sub.txt | cut -d: -f1`
    echo num=$num
    roi=`sed -n "${i} p" structure_sub.txt | cut -d: -f2 | sed 's/_mask//'`
    echo roi=$roi
    fslmaths $atlas_sub -thr $num -uthr $num -bin $resultdir/$roi
done
