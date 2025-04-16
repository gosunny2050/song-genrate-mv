from langchain.tools import Tool
import whisper

def analyze_audio(audio_path: str) -> dict:
    """提取歌词和情感风格"""
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    
    # 用LLM分析情感（示例简化）
    from langchain.llms import OpenAI
    llm = OpenAI(temperature=0.7)
    style = llm(f"用3个关键词描述以下文本的风格:\n{result['text']}")
    
    return {
        "lyrics": result["text"],
        "style": style.strip(),
        "duration": result["segments"][-1]["end"]  # 音频时长
    }

audio_tool = Tool(
    name="AudioAnalyzer",
    func=analyze_audio,
    description="输入音频路径，输出歌词、风格关键词和时长"
)