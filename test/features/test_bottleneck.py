"""Test of the module shennong.features.bottleneck"""

import os
import struct
import numpy as np
import pytest

from shennong.features.bottleneck import BottleneckProcessor


def test_available_weights():
    weights = BottleneckProcessor.available_weights()
    assert len(weights) == 3
    for w in ('BabelMulti', 'FisherMono', 'FisherTri'):
        assert w in weights
        assert os.path.isfile(weights[w])


@pytest.mark.parametrize('weights', ['BabelMulti', 'FisherMono', 'FisherTri'])
def test_weights(weights):
    # make sure all the pretrained weights are here, and contains the
    # required entries
    proc = BottleneckProcessor(weights=weights)
    assert proc.weights == weights
    assert list(proc._weights_data.keys()) == [
        'bn_std', 'input_mean', 'b2', 'b5',
        'input_std', 'W5', 'W7', 'W6', 'b6', 'b7', 'W3', 'W2',
        'context', 'b3', 'bn_mean', 'W1', 'b1']


@pytest.mark.parametrize('weights', ['BabelMulti', 'FisherMono', 'FisherTri'])
def test_process(audio, mfcc, weights):
    proc = BottleneckProcessor(weights=weights)
    feat = proc.process(audio)
    assert feat.shape == (140, 80)
    assert np.allclose(feat.times, mfcc.times)


# may fail to have approx arrays (because of random signal
# dithering), so we authorize 5 successive runs
@pytest.mark.flaky(reruns=5)
def test_compare_original(audio_8k, bottleneck_original):
    feat = BottleneckProcessor(weights='BabelMulti').process(audio_8k)
    assert bottleneck_original.shape == feat.shape
    assert bottleneck_original == pytest.approx(feat.data, abs=1e-2)