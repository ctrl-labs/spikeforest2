#!/usr/bin/env python

from spikeforest2_utils import test_sort_tetrode
import hither_sf as hither

def main():
    # I force using singularity for kilosort2 because on my computer, when docker tries to use gpu it messes up nvidia-container-cli and I need to restart the computer
    import os
    os.environ['HITHER_USE_SINGULARITY'] = 'TRUE'
    test_sort_tetrode(sorter_name='kilosort2', min_avg_accuracy=0.15, num_jobs=2, job_handler=hither.ParallelJobHandler(2))

if __name__ == '__main__':
    main()