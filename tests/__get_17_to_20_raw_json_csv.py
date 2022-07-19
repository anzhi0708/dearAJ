import pathlib
import sys

HOME_DIR: pathlib.Path = pathlib.Path().home()
AJCORE_PY = HOME_DIR / "Public/py/dearAJ/src/dearaj/ajcore.py"

sys.path.append(AJCORE_PY.parent.as_posix())


import ajcore
import time

print(dir(ajcore))

print(ajcore.LOCAL_DATA_PATH)

for conf in ajcore.Conferences(17):
    if int(conf.ct2) <= 256:
        try:
            print(conf.conf_title)
            conf.to_csv_from_original_raw_json_data()
            time.sleep(3)
        except:
            import objprint
            objprint.op(conf)
            print("FOUND")
            break
    else:
        print(conf.ct2)