#!/usr/bin/env python
# coding: utf-8
#Second-level prediction of miRNA promoters

import argparse
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd
import joblib
from pandas.core.frame import DataFrame

def secPredict(inputfile, predModel,outProbfile,outCandiPromfile):
    # load model
    pred_model = joblib.load(predModel)
    # read the inputDataFile
    path = inputfile
    data = pd.read_csv(path, sep=',', header=0)
    data_x = data.iloc[ : , 5: ] # get 11 bins Pol2
    # print(data_x.shape,data.shape)

    pred_y = pred_model.predict(data_x)
    pred_yProba = pred_model.predict_proba(data_x)
    pred_yProba = DataFrame(pred_yProba)
    pred_yProba.to_csv(outProbfile,index=False,header=False,sep = ',')

    p_loca = np.where(pred_y == 1)
    predLable1_results = data.iloc[p_loca]
    predLable1_results.to_csv(outCandiPromfile,index=False,header=False,sep = ',')

    print('Second-Level Prediction Finished!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage="it's usage tip.",
                                     description="The Second-Level Prediction of miRNA promoters")
    parser.add_argument("--inputfile", required=True, help="input features file")
    parser.add_argument("--predModel", required=True, help="loading trained model")
    parser.add_argument("--outProbfile", help="the predict results file.")
    parser.add_argument("--outCandiPromfile", help="the annotation file of predicted label 1.")
    args = parser.parse_args()

    inputfile = args.inputfile
    predModel = args.predModel
    outProbfile = args.outProbfile
    outCandiPromfile = args.outCandiPromfile
    secPredict(inputfile, predModel, outProbfile, outCandiPromfile)

