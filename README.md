# KSampler Config Node

A centralized configuration node for ComfyUI. Set your sampler parameters once
and feed them to every KSampler in the workflow. Designed for workflows where you
switch between model types.
## Installation

Copy the `ksampler_config_node` folder into:

```
ComfyUI/custom_nodes/ksampler_config_node/
```

Restart ComfyUI. The node appears under **sampling/custom** as **KSampler Config**.

---

## Outputs

| Output        | Type   | Notes                                                                 |
|---------------|--------|-----------------------------------------------------------------------|
| `steps`       | INT    | Number of denoising steps                                             |
| `cfg`         | FLOAT  | Classifier-Free Guidance scale                                        |
| `sampler_name`| COMBO  | Sampling algorithm (e.g. euler, dpmpp_2m)                             |
| `scheduler`   | COMBO  | Noise schedule (e.g. simple,karras, sgm_uniform)                             |
| `denoise`     | FLOAT  | Denoising strength (1.0 for txt2img, lower for img2img)               |
