from fmdt.core import (
    extract_all_information,
    extract_key_information,
    split_video_at_meteors,
    split_video_at_intervals,
) 

from fmdt.api import (
    detect,
    visu,
    count,
    detect_directory
)

from fmdt.args import (
    Args,
    DetectArgs,
    VisuArgs,
    Video,
    detect_args
)

from fmdt.utils import (
    condense_start_end,
)

from fmdt.truth import (
    WATEC6_DIR,
    WATEC12_DIR,
    HumanDetection,
    read_human_detection_csv,
    init_ground_truth,
    GroundTruth
)

from fmdt.download import (
    download_csvs,
    download_demo_mp4
)

from fmdt.config import (
    init,
    load_gt12,
    load_gt6,
    get_draco12,
    get_draco6
)

# from fmdt.truth import HumanDetection

MAJOR_VERSION = 0
MINOR_VERSION = 0
PATCH         = 25

VERSION = str(MAJOR_VERSION) + "." + str(MINOR_VERSION) + "." + str(PATCH)
