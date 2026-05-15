import comfy.samplers


class KSamplerConfig:
    """
    Centralized KSampler configuration node.

    Place one of these in your workflow and connect its outputs to every KSampler node.
    When you switch models (e.g. standard -> Turbo/Lightning/Distilled), you only
    need to update settings here.

    HOW TO CONNECT TO EXISTING KSAMPLER NODES:
    Right-click any KSampler node and choose:
      - "Convert steps to input"
      - "Convert cfg to input"
      - "Convert sampler_name to input"
      - "Convert scheduler to input"
      - "Convert denoise to input"
    Then connect the matching outputs from this node.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "steps": (
                    "INT",
                    {
                        "default": 20,
                        "min": 1,
                        "max": 150,
                        "step": 1,
                        "tooltip": "Number of denoising steps. Distilled models (Turbo, Lightning) typically use 1-8.",
                    },
                ),
                "cfg": (
                    "FLOAT",
                    {
                        "default": 7.0,
                        "min": 0.0,
                        "max": 30.0,
                        "step": 0.1,
                        "tooltip": "Classifier-Free Guidance scale. Distilled models often need 1.0-2.0.",
                    },
                ),
                "sampler_name": (
                    comfy.samplers.KSampler.SAMPLERS,
                    {
                        "tooltip": "Sampling algorithm. euler_a or dpm++ are common. Check your model's recommended sampler.",
                    },
                ),
                "scheduler": (
                    comfy.samplers.KSampler.SCHEDULERS,
                    {
                        "tooltip": "Noise schedule. Lightning models often use sgm_uniform. Turbo uses simple or karras.",
                    },
                ),
                "denoise": (
                    "FLOAT",
                    {
                        "default": 1.0,
                        "min": 0.0,
                        "max": 1.0,
                        "step": 0.01,
                        "tooltip": (
                            "Denoising strength. "
                            "1.0 = full txt2img. "
                            "Lower values preserve more of the input latent (img2img). "
                            "Distilled/Turbo models REQUIRE 1.0 for txt2img."
                        ),
                    },
                ),
            }
        }

    # sampler_name and scheduler use "*" (wildcard) instead of the SAMPLERS/SCHEDULERS
    # list objects. This avoids a load-order bug: if any custom node replaces
    # comfy.samplers.KSampler.SCHEDULERS with a new list (e.g. to add "beta57"),
    # our RETURN_TYPES would hold a stale snapshot of the old list while other nodes
    # read the new one. ComfyUI compares the lists, finds them different, and raises
    # "Return type mismatch". Using "*" sidesteps the comparison entirely.
    # The values passed are still valid strings selected from our own dropdowns.
    RETURN_TYPES = (
        "INT",
        "FLOAT",
        "*",
        "*",
        "FLOAT",
    )
    RETURN_NAMES = ("steps", "cfg", "sampler_name", "scheduler", "denoise")
    OUTPUT_TOOLTIPS = (
        "Connect to KSampler > steps (after Convert to input)",
        "Connect to KSampler > cfg (after Convert to input)",
        "Connect to KSampler > sampler_name (after Convert to input)",
        "Connect to KSampler > scheduler (after Convert to input)",
        "Connect to KSampler > denoise (after Convert to input)",
    )

    FUNCTION = "get_config"
    CATEGORY = "sampling/custom"

    def get_config(self, steps, cfg, sampler_name, scheduler, denoise):
        return (steps, cfg, sampler_name, scheduler, denoise)


# --------------------------------------------------------------------------- #
# Registration
# --------------------------------------------------------------------------- #

NODE_CLASS_MAPPINGS = {
    "KSamplerConfig": KSamplerConfig,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "KSamplerConfig": "KSampler Config",
}
