import sys
sys.path.insert(1,'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import decorate

#5674

#5{
frecuencia770 = SinSignal(freq=770, amp=1, offset=0)
frecuencia1336 = SinSignal(freq=1336, amp=1, offset=0)

#6{
#770
frecuencia1477 = SinSignal(freq=1477, amp=1, offset=0)

#7{
frecuencia852= SinSignal(freq=852, amp=1, offset=0)
frecuencia1209 = SinSignal(freq=941, amp=1, offset=0)

#4{
#770
#1209

#//////

#5
wave_770 = frecuencia770.make_wave(duration=0.5, start=0.5, framerate=44100)
wave_1336 = frecuencia1336.make_wave(duration=0.5, start=0.5, framerate=44100)

#6
wave_770 = frecuencia770.make_wave(duration=0.5, start=1, framerate=44100)
wave_1477 = frecuencia1477.make_wave(duration=0.5, start=1, framerate=44100)

#7
wave_852 = frecuencia852.make_wave(duration=0.5, start=1.5, framerate=44100)
wave_1209 = frecuencia1209.make_wave(duration=0.5, start=1.5, framerate=44100)

#4
wave_770 = frecuencia770.make_wave(duration=0.5, start=2, framerate=44100)
wave_1209 = frecuencia1209.make_wave(duration=0.5, start=2, framerate=44100)

wave_sonido = (wave_770 + wave_1336) + (wave_770 + wave_1477) + (wave_852 + wave_1209) +(wave_770 + wave_1209)  

wave_sonido.write("output_daniela.wav")
