# MicroRNA promoter identification in hunman with a three-level prediction method
## Introduction
Our method includes three parts, (i) the datasets are represented by a novel feature extraction method called SCPseDNC, and a trained SVm model is used for first-level prediction; (ii) Ectract RPol II signal features and use the trained RF model to perform second-level prediction on the miRNA candidate promoters identified in (i); (iii) Innovatively using Pearson and Spearman correlation coefficients to characterize the correlation of RPol II distribution of promoters-promoters and promoters-non-promoters from a horizontal perspective, respectively. 
## Requirement
First, create the enviroment:
'''
conda create -n miPromPred python==3.7
conda activate miPromPred
'''
Next, install the packages:
'''
scikit-learn==0.23.1
pandas==1.3.5
numpy==1.18.1
'''
## Usage
**-- You can run the codes step by step using command line.**  

**1.Features Exraction**  

Calculate 25 features of the input fasta format transcript file.  
Input the fasta file of transcript, and the prepared hexamer table file. (The hexamer tables used in this experiment are in the folder "HexamerTables").
```
# Get the feature file named *OutputFeatures_dir*:

python2 ExtractFeatures transcript.fa ./HexamerTables/HexamerTable_*.txt OutputFeatures_dir
```
**NOTE**: For other species, you can calculate the hexamer tables as follows.
You need to input the fasta files of coding sequences and non-coding sequences.
```
# Get a hexame table file named *OutputHexamer_dir*:

python2 MakeHexamerTables.py codingRNA.fa noncodingRNA.fa OutputHexamer_dir.
```

**2.Model Training**  
You need to input the coding RNA and non-coding RNA features files obtained in ***1.Features Exraction***.
```
# Get the trained models:

python2 Model_training.py codingFeatures_file noncodingFeatures_file
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
