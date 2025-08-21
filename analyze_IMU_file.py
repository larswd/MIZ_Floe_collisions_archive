import numpy as np
from scipy.signal import butter, filtfilt, detrend, csd
import pandas as pd


def analyse_IMU_file(src_file, file_id, tags, out_dir, fs, skip_n):

    # Reading files
    data_lib = pd.read_csv(src_file + "_B")
    filename = src_file + "_Bt"
    with open(filename, 'r') as infile: 
        lines = infile.readlines()
        t = np.zeros(len(lines))
        for i,line in enumerate(lines):
            t[i] = float(line)

    t = t/1000 # ms to s

    # Skipping the first skip_n datapoints
    t = t[skip_n:] 
    Nt = len(t)

    # Computing magnitude of horizontal acceleration and vertical acceleration. 
    horizontal_mag = np.sqrt(data_lib[tags[0]].to_numpy()[skip_n:]**2 + data_lib[tags[1]].to_numpy()[skip_n:]**2)
    vertical_ac = data_lib[tags[2]].to_numpy()[skip_n:]

    # Noise filtering using a lowpass filter
    order = 5
    cutoff = 0.3
    b, a = butter(order, cutoff, fs=fs, btype='low', analog=False)
    filtered_ac = filtfilt(b,a,horizontal_mag)


    # Standard deviation and average of extracted noise
    noise = horizontal_mag[:Nt]-filtered_ac[:Nt]
    noisy_avg = np.sum(noise)/Nt
    std_noise = np.sqrt(np.sum((noise-noisy_avg)**2)/Nt)

    # Computing the significant waveheight from filtered vertical acceleration and double integration with fft
    detrended_vert = detrend(vertical_ac)
    Y = np.fft.fft(detrended_vert[:Nt])
    freq = np.fft.fftfreq(len(t), d=1.0/fs)
    weights = -1.0/(2*np.pi*freq)**2
    
    # Filtering algorithm
    f1 = 0.03
    f2 = 0.04
    Yf = np.zeros_like(Y)
    ind = np.argwhere(np.logical_and(freq >= f1, freq <= f2))
    Yf[ind] = Y[ind] * 0.5 * (1 - np.cos(np.pi * (freq[ind] - f1) / (f2 - f1))) * weights[ind]
    Yf[freq > f2] = Y[freq > f2] * weights[freq > f2]
    eta = -np.real(np.fft.ifft(2 * Yf))
    #Wavestats
    SWH = 4*np.std(eta)
    IMU_nfft = 2**13
    IMU_nperseg = IMU_nfft / 8.0
    IMU_noverlap = IMU_nperseg / 2.0
    IMU_buffer =  int(120 * fs)
    eta_red = eta[IMU_buffer:-IMU_buffer]
    f11, p11 = csd(eta_red, eta_red, fs=fs, nperseg=IMU_nperseg, noverlap=IMU_noverlap, nfft=IMU_nfft, return_onesided=True)
    Tp  = 1.0/f11[np.argmax(p11)]
    accX = data_lib[tags[0]].to_numpy()[skip_n:]
    accY = data_lib[tags[1]].to_numpy()[skip_n:]
    accZ = data_lib[tags[2]].to_numpy()[skip_n:]
    ak = 4*(np.pi)**2 * SWH/(9.83*Tp**2)

    # Temperature 
    temp = data_lib[" Temp"].to_numpy()[skip_n:]
    return noisy_avg.real, std_noise, SWH, Tp, ak, detrended_vert, filtered_ac,t, accX, accY, accZ, eta, temp

