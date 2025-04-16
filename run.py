from langchain.agents import initialize_agent
from langchain.llms import OpenAI
from tools.audio_tool import audio_tool  # 显式导入音频工具
from tools.image_tool import image_tool  # 显式导入图片工具
from tools.video_tool import video_tool  # 显式导入视频工具

# 组合工具列表
tools = [audio_tool, image_tool, video_tool]

# 初始化Agent
agent = initialize_agent(
    tools,
    OpenAI(temperature=0.7, model="gpt-4"),
    agent="structured-chat-zero-shot-react-description",
    verbose=True
)

# 执行任务
result = agent.run("为音频love_song.mp3生成MV配图视频")
print(f"生成的MV路径: {result}")

tools = [audio_tool, image_tool, video_tool]
agent = initialize_agent(
    tools,
    OpenAI(temperature=0.7, model="gpt-4"),
    agent="structured-chat-zero-shot-react-description",
    verbose=True
)

# 执行任务
result = agent.run("为音频love_song.mp3生成MV配图视频")
print(f"生成的MV路径: {result}")