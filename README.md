<div align="center">

  <img src="https://raw.githubusercontent.com/anzhi0708/dearAJ/main/img/logo.png" />

</div>

<br>

<div align="center">

  [![last-commit](https://img.shields.io/github/last-commit/anzhi0708/dearAJ?style=social)](https://github.com/anzhi0708/yeongnok/commits/main)    ![pypi-version](https://img.shields.io/pypi/v/dearaj?color=blue&style=flat-square) ![license](https://img.shields.io/github/license/anzhi0708/dearAJ?color=blue&style=flat-square)    ![repo-size](https://img.shields.io/github/repo-size/anzhi0708/dearAJ?style=social)

</div>


# dearAJ

**Data analysis tool for Korean National Assembly**

- [Installation](https://github.com/anzhi0708/dearAJ#install)
- [Usage](https://github.com/anzhi0708/dearAJ#usage)
  - fn&nbsp;&nbsp;&nbsp;&nbsp;get_normal_page_of
  - fn&nbsp;&nbsp;&nbsp;&nbsp;get_conf_vod_link
  - fn&nbsp;&nbsp;&nbsp;&nbsp;get_conf_movie_info
  - fn&nbsp;&nbsp;&nbsp;&nbsp;get_conf_file_info
  - fn&nbsp;&nbsp;&nbsp;&nbsp;get_conf_vod_chunks
  - fn&nbsp;&nbsp;&nbsp;&nbsp;get_conf_pdf
  - fn&nbsp;&nbsp;&nbsp;&nbsp;[get_conferences_of](https://github.com/anzhi0708/dearAJ#get_conferences_of)(nth: int, save: bool, to: str, sleep: Union[float, int])
  - cls&nbsp;&nbsp;&nbsp;[Speak](https://github.com/anzhi0708/dearAJ#speak)
  - cls&nbsp;&nbsp;&nbsp;[Movie](https://github.com/anzhi0708/dearAJ#movie)
  - cls&nbsp;&nbsp;&nbsp;[Conference](https://github.com/anzhi0708/dearAJ#conferences)
  - cls&nbsp;&nbsp;&nbsp;[Conferences](https://github.com/anzhi0708/dearAJ#conferences)
  - cls&nbsp;&nbsp;&nbsp;[MP](https://github.com/anzhi0708/dearAJ#mplist)
  - cls&nbsp;&nbsp;&nbsp;[MPList](https://github.com/anzhi0708/dearAJ#mplist)
- [License](https://github.com/anzhi0708/dearAJ#license)

## Install

```bash
pip3 install dearaj
```
or
```bash
git clone https://github.com/anzhi0708/dearAJ
cd dearAJ
make install
```

## Usage

```python
from dearaj import *
```

### MPList

Collection of single `MP`s using data from [열린국회정보](https://open.assembly.go.kr/portal/assm/search/memberHistSchPage.do).

```python
>>> MPList(20)
MPList(male=267, female=53, total=320)
```
```python
>>> for mp in MPList(19):
...     if mp.name == '문재인':
...             print(mp)
...
MP(generation=19, name='문재인', party='민주통합당', committee=[], region='부산 사상구', gender='남', n='초선', how='지역구')
```

### Conferences

`Conferences(n)` is the collection of the `n`th assembly's conferences. A `Conferences` object can hold multiple `Conference` objects.

`Conference`s are the children of `Conferences`s.

```python
>>> Conferences(19)
<Conferences of 19th, total: 2605>
>>> Conferences(19)[0]
Conference(sami='1', angun_type=[], minutes='1', ct1='19', ct2='342', ct3='01', open_time='10:25', date='2016-05-19', hand_lang='0', mc='10', conf_title='제342회 국회(임시회) 제01차 본회의', comm_name='본회의', qvod=0)
```

### Movie

A `Movie` object contains multuple `Speak`s, and other meta info. Sometimes a single `Conference` has multuple `Movie`s.

```python
>>> Conferences(20)[69].movies
[Movie(real_time='10:09:00', play_time='00:07:12', speak_type='전체보기', no=486665, sublist=[{'realTime': '10:09:04', 'playTime': '00:00:43', 'speakType': '개의', 'no': 486701, 'movieTitle': '안규백 위원장(더불어민주당)  개의, 발언', 'wv': 0}, {'realTime': '10:09:47', 'playTime': '00:01:26', 'speakType': '인사', 'no': 486702, 'movieTitle': '모종화 청장(병무청)  인사', 'wv': 0}, {'realTime': '10:11:13', 'playTime': '00:04:54', 'speakType': '정회', 'no': 486703, 'movieTitle': '안규백 위원장(더불어민주당)  발언, 의사일정 제1항 상정, 정회', 'wv': 0}]), Movie(real_time='10:24:00', play_time='01:26:47', speak_type='전체보기', no=486700, sublist=[{'realTime': '10:24:05', 'playTime': '00:01:34', 'speakType': '속개', 'no': 486704, 'movieTitle': '안규백 위원장(더불어민주당)  속개, 발언, 의사일정 제2항~제4항, 제33항~제40항 상정제1항 의결', 'wv': 0}, {'realTime': '10:25:39', 'playTime': '00:03:30', 'speakType': '보고', 'no': 486705, 'movieTitle': '백승주 위원(미래통합당)  보고', 'wv': 0}, {'realTime': '10:29:10', 'playTime': '00:00:29', 'speakType': '발언', 'no': 486706, 'movieTitle': '안규백 위원장(더불어민주당)  발언', 'wv': 0}, {'realTime': '10:29:39', 'playTime': '00:05:33', 'speakType': '질의', 'no': 486707, 'movieTitle': '백승주 위원(미래통합당)  질의 / 박재민 차관(국방부)  답변 / 안규백 위원장(더불어민주당)  발언', 'wv': 0}, {'realTime': '10:35:13', 'playTime': '00:01:13', 'speakType': '발언', 'no': 486708, 'movieTitle': '안규백 위원장(더불어민주당)  발언', 'wv': 0}, {'realTime': '10:36:27', 'playTime': '00:01:21', 'speakType': '발언', 'no': 486709, 'movieTitle': '서청원 위원(무소속)  발언', 'wv': 0}, {'realTime': '10:37:49', 'playTime': '00:00:14', 'speakType': '발언', 'no': 486710, 'movieTitle': '안규백 위원장(더불어민주당)  발언', 'wv': 0}, {'realTime': '10:38:03', 'playTime': '00:05:01', 'speakType': '질의', 'no': 486711, 'movieTitle': '박맹우 위원(미래통합당)  질의 / 박재민 차관(국방부)  답변', 'wv': 0}, {'realTime': '10:43:04', 'playTime': '00:05:42', 'speakType': '질의', 'no': 486712, 'movieTitle': '김진표 위원(더불어민주당)  질의 / 박재민 차관(국방부)  답변 / 이남우 인사복지실장(국방부)  답변', 'wv': 0}, {'realTime': '10:48:47', 'playTime': '00:04:32', 'speakType': '질의', 'no': 486713, 'movieTitle': '서청원 위원(무소속)  질의 / 박재민 차관(국방부)  답변', 'wv': 0}, {'realTime': '10:53:19', 'playTime': '00:05:04', 'speakType': '질의', 'no': 486714, 'movieTitle': '민홍철 위원(더불어민주당)  질의 / 박재민 차관(국방부)  답변 / 모종화 청장(병무청)  답변', 'wv': 0}, {'realTime': '10:58:24', 'playTime': '00:03:54', 'speakType': '법안', 'no': 486715, 'movieTitle': '안규백 위원장(더불어민주당)  발언, 의사일정 제2항~제4항, 제33항~제40항 의결', 'wv': 0}, {'realTime': '11:02:19', 'playTime': '00:00:24', 'speakType': '인사', 'no': 486716, 'movieTitle': '박재민 차관(국방부)  인사', 'wv': 0}, {'realTime': '11:02:43', 'playTime': '00:00:33', 'speakType': '발언', 'no': 486717, 'movieTitle': '안규백 위원장(더불어민주당)  발언', 'wv': 0}, {'realTime': '11:03:16', 'playTime': '00:05:12', 'speakType': '질의', 'no': 486718, 'movieTitle': '이종명 위원(미래한국당)  질의 / 박재민 차관(국방부)  답변', 'wv': 0}, {'realTime': '11:08:28', 'playTime': '00:00:28', 'speakType': '발언', 'no': 486719, 'movieTitle': '안규백 위원장(더불어민주당)  발언 / 박재민 차관(국방부)  발언', 'wv': 0}, {'realTime': '11:08:57', 'playTime': '00:03:24', 'speakType': '질의', 'no': 486720, 'movieTitle': '김중로 위원(미래통합당)  질의 / 박재민 차관(국방부)  답변', 'wv': 0}, {'realTime': '11:12:21', 'playTime': '00:00:32', 'speakType': '발언', 'no': 486721, 'movieTitle': '안규백 위원장(더불어민주당)  발언 / 박재민 차관(국방부)  발언', 'wv': 0}, {'realTime': '11:12:53', 'playTime': '00:04:44', 'speakType': '질의', 'no': 486722, 'movieTitle': '홍영표 위원(더불어민주당)  질의 / 박재민 차관(국방부)  답변', 'wv': 0}, {'realTime': '11:17:37', 'playTime': '00:06:19', 'speakType': '질의', 'no': 486723, 'movieTitle': '이주영 위원(미래통합당)  질의 / 박재민 차관(국방부)  답변', 'wv': 0}, {'realTime': '11:23:57', 'playTime': '00:05:45', 'speakType': '질의', 'no': 486724, 'movieTitle': '도종환 위원(더불어민주당)  질의 / 박재민 차관(국방부)  답변 /    실무자  답변', 'wv': 0}, {'realTime': '11:29:42', 'playTime': '00:01:02', 'speakType': '발언', 'no': 486725, 'movieTitle': '안규백 위원장(더불어민주당)  발언 / 이남우 인사복지실장(국방부)  발언', 'wv': 0}, {'realTime': '11:30:44', 'playTime': '00:05:18', 'speakType': '질의', 'no': 486726, 'movieTitle': '최재성 위원(더불어민주당)  질의 / 박재민 차관(국방부)  답변', 'wv': 0}, {'realTime': '11:36:02', 'playTime': '00:05:01', 'speakType': '질의', 'no': 486727, 'movieTitle': '이주영 위원(미래통합당)  질의 / 박재민 차관(국방부)  답변 / 왕정홍 청장(방위사업청)  답변', 'wv': 0}, {'realTime': '11:41:04', 'playTime': '00:00:37', 'speakType': '발언', 'no': 486728, 'movieTitle': '안규백 위원장(더불어민주당)  발언 / 박재민 차관(국방부)  발언', 'wv': 0}, {'realTime': '11:41:42', 'playTime': '00:01:16', 'speakType': '법안', 'no': 486729, 'movieTitle': '안규백 위원장(더불어민주당)  발언, 의사일정 제5할~제31항 상정', 'wv': 0}, {'realTime': '11:42:58', 'playTime': '00:01:18', 'speakType': '설명', 'no': 486730, 'movieTitle': '박재민 차관(국방부)  설명', 'wv': 0}, {'realTime': '11:44:17', 'playTime': '00:00:18', 'speakType': '발언', 'no': 486731, 'movieTitle': '안규백 위원장(더불어민주당)  발언', 'wv': 0}, {'realTime': '11:44:35', 'playTime': '00:02:36', 'speakType': '보고', 'no': 486732, 'movieTitle': '배용근 수석전문위원(국방위원회)  보고', 'wv': 0}, {'realTime': '11:47:11', 'playTime': '00:00:13', 'speakType': '발언', 'no': 486733, 'movieTitle': '안규백 위원장(더불어민주당)  발언', 'wv': 0}, {'realTime': '11:47:24', 'playTime': '00:01:38', 'speakType': '보고', 'no': 486734, 'movieTitle': '전문위원  보고', 'wv': 0}, {'realTime': '11:49:03', 'playTime': '00:01:37', 'speakType': '산회', 'no': 486735, 'movieTitle': '안규백 위원장(더불어민주당)  발언, 의사일정 제5항~제31항 의결, 산회', 'wv': 0}])]
```

<div align="center">

  <img src="https://raw.githubusercontent.com/anzhi0708/dearAJ/main/img/actual_kr_conf_site_page.png" />
  *A `Movie` contains multiple `Speak`s.*

</div>

### Speak

Info about some specific `MP`'s speech, such as `speak_type` etc. A `Movie` can hold multuple `Speak`s.

```python
>>> len(Conferences(20)[69].speaks)
35
```

`Conference`'s property `.pdf` is the PDF file raw bytes data. Use `open(output_file_path, "wb").write(conference.pdf)` to save PDF file.

### get_conferences_of

The crawler class. Use `get_conferences_of(nth, save=True)` to save JSON data to csv files.

## License

Copyright Anji Wong, 2022.

Distributed under the terms of the Apache 2.0 license.
