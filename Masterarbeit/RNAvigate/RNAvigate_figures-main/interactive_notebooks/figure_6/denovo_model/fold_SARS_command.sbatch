#!/usr/bin/env bash
#SBATCH --job-name=foldsars
#SBATCH --output=foldsars_%A_%a.out
#SBATCH --time=3:00:00
#SBATCH --ntasks=24
#SBATCH --nodes=1

Fold-smp sars_1_8000.fa sars_1_8000_md300.ct --maxdistance 300
