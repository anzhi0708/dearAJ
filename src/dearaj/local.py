"""
This module provides functions and classes for performing
operations on local csv data files.
"""
import ajcore as core
from ajcore import MP, MPList, Movie, Speak

__all__ = [
    "core",
    "MP",
    "MPList",
    "Conference",
    "Conferences",
    "Movie",
    "Speak"
]


class Conference:
    """Conference from local data."""

    __slots__ = "angun_base", "sami", "minutes", "ct1", "ct2", "ct3", "menu", "type", "movie_list", "open_time", "week", "hand_lang", "date", "mc", "minutes_type", "audio_service", "title", "angun", "qvod"

    def __init__(
        self,
        angun_base: str,
        sami: str,
        minutes: str,
        ct1: str,
        ct2: str,
        ct3: str,
        menu: str,
        type: str,
        movie_list: list[dict],
        open_time: str,
        week: str,
        hand_lang: str,
        date: str,
        mc: str,
        minutes_type: str,
        audio_service: int,
        title: str,
        angun: list[dict],
        qvod: int
    ):
        self.angun_base: str = angun_base
        self.sami: str = sami
        self.minutes: str = minutes
        self.ct1: str = ct1
        self.ct2: str = ct2
        self.ct3: str = ct3
        self.menu: str = menu
        self.type: str = type
        self.movie_list: list[dict] = movie_list
        self.open_time: str = open_time
        self.week: str = week
        self.hand_lang: str = hand_lang
        self.date: str = date
        self.mc: str = mc
        self.minutes_type: str = minutes_type
        self.audio_service: int = audio_service
        self.title: str = title
        self.angun: list[dict] = angun
        self.qvod: int = qvod


class Conferences:
    """Load data from local disk"""
    __slots__ = "files", "conferences"

    def __init__(self, nth: int):
        print(len(core.Local.files))
        self.files = []
        for file in core.Local.files:
            if f"gen{nth}" in str(file):
                self.files.append(file)
        self.conferences = []
        import csv
        import json
        for file in self.files:
            with open(file, "r") as conf_file:
                reader = csv.reader(conf_file)
                for line in reader:
                    current_raw_data = json.loads(line[0])
                    # import pprint
                    # pprint.pp(current_raw_data)
                    # self.conferences.append(
                    current_conf_movies_dict_data_list: list = current_raw_data['movieList']
                    current_conf_movies_list: list = []
                    for current_movie in current_conf_movies_dict_data_list:
                        current_movie_speak_list: list = current_movie.get('subList')
                        current_conf_movies_list.append(
                            Movie(
                                current_movie.get('realTime'),
                                current_movie['playTime'],
                                current_movie['speakType'],
                                current_movie['no'],
                                [
                                    Speak(
                                        d.get('realTime'),
                                        d.get('playTime'),
                                        d.get('speakType'),
                                        d.get('no'),
                                        d.get('movieTitle'),
                                        d.get('wv')
                                    )
                                    for d in current_movie_speak_list
                                ] if current_movie_speak_list is not None else []
                            )
                        )
                    current_conf = Conference(
                            current_raw_data['angunBase'],
                            current_raw_data['sami'],
                            current_raw_data['minutes'],
                            current_raw_data['ct1'],
                            current_raw_data['ct2'],
                            current_raw_data['ct3'],
                            current_raw_data['menu'],
                            current_raw_data['type'],
                            # current_raw_data['movieList'],
                            current_conf_movies_list,
                            current_raw_data['confOpenTime'],
                            current_raw_data['confWeek'],
                            current_raw_data['handlang'],
                            current_raw_data['confDate'],
                            current_raw_data['mc'],
                            current_raw_data['munitesType'],
                            current_raw_data['audioService'],
                            current_raw_data['confTitle'],
                            current_raw_data['angun'],
                            current_raw_data['qvod'],
                        # )
                    )
                    self.conferences.append(current_conf)

    def __iter__(self):
        return iter(self.conferences)
