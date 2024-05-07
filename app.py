import moviepy.editor as mp
import speech_recognition as sr

# 動画ファイルのパス
video_path = "filefolder/Download.mp4"

# 動画から音声を抽出
clip = mp.VideoFileClip(video_path)
clip.audio.write_audiofile("filefolder/temp_audio.wav")

# 音声認識を初期化
recognizer = sr.Recognizer()

# 音声ファイルを読み込む
with sr.AudioFile("filefolder/temp_audio.wav") as source:
    audio_data = recognizer.record(source)

# 音声をテキストに変換
text = recognizer.recognize_google(audio_data, language="ja-JP")

# テキストを出力
print(text)

# 必要であれば、テキストをファイルに保存することもできます
with open("filefolder/transcript.txt", "w") as file:
    file.write(text)
