from moviepy.editor import ImageClip, AudioFileClip
from langchain.tools import Tool

def create_mv(audio_path: str, image_path: str, duration: float) -> str:
    # 创建视频片段
    clip = ImageClip(image_path).set_duration(duration)
    audio = AudioFileClip(audio_path)
    final_clip = clip.set_audio(audio)
    
    # 输出视频
    output_path = "output_mv.mp4"
    final_clip.write_videofile(output_path, fps=24)
    return output_path

video_tool = Tool(
    name="MVCreator",
    func=create_mv,
    description="合成音频和图片为MV，输入：音频路径、图片路径、时长"
)