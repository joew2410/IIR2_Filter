# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 14:31:07 2017

@author: Joe
"""

import numpy as np
import scipy.io.wavfile as sci
import IIR_Filter as iir


if __name__ == "__main__":
    


    sample_rate, data = sci.read('assignment3_noise_speech.wav')          #import the recorded wavefile
    data = data[:,0]                                                      #splyce out one of the audio channels
    data_ft = np.fft.fft(data)                                            #perform the fast fourier transform on the first column of data, ignore second stereo channel
    x_axis_time = np.linspace(0,len(data_ft)/sample_rate,len(data_ft))    #set the x axis to show in seconds in the time domain
    faxis = np.linspace(0,sample_rate,len(data_ft))                       #set the x axis of the frequency domain to match the sampling rate
    N=len(data)
  
        
    #set up high pass filter
    order=4                                                                      #define desired filter order
    f0 = 300/sample_rate
    f1 = 7000/sample_rate
    cut=np.array([f0,f1])                                                          #define desired cutoff frequencies
    p3 = iir.IIR2Filter(order,cut,filter_type='bandpass',analogue_filter='butter',direct_form=2)  #instantiate the class, define filter type and analogue filter
    
                   
    
    #create an array for the filtered data
    filtered_data = np.zeros(N)                                                 
    
    #loop to implement the filter    
    for i in range(N):
        filtered_data[i] = p3.filter(data[i])
   
    #Write the processed data to an output .wav file
    filtered_data = np.int16(filtered_data)
    sci.write('assignment3_part4_filtered_noise_speech.wav', sample_rate, filtered_data)
    
