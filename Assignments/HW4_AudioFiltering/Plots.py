import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile



def makeZCSFigure():
    fs, xaudio = wavfile.read("femalecountdown.wav")
    xaudio = np.array(xaudio, dtype=np.int)
    x = xaudio/32768
    print(np.max(xaudio))
    win = 2000
    zcs = np.zeros_like(x)
    sign = np.zeros_like(x)
    sign[1::] = 0.5*np.abs(np.sign(x[1::]) - np.sign(x[0:-1]))
    sign_c = np.cumsum(sign)
    for i in range(x.size):
        si = max(0, i-win)
        ei = min(x.size-1, i+win)
        zcs[i] = (sign_c[ei]-sign_c[si])
    cutoff = 150
    y = xaudio[zcs > cutoff]
    plt.figure(figsize=(12, 6))
    #plt.subplot(311)
    plt.xlabel("Array Index")
    plt.ylabel("Audio Sample Value")
    plt.title("Original Audio Signal x")
    plt.plot(xaudio+32768)
    plt.plot([0, xaudio.size], [32768]*2, linestyle='--')
    plt.ylim([0, 65536])
    plt.xlim([0, x.size-1])
    plt.show()
    """
	plt.subplot(312)
    plt.plot(zcs)
    plt.xlim([0, x.size-1])
    plt.plot([0, zcs.size-1], [cutoff, cutoff], linestyle='--')
    plt.xlabel("Array Index")
    plt.ylabel("Zero Crossings")
    plt.subplot(313)
    plt.plot(y+32768)
    plt.xlim([0, x.size-1])
    plt.xlabel("Array Index")
    plt.ylabel("Audio Sample Value")
    plt.title("Filtered Audio y")
    plt.tight_layout()
    #plt.savefig("Consonants.png", bbox_inches='tight')
	"""


makeZCSFigure()
