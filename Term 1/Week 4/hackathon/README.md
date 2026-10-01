# Urban Heat — Make Room for Nature

A six-shot climate-awareness film about heat in paved Dutch neighbourhoods and the relief offered by shade and greenery. Two students move from an exposed public space to a shaded bench. The video clips were generated locally in ComfyUI using Wan 2.2.

**Assigned SDG:** 13 — Climate Action  
**Film:** 30.42 seconds · six shots · 1080 × 1080 · 30 fps final export  
**Team:** [ADD TEAM MEMBERS]  
**YouTube:** [ADD PUBLIC OR UNLISTED VIDEO URL]

[Watch/download the supplied MP4](video/urban-heat.mp4) · [Illustrated shot list](shotlist/Urban_Heat_Shot_List.pdf) · [Prompts and starting frames](shotlist/Urban_Heat_Shot_List.md)

## The issue

During hot summer weather, students walking and spending time outdoors in Dutch urban neighbourhoods can experience uncomfortable heat, especially in exposed paved spaces with little shade. Buildings and paving store heat, while the amount of vegetation, wind and urban form affect local conditions. Our film focuses on this everyday experience in a fictional Dutch residential neighbourhood. It does not document a specific heatwave or a measured street temperature.

The issue can be substantial: KNMI explains that city–countryside temperature differences can reach about 4°C for a city of 10,000 inhabitants and 7°C for one of 200,000 inhabitants. **These large differences occur during clear, calm nights**, not necessarily during the daytime scene shown in our film. We use this as background evidence for urban heat, not as a measured cooling effect between the two benches. [1]

The US Environmental Protection Agency explains that trees and vegetation can reduce heat through shade and evapotranspiration. The amount of cooling depends on the setting; the film makes no numerical claim about the temperature of its fictional locations. [2]

## Audience and placement

Our intended audience is **students aged approximately 18–25 who study or live in Dutch cities and walk between classes, public transport and home**. They may recognise hot streets but may not connect the comfort of outdoor spaces with shade, paving and greenery. This is a design assumption, not a finding from audience research.

The intended placement is **a student association's Instagram feed during warm weather**, using the square film format. The YouTube upload is the portfolio viewing copy. Short scenes, recognisable student characters and simple English narration are intended to make the message easy to follow without specialist knowledge.

The film is not aimed at professional urban planners who need quantified design evidence, or at people seeking personalised heat-health guidance. Its young, mobile protagonists do not represent everyone affected by heat, especially people who cannot easily move to a shaded space. English-only narration also limits accessibility; matching English captions should be added before publication.

## SDG 13 and the intended message

The film addresses **SDG 13: Climate Action**, particularly **target 13.3**, which includes education and awareness about climate adaptation and impact reduction. [3] Its concrete message is that shade and greenery matter for the experience of urban heat, and that making room for them is part of adapting public spaces to hotter conditions.

The intended takeaway is: **“Make room for nature in our streets.”** Students are the direct audience; residents could benefit if greater awareness contributes to support for greener public spaces. The film itself does not lower temperatures, prove behaviour change or replace wider climate mitigation and adaptation measures.

## What we built

The audience-facing product is a short film. The technical prototype is a ComfyUI image-to-video workflow: it takes a starting image, a positive motion prompt, a negative prompt and generation settings, then produces an animated clip. The six clips are assembled into a film in a separate editing step.

| Shot | Approx. time | Story and intended movement |
|---|---|---|
| 1 | 00–05 s | Two students walk toward the camera through a sunlit neighbourhood. |
| 2 | 05–10 s | Dry leaves move around a tree pit in a paved street. |
| 3 | 10–15 s | The students sit in direct sunlight; the woman fans herself and the man leans forward. |
| 4 | 15–20 s | They walk away from the exposed square toward a shaded path. |
| 5 | 20–25 s | Green leaves sway above a shaded path. |
| 6 | 25–30 s | The students sit together on a shaded bench and relax. |

The [detailed shot list](shotlist/Urban_Heat_Shot_List.md) contains the six starting images, positive and negative prompts, framing, narration and prompt-record notes. The time ranges above are approximate, not frame-accurate cut points.

### Where the AI tool contributes

1. **Load Image** supplies the shot's starting composition and characters.
2. **Load CLIP and CLIP Text Encode** turn the positive and negative prompts into conditioning for generation.
3. **Load Diffusion Model** loads Wan 2.2 TI2V 5B. **ModelSamplingSD3** supplies its sampling configuration.
4. **Wan22ImageToVideoLatent** prepares the video latent using the starting image, width, height and frame count.
5. **KSampler** generates the motion sequence using the model, prompts, seed and sampling settings.
6. **VAE Decode / VAE Decode (Tiled)** converts the sampled latents into visible frames. Tiled decoding was used during local iterations.
7. **Create Video and Save Video** encode and save the clip. The clips are then cut together and audio is added in the video editor.

ComfyUI performs the generative motion step. Without that step, this workflow would supply still images rather than the intended walking, fanning and leaf movement. Film assembly is a separate manual production step, not an automated part of the supplied graph.

## Workflow screenshots

These screenshots document the three ComfyUI setups used during development: still-image generation, background replacement and video generation. The settings below describe the visible configurations. Screenshots supplement the exported JSON files; they do not establish which settings produced every final shot.

### 1. Text-to-image generation with SDXL

![SDXL text-to-image workflow with positive and negative prompts, sampling, VAE decoding and image saving](assets/workflows/text-to-image.png)

The SDXL checkpoint loader supplies the model, text encoder and VAE. Positive and negative prompts condition the sampler, while an empty latent defines the image size. The sampler creates the latent image, the VAE decoder turns it into pixels, and the save node writes the result. The visible prompt describes two students sitting on a bench, viewed from behind.

| Setting | Visible value |
|---|---|
| Checkpoint | `sd_xl_base_1.0.safetensors` |
| Image size / batch | 1024 × 1024 / 1 |
| Seed / control after generation | `27092623` / fixed |
| Steps / CFG | 30 / 5.0 |
| Sampler / scheduler | `dpmpp_2m` / `karras` |
| Denoise | 1.00 |

### 2. Automatic masking and background replacement

![ComfyUI background-replacement workflow using automatic person masking, SDXL inpainting and compositing](assets/workflows/background-mask.png)

The input image feeds the **Select persons** node from `comfyui-inspyrenet-rembg`. Its mask is inverted to select the background. The masked-area encoder prepares that region for generation, and SDXL generates replacement content from the prompts. After decoding, **Keep pixels outside mask** composites the result with the original image to preserve the unmasked subject. The mask preview provides a way to inspect the selected region.

This screenshot shows a single male subject loaded into the workflow, while the positive prompt still describes two students. It records an intermediate setup rather than a confirmed final configuration for both characters.

| Setting | Visible value |
|---|---|
| Checkpoint | `sd_xl_base_1.0.safetensors` |
| Seed / control after generation | `27092711` / fixed |
| Steps / CFG | 30 / 5.0 |
| Sampler / scheduler | `dpmpp_2m` / `karras` |
| Denoise | 1.00 |
| Mask growth | 6 pixels |

### 3. Image-to-video generation with Wan 2.2

![Wan 2.2 image-to-video workflow with the shot 6 starting image, text conditioning, sampling, tiled VAE decoding and video output](assets/workflows/image-to-video.png)

The **Start image** node loads `startshot 6.png`. Wan 2.2 uses this image and the text conditioning to generate the sequence. The sampler output passes through **VAE Decode (Tiled)**, then **Create Video** and **Save Video** produce the clip.

The upper green text node is titled **Negative prompt**, but its connection runs to the sampler's **positive** input and its text describes the intended action. It therefore acts as the positive prompt. The lower text node connects to **negative**. Renaming the upper node to **Positive prompt** would make the graph easier to understand.

| Setting | Visible value |
|---|---|
| Diffusion model | `wan2.2_ti2v_5B_fp16.safetensors` |
| Text encoder | `umt5_xxl_fp8_e4m3fn_scaled.safetensors` |
| VAE | `wan2.2_vae.safetensors` |
| Resolution / frames / batch | 768 × 768 / 121 / 1 |
| Seed / control after generation | `27092619` / fixed |
| Steps / CFG | 30 / 4.0 |
| Sampler / scheduler | `uni_pc` / `simple` |
| Denoise / model sampling shift | 1.00 / 8.00 |
| VAE tile size / overlap | 512 / 64 |
| Temporal size / temporal overlap | 64 / 4 |
| Generated clip frame rate | 24 fps |

This provides a visible settings record for the displayed shot 6 setup. The Save Video controls are partly cropped, so the screenshot does not establish the output filename or encoding settings. The corresponding JSON export is still needed to preserve the complete graph.

## Why this approach fits the audience

A short visual story connects an abstract climate-adaptation topic to an everyday situation: walking through a neighbourhood and looking for a comfortable place to sit. Following the same two students makes the contrast between exposure and shade easy to recognise. The final scene offers a constructive message rather than relying on disaster imagery.

A poster could communicate the basic fact more simply and with less rendering effort. The film adds movement and a sequence of discomfort, movement toward shade and relief, which is the reason for choosing this format for a student social feed. We have not tested whether it persuades viewers more effectively than a poster; that remains an evaluation question.

## How to run the workflow

### Requirements

Use a local ComfyUI installation with native Wan 2.2 support and a compatible GPU setup. See the [official Wan 2.2 guide](https://docs.comfy.org/tutorials/video/wan/wan2_2) for installation and model details. [4] The model files are not bundled in this repository.

| Model | Location inside ComfyUI |
|---|---|
| `wan2.2_ti2v_5B_fp16.safetensors` | `models/diffusion_models/` |
| `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | `models/text_encoders/` |
| `wan2.2_vae.safetensors` | `models/vae/` |

### Generate a clip

1. Start ComfyUI locally and import the workflow JSON.
2. A previous [image-to-video reference workflow](workflows/reference/Urban_Heat_Duo_Shot1_Image_to_Video.json) is included. It uses ordinary VAE Decode and is **not an archived export of every successful final render**. For exact reproduction, add the successful final workflow exports from the production laptop.
3. Select the three model files in their loader nodes.
4. Upload the corresponding `shotlist/images/shot-01.png` through `shot-06.png` into **Load Image**.
5. Copy that shot's positive and negative prompts from the shot list into the text-encoding nodes.
6. Set the shot's saved seed and generation settings. The shared working settings are listed below, but they do not replace the missing per-shot final records.
7. Click **Run**. The reference workflow saves clips under `ComfyUI/output/UrbanHeat/`.
8. Review the output, then save the successful workflow JSON with its seed. Repeat for the remaining shots.
9. Arrange the clips in shot order in the video editor, add the recorded narration and any licensed audio, and export the film. The supplied final edit is square 1080 × 1080 at 30 fps; the working generation setup used 24 fps.

### Working settings and reproduction limits

| Setting | Recorded working value |
|---|---|
| Resolution | 768 × 768 |
| Frame count / generation rate | 121 frames / 24 fps (about 5.04 seconds) |
| Batch size | 1 |
| Steps / CFG | 30 / 4 |
| Sampler / scheduler | `uni_pc` / `simple` |
| Denoise / model sampling shift | 1.0 / 8 |
| Seed | Shot 1 source clip: `27092613`; displayed shot 6 setup: `27092619`; other final seeds still need confirmation |
| Tiled VAE settings | Displayed shot 6 setup: tile 512, overlap 64, temporal size 64, temporal overlap 4; confirm the remaining shots |

A matching seed alone is insufficient to reproduce a shot: the input image, prompt, models, graph and settings must also match. Record the ComfyUI version, any custom-node versions and the GPU environment. The reference JSON has been inspected, but it has not been executed in this documentation environment. Exact reproduction of the final six shots is not yet verified.

## Voiceover and audio

The proposed English narration is divided across shots:

1. “On a hot summer day, city streets can feel overwhelming.”
2. “Brick and pavement absorb the sun's heat.”
3. “With little shade, even sitting down offers no relief.”
4. “But a few steps can make a difference.”
5. “Trees shade our streets, and plants help cool the air.”
6. “As our cities get hotter, let's make room for nature.”

Record the narration with a team member's own voice. The assignment also permits ComfyUI-generated sound and royalty-free music, but excludes third-party AI voice tools. The supplied MP4 has an audio stream; its contents and licensing have not been verified for this documentation.

**Complete the audio record before submission:**

- Narration performer and recording method: [ADD]
- Music/sound effect title, creator, source URL and licence, or “none”: [ADD]
- Confirmation that this record matches the final uploaded film: [ADD]

## Ethical reflection

The realistic AI imagery could be mistaken for evidence of a real Dutch heatwave. The neighbourhood and characters are fictional; the film is an illustration, not a measurement or documentary record. We reduce misleading specificity by avoiding named locations and numerical temperature claims in the story. Dry leaves are a visual storytelling cue, not proof of climate change, and the film should not imply that one shaded bench solves urban heat. No real person was intentionally portrayed; generated faces should still be checked for unintended resemblance. Before publication, add a readable disclosure inside the film, such as **“AI-generated fictional scene — illustrating urban heat”**, and matching captions; these additions have not been verified in the supplied export. Multiple iterations consumed GPU time, including a reported render of about an hour. We have not measured energy use or completed a generation count, so we cannot claim a low environmental footprint. Reusing accepted inputs and stopping unnecessary rerenders can reduce further computation. The film's educational benefit remains an intention, not a measured outcome.

**Generation record to complete:** [NUMBER OF STILL-IMAGE GENERATIONS] still generations; [NUMBER OF VIDEO GENERATIONS] video generations, including rejected attempts; [APPROXIMATE TOTAL GPU RUNTIME] with the estimation method. If logs are incomplete, label estimates explicitly.

## What we learned

Consistent characters required stable reference images, clothing and hairstyles. Motion prompts worked better when they named a small number of visible actions rather than only describing the scene. Seeds changed the result, while memory use and VAE decoding settings affected the practical rendering process. Blurred faces, distorted textures and static-looking outputs required visual review. Saving the successful graph and settings matters as much as saving the finished clip.

## Submission status

The film, six starting images, illustrated shot list and a previous reference workflow are included in the portfolio package. This README also includes three workflow screenshots. Presentation slides have been prepared separately. This is not yet a complete reproduction archive. Add the successful final workflow exports, remaining settings, YouTube link, audio record, generation count before submission, and upload the prepared presentation slides. Read [RUBRIC_CHECK.md](RUBRIC_CHECK.md) for the evidence-based assessment and the separate assignment-specific compliance issue.

## Sources

1. [KNMI — Stadsklimaat](https://www.knmi.nl/kennis-en-datacentrum/uitleg/stadsklimaat). Dutch urban-heat context and the conditions behind the cited temperature differences.
2. [US EPA — Benefits of Trees and Vegetation](https://www.epa.gov/heatislands/benefits-trees-and-vegetation). Shade and evapotranspiration as cooling mechanisms.
3. [United Nations — Sustainable Development Goal 13](https://sdgs.un.org/goals/goal13). Target 13.3 on climate education, awareness and adaptation.
4. [ComfyUI — Wan 2.2 Native Workflow](https://docs.comfy.org/tutorials/video/wan/wan2_2). Native workflow and model locations.

Sources checked on 1 October 2026.
