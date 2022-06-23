# MicroRNA promoter identification in hunman with a three-level prediction method
## Introduction
Our method includes three parts, (i) the datasets are represented by a novel feature extraction method called SCPseDNC, and a trained SVm model is used for first-level prediction; (ii) Ectract RPol II signal features and use the trained RF model to perform second-level prediction on the miRNA candidate promoters identified in (i); (iii) Innovatively using Pearson and Spearman correlation coefficients to characterize the correlation of RPol II distribution of promoters-promoters and promoters-non-promoters from a horizontal perspective, respectively. 
## Requirement
First, create the enviroment:
```
conda create -n miPromPred python==3.7
conda activate miPromPred
```
Next, install the packages:
```
R version 3.2.3
sys, os, platform，argparse，re,itertools
scikit-learn==0.23.1
pandas==1.3.5
numpy==1.18.1
```
## Usage
**-- You can run the codes step by step using command line.**  
### 1.First Level Prediction
**1.1 Features Exraction**  
Input the fasta file of sequences.
```
# Get the feature file named *FirstLevel_Features.csv*:

python SCPseDNC/SCPseDNC.py --file fastaFile.txt --method SCPseDNC --lamada 4 --weight 0.1 --index ./index.txt --format csv --out FirstLevel_Features.csv
```
**1.2 Prediction with trained Model**
```
# Get the first-level prediction result files:

python firstLevelPredict.py --inputfile FirstLevel_Features.csv --predModel model/SVM.model --outfile firstLevelPredResults.csv --outIndexfile firstLevelPredIndex.csv
```

### 2.Second Level Prediction
**2.1 Extract the RPol II signal**  
Before extract the RPol II signal, organize the sequences predicted as label 1 in 1.2 into a txt (Tab as the delimiter) file containing the following information (please see the example/firstResults.txt):   
1 colum: sample annotaion information, (eg. hsa-mir-1);  
2 colum: chromsome;  
3 colum: strand;  
4 colum: sequence start coordinates;  
5 colum: sequence end coordinates.  
```
# Get the RPol II signal features:

Rscript extractRPol2.R -i firstResults.txt -p ChipSeq_Pol2.RData -o pol2Features.csv
```
**2.2 Prediction with trained Model**  
```
# Get the second-level prediction result files:

python secondLevelPredict.py --inputfile pol2Features.csv --predModel ./model/RF.model --outProbfile secondResutls.csv --outCandiPromfile secondPredResults_Label1.csv
```
### 3.Third Level Prediction
```
Rscript thirdLevelPredict.R -i secondPredResults_Label1.csv -x GenePromoters_x.RData -o OptimalPromoters.txt
```

## Example
+ 1 Features Exraction use SCPseDNC**  
```
python SCPseDNC/SCPseDNC.py --file example/test.txt --method SCPseDNC --lamada 4 --weight 0.1 --index SCPseDNC/indexes.txt --format csv --out example/features_SCPseDNC.csv
```
+ 2 First Level Prediciton**  
```
python firstLevelPredict.py --inputfile example/features_SCPseDNC.csv --predModel model/SVM.model --outfile example/firstPredResults.csv --outIndexfile example/firstPredResults_Index.csv
```
+ 3 Extract the RPol II signal
```
Rscript extractRPol2.R -i example/firstResults.txt -p ChipSeq_Pol2.RData -o example/features_pol2.csv
```
+ 4 Make Second Level Prediction
```
python secondLevelPredict.py --inputfile example/features_pol2.csv --predModel model/RF.model --outProbfile example/secondPredResults.csv --outCandiPromfile example/secondPredResults_Label1.csv
```
+ 5 Make Third Level Prediction
```
Rscript thirdLevelPredict.R -i example/secondPredResults_Label1.csv -x GenePromoters_x.RData -o example/OptimalPromoters.txt
```
