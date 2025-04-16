from diffusers import StableDiffusionPipeline
import torch

# 本地SD模型（需GPU）
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16
).to("cuda")

def generate_mv_image(prompt: str, style: str) -> str:
    enhanced_prompt = f"{prompt}, {style}, MV style, vibrant colors"
    image = pipe(enhanced_prompt).images[0]
    image_path = "mv_frame.png"
    image.save(image_path)
    return image_path

image_tool = Tool(
    name="MVImageGenerator",
    func=generate_mv_image,
    description="根据提示词和风格生成MV图片，输入格式：'内容描述, 风格关键词'"
)