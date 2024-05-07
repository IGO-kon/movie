import os
import glob
import moviepy.editor as mp
import speech_recognition as sr

# 動画ファイルが含まれるフォルダのパス
folder_path = "filefolder/"

# フォルダ内のすべての動画ファイルに対して処理を行う
for video_file in glob.glob(os.path.join(folder_path, "*.mp4")):
    # 動画から音声を抽出
    clip = mp.VideoFileClip(video_file)
    audio_file = os.path.splitext(video_file)[0] + ".wav"
    clip.audio.write_audiofile(audio_file)

    # 音声認識を初期化
    recognizer = sr.Recognizer()

    # 音声ファイルを読み込む
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)

    # 音声をテキストに変換
    text = recognizer.recognize_google(audio_data, language="ja-JP")

    # テキスト内のピリオド、疑問符、感嘆符で改行を挿入
    text_with_line_breaks = ""
    for char in text:
        text_with_line_breaks += char
        if char in ['。', '？', '！']:
            text_with_line_breaks += '\n'

    # テキストを出力
    print(text_with_line_breaks)

    # 必要であれば、テキストをファイルに保存することもできます
    transcript_file = os.path.splitext(video_file)[0] + ".txt"
    with open(transcript_file, "w") as file:
        file.write(text_with_line_breaks)
