#!/usr/bin/env python
# a bar plot with errorbars
from __future__ import division
import os,sys,re
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pylab 
import pandas as pd

def runningMeanFast(x, N):
    return np.convolve(x, np.ones((N,))/N)[(N-1):]

if __name__ == "__main__":
    file_name = sys.argv[1]
    #file_name = "disorder.tsv"
    outfile=re.sub('.tsv','',file_name)
    
    data = pd.read_csv(file_name, delimiter='\t')
    data=data.sort_values(by="Meff")
    
    #scores=data[['Score','ScoreMix','ScoreDiso']]
    #scores.plot(kind='box')
    
    score=data['Score']
    scoremix=data['ScoreMix']
    scorediso=data['ScoreDiso']
    fig = pylab.figure( figsize=(10,6))
    ax = pylab.subplot2grid((1,1),(0,0))
    plot=ax.violinplot(score,[1], points=20, widths=0.5,showmeans=True, showextrema=False, showmedians=False)
    plot=ax.violinplot(scoremix,[2], points=20, widths=0.5,showmeans=True, showextrema=False, showmedians=False)
    plot=ax.violinplot(scorediso,[3], points=20, widths=0.5,showmeans=True, showextrema=False, showmedians=False)
    xticklabels = ["Score","MixScore","DisoScore"]
    xticks = [1,2,3]
    ax.set_xticklabels(xticklabels)
    ax.set_xticks(xticks)
    pylab.title("Score for "+outfile)
    pylab.ylabel("Score")
    pylab.savefig(outfile+"-score.eps")
    pylab.clf()

    diso=data['Diso']
    mix=data['FractionMix']
    diso=data['FractionDiso']
    fig = pylab.figure( figsize=(10,6))
    ax = pylab.subplot2grid((1,1),(0,0))
    plot=ax.violinplot(diso,[1], points=20, widths=0.5,showmeans=True, showextrema=False, showmedians=False)
    plot=ax.violinplot(mix,[2], points=20, widths=0.5,showmeans=True, showextrema=False, showmedians=False)
    plot=ax.violinplot(diso,[3], points=20, widths=0.5,showmeans=True, showextrema=False, showmedians=False)
    xticklabels = ["Disorder","Mix-Contacts","Diso-Contacts"]
    xticks = [1,2,3]
    ax.set_xticklabels(xticklabels)
    ax.set_xticks(xticks)
    pylab.title("Score for "+outfile)
    pylab.ylabel("Fraction")
    pylab.savefig(outfile+"-fraction.eps")
    pylab.clf()
 
        
    newdata=data.loc[data['PPV'] >0]
    #foo=newdata.as_matrix(columns=['Meff','PPV'])
    
    
    meff=newdata['Meff']
    PPV=newdata['PPV']
    N=min(25,int(len(PPV)/2))
    PPVmean=runningMeanFast(PPV, N)
    PPVmix=newdata['PPVMix']
    PPVmixmean=runningMeanFast(PPVmix, N)
    PPVdiso=newdata['PPVDiso']
    PPVdisomean=runningMeanFast(PPVdiso, N)
    fig = pylab.figure( figsize=(10,6))
    ax = pylab.subplot2grid((1,1),(0,0))
    #plot=ax.violinplot(PPV,[1], points=20, widths=0.5,showmeans=True, showextrema=False, showmedians=False)
    #plot=ax.violinplot(PPVmix,[2], points=20, widths=0.5,showmeans=True, showextrema=False, showmedians=False)
    #plot=ax.violinplot(PPVdiso,[3], points=20, widths=0.5,showmeans=True, showextrema=False, showmedians=False)
    ax.plot(meff,PPV,'ro',label="PPV")
    ax.plot(meff,PPVmean,'r')
    ax.plot(meff,PPVmix,'bs',label="PPVmix")
    ax.plot(meff,PPVmixmean,'b')
    ax.plot(meff,PPVdiso,'go',label="PPVDiso")
    ax.plot(meff,PPVdisomean,'g')
    
    ax.legend()
    ax.set_xscale("log", nonposx='clip')
    pylab.title("PPV for "+outfile)
    pylab.ylabel("PPV")
    pylab.xlabel("Meff")
    pylab.savefig(outfile+"-PPV.eps")
    pylab.clf()

    disodata=data.loc[data['Meff'] >0]
    disomeff=disodata['Meff']
    Score=newdata['Score']
    N=min(25,int(len(Score)/2))
    Scoremean=runningMeanFast(Score, N)
    Scoremix=newdata['ScoreMix']
    Scoremixmean=runningMeanFast(Scoremix, N)
    Scorediso=newdata['ScoreDiso']
    Scoredisomean=runningMeanFast(Scorediso, N)
    fig = pylab.figure( figsize=(10,6))
    ax = pylab.subplot2grid((1,1),(0,0))
    #plot=ax.violinplot(Score,[1], points=20, widths=0.5,showmeans=True, showextrema=False, showmedians=False)
    #plot=ax.violinplot(Scoremix,[2], points=20, widths=0.5,showmeans=True, showextrema=False, showmedians=False)
    #plot=ax.violinplot(Scorediso,[3], points=20, widths=0.5,showmeans=True, showextrema=False, showmedians=False)
    ax.plot(meff,Score,'ro',label="Score")
    ax.plot(meff,Scoremean,'r')
    ax.plot(meff,Scoremix,'bs',label="Scoremix")
    ax.plot(meff,Scoremixmean,'b')
    ax.plot(meff,Scorediso,'go',label="ScoreDiso")
    ax.plot(meff,Scoredisomean,'g')
    
    ax.legend()
    ax.set_xscale("log", nonposx='clip')
    pylab.title("Score for "+outfile)
    pylab.ylabel("Score")
    pylab.xlabel("Meff")
    pylab.savefig(outfile+"-meanscore.eps")
    pylab.clf()
    
