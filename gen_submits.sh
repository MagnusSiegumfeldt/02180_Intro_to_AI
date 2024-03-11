
runs=(
    "0 1 2 4" 
    "1 0 4 2" 
    "0 2 2 4" 
    "2 0 4 2" 
    "1 2 4 4" 
    "2 1 4 4"
    
    "0 1 2 6" 
    "1 0 6 2" 
    "0 2 2 6" 
    "2 0 6 2" 
    "1 2 6 6" 
    "2 1 6 6"
)

for i in "${runs[@]}"; do
    set -- $i;
    echo -e "#!/bin/sh 
### General options 
### -- specify queue -- 
#BSUB -q hpc
### -- set the job Name -- 
#BSUB -J 02180_AI_Test
### -- ask for number of cores (default: 1) -- 
#BSUB -n 1
### -- specify that the cores must be on the same host -- 
#BSUB -R "span[hosts=1]"
### -- specify that we need 4GB of memory per core/slot -- 
#BSUB -R "rusage[mem=4GB]"
##BSUB -R "select[model == XeonE5_2650v4]"
### -- specify that we want the job to get killed if it exceeds 5 GB per core/slot -- 
#BSUB -M 5GB
### -- set walltime limit: hh:mm -- 
#BSUB -W 24:00 
### -- send notification at start -- 
##BSUB -B 
### -- send notification at completion -- 
##BSUB -N 
### -- Specify the output and error file. %J is the job-id -- 
### -- -o and -e mean append, -oo and -eo mean overwrite -- 
#BSUB -o ./out/Output_%J.out 
#BSUB -e ./out/Output_%J.err 

python3 src/testrunner.py $1 $2 $3 $4" > ./submit/submit_${1}_${2}_${3}_${4}.sh
done

echo "" > submit_all.sh
for i in "${runs[@]}"; do
    set -- $i;
echo "bsub < ./submit/submit_${1}_${2}_${3}_${4}.sh" >> submit_all.sh
done

for i in "${runs[@]}"; do
    set -- $i;
    chmod +x ./submit/submit_${1}_${2}_${3}_${4}.sh
done