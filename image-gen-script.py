import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
import matplotlib.pyplot as plt
import os

torch.cuda.empty_cache()
model_id = "stabilityai/stable-diffusion-2-1"

pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
pipe.enable_attention_slicing()  # keeping this as it helps with memory
pipe = pipe.to("cuda")

prompt = "a shoe"  # you can modify this prompt as needed

# Generate image with higher resolution
image = pipe(
    prompt,
    num_inference_steps=50,    # default value, you can adjust if needed
    guidance_scale=7.5,        # keeping this as it helps with prompt adherence
    height=1000,
    width=1000
).images[0]

# Display the image
plt.figure(figsize=(10, 10))
plt.imshow(image)
plt.axis("off")
plt.show()

# Save the image
# Create assets directory if it doesn't exist
os.makedirs("assets", exist_ok=True)

# Save the image to assets folder
image.save(os.path.join("assets", "generated_image.png"))