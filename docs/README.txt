# THE SAIVT-BNEWS DATABASE #

This distribution contains the SAIVT-BNEWS database, consisting of
ground truth information and metadata for a selection of 55 Australian
broadcast news videos that need to be downloaded separately.

Further information on the SAIVT-BNEWS database is available in our
paper:

> Ghaemmaghami, H., Dean, D., & Sridharan, S (2013) Speaker
> attribution of Australian broadcast news data, In "Proceedings of
> the First Workshop on Speech, Language and Audio in Multimedia
> (SLAM)", CEUR Workshop Proceeedings, Volume 1012, Sun SITE Central
> Europe, Marseille, France, pp 72-77, available at
> https://wiki.qut.edu.au/display/saivt/SAIVT-BNEWS.

This paper is also available alongside this document in the file
`Ghaemmaghami2013, Speaker Attribution of Australian Broadcast News
Data.pdf`.

The SAIVT-BNEWS ground truth information and associated metadata is
licensed CC-BY-SA, and the 55 Australian broadcast news videos
(downloaded separately, instructions below) are copyright All Rights
Reserved by Fairfax Media.

To attribute this database, please include the following citation:

> Ghaemmaghami, H., Dean, D., & Sridharan, S (2013) Speaker
> attribution of Australian broadcast news data, In "Proceedings of
> the First Workshop on Speech, Language and Audio in Multimedia
> (SLAM)", CEUR Workshop Proceeedings, Volume 1012, Sun SITE Central
> Europe, Marseille, France, pp 72-77, available at
> https://wiki.qut.edu.au/display/saivt/SAIVT-BNEWS.

## INSTALLATION ##

Download and unzip `SAIVT-BNEWS.zip` from
https://wiki.qut.edu.au/display/saivt/SAIVT-BNEWS or clone the
repository:

```git clone https://github.com/qutsaivt/SAIVT-BNEWS.git```

You should have the following folder structure:

    SAIVT-BNEWS
      +-- The_Sydney_Morning_Herald_MRSS_Feed
      |      +-- <videoid>                      (for each video)
      |      |      +-- <videoid>*.txt          (video metadata)
      |	 	 +-- <videoid>*.diarref.lab   (speech and speaker
      |		 |                             ground truth)
      |		 +-- <videoid>*.faceref.lab   (face timing ground truth)
      |      |     +-- <videoid>*.facepositions (face position ground truth)
      |		 +-- <videoid>*.ocrref.lab    (ocr ground truth)
      |
      +-- code       (python script to help download videos)
      +-- docs       (this file and the publication)

At this point, you have the SAIVT-BNEWS ground truth information and
associated meta data. To download the associated videos, continue to
follow these instructions:

The videos can be downloaded using the information in the
`<videoid>*.txt` files on the lines starting with `media_content:`, and
a python script is provided in the code folder to automate this
process. Simply run `python code/downloadvids.py` to do so.

The videos will be downloaded into the appropriate
`SAIVT-BNEWS/The_Sydney_Morning_Herald_MRSS_Feed/<videoid>` folders.

If you aren't using the python script to download the videos,
please ensure that only one files is downloaded at a time, and
pause briefly between videos to ensure that the media provided
doesn't blacklist your IP adress.

## DATA DESCRIPTION ##

### Video Metadata ### 

Contains information about the video, including title, a short
summary, a link to the video's web page (`link`), as well as a link to
the video itself (`media_content`), and the id.

This file has one line per each field, with the field name and the
value separated by a ':'

*Example (3123523_high.mp4.txt)*

    updated: Wed, 14 March 2012 09:47:50
    title: Carr crashes into Senate
    summary: After being officially sworn into the Senate, former premier Bob Carr unleashed on the Opposition.
    link: http://media.smh.com.au/news/national-news/carr-crashes-into-senate-3123523.html
    media_content: http://mediadownload2.f2.com.au/flash/media/2012/03/13/3123523/3123523_high.mp4
    id: 3123523

### Diarisation Ground Truth ###

Contains information about the speakers appearing on the audio track
of the video, as well as a transcription of their speech.

Each line has the start and end time of the speech (in seconds)
followed by a database-level unique speaker identity and finally the
speech transcription.

There may be comments, that should be ignored, indicated by a `#` in
the first column, and a commented header to indicate the overall
length of the video (in seconds).

*Example (3123523.diarref.lab)*

    #length=100.14
    3.444518        10.693765       paul_bongiorno BACK INTO THE FRAY BOB CARR SWORN IN AS SENATOR SO HE CAN FULFIL A LONG TIME DREAM TO BECOME FOREIGN MINISTER
    10.693765       12.922571       bob_carr I WILL BE FAITHFUL A BE A TRUE ALLEGIANCE
    13.035137       17.312643       paul_bongiorno THE BIPARTISAN WELCOME WON'T DETER HIM FROM BEING A GOVERNMENT BOMB THROWER
    17.312643       18.618408       bob_carr TONY ABBOTT IS LIKE THE
    ... continues ...

### Face Ground Truth ###

Contains information about the faces appearing in the video. Only
faces judged to be sufficiently prominent and frontal are labelled
at this stage.

Each line has the start and end time of the face appearance (in
seconds) followed by a database-level unique speaker
identity. Identity labels are shared between faces and speakers if
they are the same person.

There may be comments, that should be ignored, indicated by a `#` in
the first column, and a commented header to indicate the overall
length of the video (in seconds).

*Example (3123523.faceref.lab)*

    #length=100.14
    2.96    6.64    bob_carr
    10.92   14.2    bob_carr
    14.2    15.36   bob_carr
    ... continues ..

While this file indicates the timing information of the faces in the
videos, it does not contain the actual locations of the faces in the
video. That information is in the matching `<faceid>*.facepositions`
file, where each line has the time, the faceid, and the top, left,
height and width of the face, collected around 2.5 times per second
(or every 10 frames) whenever a face is visible.

*Example (3123523.facepositions)*

    #time   id      top     left    height  width
    2.96    bob_carr        74      526     76      64
    3.36    bob_carr        100     508     70      60
    3.76    bob_carr        92      526     72      62
    4.16    bob_carr        68      500     70      62
    ... continues ...

### OCR Ground Truth ###

Contains information about the on-screen text appearing in the
video. Only text appearing in the lower third of the video is
considered.

Each line has the start and end time of the text appearance (in
seconds) followed by a video-level unique ocr identity. The identity
is designed to indicate when different lines of text appear in the
same area within the video.

There may be comments, that should be ignored, indicated by a `#` in
the first column, and a commented header to indicate the overall
length of the video (in seconds).

At this stage the ocr reference does not indicate the location of
the ocr text. This may be provided in the future, and/or QUT would
be happy to incorporate this information back into the ground truth
if it is produced by other researchers.

*Example (3123523.ocrref.lab)*

    #length=100.14
    5.3 7.7 OCR_1 PAUL BONGIORNO
    5.3 7.7 OCR_1 NATIONAL AFFAIRS EDITOR
    19.1 21.6 OCR_2 BOB CARR
    19.1 21.6 OCR_2 FOREIGN MINISTER
    ... continues ..



