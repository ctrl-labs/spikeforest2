import kachery as ka
import hither_sf as hither

def sort(algorithm: str, recording_path: str):
    from spikeforest2 import sorters
    if not hasattr(sorters, algorithm):
        raise Exception('Sorter not found: {}'.format(algorithm))
    sorter = getattr(sorters, algorithm)
    if algorithm in ['kilosort2', 'kilosort', 'ironclust', 'tridesclous']:
        gpu = True
    else:
        gpu = False
    with hither.config(gpu=gpu):
        result = sorter.run(recording_path=recording_path, sorting_out=hither.File())
    print('SORTING')
    print('==============================================')
    return ka.store_file(result.outputs.sorting_out._path, basename='firings.mda')