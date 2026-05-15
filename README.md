# KSampler Config Node

A centralized configuration node for ComfyUI. Set your sampler parameters once
and feed them to every KSampler in the workflow. Designed for workflows where you
switch between model types (standard SDXL, Turbo, Lightning, Distilled, etc.).

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
| `scheduler`   | COMBO  | Noise schedule (e.g. karras, sgm_uniform)                             |
| `denoise`     | FLOAT  | Denoising strength (1.0 for txt2img, lower for img2img)               |

---

## Connecting to existing KSampler nodes

ComfyUI's built-in KSampler does not expose all inputs as connectable sockets by default.
You need to convert each input manually:

1. Right-click your KSampler node.
2. Select **"Convert steps to input"** -> connect to `steps` output.
3. Select **"Convert cfg to input"** -> connect to `cfg` output.
4. Select **"Convert sampler_name to input"** -> connect to `sampler_name` output.
5. Select **"Convert scheduler to input"** -> connect to `scheduler` output.
6. Select **"Convert denoise to input"** -> connect to `denoise` output.

Repeat for every KSampler in the workflow. From then on, one change in the
KSampler Config node propagates everywhere.

---

## Recommended settings by model type

| Model type          | steps  | cfg       | sampler        | scheduler    | denoise |
|---------------------|--------|-----------|----------------|--------------|---------|
| Standard SDXL       | 20-30  | 5.0-7.5   | dpmpp_2m       | karras       | 1.0     |
| SDXL Turbo          | 1-4    | 1.0       | euler_a        | simple       | 1.0     |
| SDXL Lightning 4-step | 4    | 1.0-1.5   | euler          | sgm_uniform  | 1.0     |
| SDXL Lightning 8-step | 8    | 1.5-2.0   | euler          | sgm_uniform  | 1.0     |
| SD 1.5 standard     | 20-30  | 7.0       | euler_a        | karras       | 1.0     |
| Hyper-SD (SDXL)     | 4-8    | 1.0-2.0   | dpmpp_sde      | karras       | 1.0     |

These are starting points. Always check the model card for the author's recommendations.

---

## Planned: switch/preset system

If you plan to add a model-type selector (a dropdown like "Standard / Turbo / Lightning"
that auto-fills the values), the node will need an additional `mode` input and conditional
logic in `get_config`. This is a natural next step for this node.
