#!/usr/bin/env python
# coding: utf-8
#First-level prediction of miRNA promoters

import argparse
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
from pandas.core.frame import DataFrame

def firPredict(inputfile, predModel,outfile,outIndexfile):
    # load model
    pred_model = joblib.load(predModel)
    # read the inputDataFile
    path = inputfile
    data = pd.read_csv(path, sep=',', header=None)
    data_x = data.iloc[ : , 1: ]

    #print(data_x.shape,data.shape)

    pred_x = StandardScaler().fit_transform(data_x)

    pred_y = pred_model.predict(pred_x)  #n*1
    pred_yProbability = pred_model.predict_proba(pred_x) #n*2 
    pred_yProbability = DataFrame(pred_yProbability)
    pred_yProbability.to_csv(outfile,index=False,header=False,sep = ',')

    p_loca = np.where(pred_y == 1) #the index of predcit label 1
    p_loca = DataFrame(np.transpose(p_loca))
    p_loca.to_csv(outIndexfile, index=False, header=False, sep = ',')
    
    print('First-Level Prediction Finished!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage="it's usage tip.",
                                     description="The First-Level Prediction of miRNA promoters")
    parser.add_argument("--inputfile", required=True, help="input features file")
    parser.add_argument("--predModel", required=True, help="loading trained model")
    parser.add_argument("--outfile", help="the predict results file.")
    parser.add_argument("--outIndexfile", help="the index file of predcited label 1.")
    args = parser.parse_args()

    inputfile = args.inputfile
    predModel = args.predModel
    outfile = args.outfile
    outIndexfile = args.outIndexfile
    firPredict(inputfile, predModel, outfile, outIndexfile)

