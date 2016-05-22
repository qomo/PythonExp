import wave
import numpy as np
import pylab as pl


f = wave.open("./filco.wav", "rb")

params = f.getparams()
nchanels, sampwidth, framerate, nframes = params[:4]

str_data = f.readframes(nframes)

f.close()

wave_data = np.fromstring(str_data, dtype=np.short)
wave_data.shape = -1, 2
wave_data = wave_data.T
time = np.arange(0, nframes) * (1000.0/framerate)

pl.plot(time, wave_data[0])
pl.ylabel("sound")
pl.xlabel("time (ms)")
pl.grid(True)
pl.show()