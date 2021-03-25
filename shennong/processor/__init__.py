"""Speech features extraction processors"""

from shennong.processor.bottleneck import BottleneckProcessor
from shennong.processor.crepepitch import (
    CrepePitchProcessor, CrepePitchPostProcessor)
from shennong.processor.energy import EnergyProcessor
from shennong.processor.filterbank import FilterbankProcessor
from shennong.processor.mfcc import MfccProcessor
from shennong.processor.onehot import FramedOneHotProcessor, OneHotProcessor
from shennong.processor.pitch import PitchProcessor, PitchPostProcessor
from shennong.processor.plp import PlpProcessor
from shennong.processor.rastaplp import RastaPlpProcessor
from shennong.processor.spectrogram import SpectrogramProcessor
from shennong.processor.vtln import VtlnProcessor
