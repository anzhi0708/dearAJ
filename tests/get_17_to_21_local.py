import pathlib
import sys

HOME_DIR: pathlib.Path = pathlib.Path().home()
AJCORE_PY = HOME_DIR / "Public/py/dearAJ/src/dearaj/ajcore.py"

sys.path.append(AJCORE_PY.parent.as_posix())


import ajcore
import time

print(dir(ajcore))

print(ajcore.LOCAL_DATA_PATH)


def get(n):
    count: int = 0
    for conf in ajcore.Conferences(n):
        print(" ")
        print(f"{conf.vod_link}")
        print(f"getting gen{conf.ct1}, {conf.date} {conf.conf_title!r}... ", end="")
        conf.to_csv_from_original_raw_json_data()
        count += 1
        print("done\n")
        time.sleep(0.66)
    print(f"\nTOTAL: {count} (gen {n})")


if __name__ == "__main__":
    for n in range(17, 21):
        try:
            get(n)
            with open("./nth_got.log", "w") as log:
                log.write("")
        except Exception as e:
            with open("./nth_got.log", "w") as log:
                import time

                log.write(
                    f"retrying: {n} due to {e} ({time.strftime('%d %m %H:%M:%S')})\n"
                )
            get(n)
            with open("./nth_got.log", "w") as log:
                log.write("")
