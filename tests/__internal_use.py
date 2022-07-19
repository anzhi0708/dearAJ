import pathlib
import sys

HOME_DIR: pathlib.Path = pathlib.Path().home()
AJCORE_PY = HOME_DIR / "Public/py/dearAJ/src/dearaj/ajcore.py"

sys.path.append(AJCORE_PY.parent.as_posix())


import ajcore
import time

print(dir(ajcore))

print(ajcore.LOCAL_DATA_PATH)

for n in range(17, 21):
    for conf in ajcore.Conferences(n):
        print(" ")
        print(f"{conf.vod_link}")
        print(f"getting {conf.date} {conf.conf_title}... ", end='')
        conf.to_csv_from_original_raw_json_data()
        print('done\n')
        time.sleep(1)
