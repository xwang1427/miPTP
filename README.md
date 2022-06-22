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

python ../1.SCPseDNC/SCPseDNC.py --file fastaFile.txt --method SCPseDNC --lamada 4 --weight 0.1 --index ./index.txt --format csv --out FirstLevel_Features.csv
```
**1.2 prediction with trained model**
```
# Get the index file of predcited label 1 named *firstLevelPredIndex.csv*.

python firstLevelPredict.py --inputfile FirstLevel_Features.csv --predModel ./model/SVM.model --outfile firstLevelPredResults.csv --outIndexfile firstLevelPredIndex.csv
```

### 2.Second Level Prediction
**2.1 Extract the RPol II signal**  
Inout the index file of predcited label 1.
```
# Get the RPol II signal features:

R 
```
**3.Cross-species Model Prediction**  
You need to input the featrue file of the transcript to be predicted.
```
# Get the prediction result file named *OutputPredict_dir*:

python2 SpeciesNeutralModel_predict.py TranscriptFeatures_file OutputPredict_dir
```
**4.Plant-specific Model Prediction**  

+ Plant model trained with Arabidopsis data

```
python2 PlantExperiment1_modelPredict.py TranscriptFeatures_file OutputPredict1_dir
```
+ Plant model trained with Zea mays data

```
python2 PlantExperiment2_modelPredict.py TranscriptFeatures_file OutputPredict2_dir
```  

## Example
+ Features Extraction
```
python2 ./ExtractFeatures.py ./Example/test_transcripts.fa ./Example/HexamerTable.txt ./Example/features/test_transcriptsFeatures.txt
```
+ Model Prediction
```
python2 ./SpeciesNeutralModel_predict.py ./Example/features/test_transcriptsFeatures.txt ./Example/predicResult/test_PredResult.txt
```
