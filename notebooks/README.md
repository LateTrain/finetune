# Trinity Finetuning Notebooks (Phase 2)

Experiments in finetuning "Trinity," the cyber-defense assistant, using three
different LoRA-based approaches on the same small starter dataset. This is a
learning exercise, not a production training pipeline.

## Shared dataset

[`data/cyber_defense_qa.jsonl`](data/cyber_defense_qa.jsonl) — ~20
instruction/response pairs covering threat detection, incident response,
secure coding, and system hardening. Small and illustrative only; real
finetuning would need a much larger, more diverse dataset.

## Approaches

| Folder | Tool | Style | Notes |
|---|---|---|---|
| [`unsloth/`](unsloth/unsloth_finetune.ipynb) | [Unsloth](https://github.com/unslothai/unsloth) | Fast, memory-efficient, beginner-friendly | Best starting point; also shows GGUF export back to Ollama |
| [`peft_trl/`](peft_trl/peft_trl_finetune.ipynb) | Plain `transformers` + `peft` + `trl` | Explicit, step-by-step | Good for understanding the fundamentals Unsloth optimizes |
| [`axolotl/`](axolotl/axolotl_finetune.ipynb) | [Axolotl](https://github.com/axolotl-ai-cloud/axolotl) | Config-driven (YAML) | Best for quickly comparing many runs by editing config, not code |

All three finetune a small Llama 3.2 3B model with LoRA on the same dataset,
using the same Trinity system prompt, so outputs can be compared across
approaches.

## Running in Google Colab

This project's development Mac has no CUDA GPU, so these notebooks are
designed to run in [Google Colab](https://colab.research.google.com/) with a
GPU runtime (Runtime → Change runtime type → T4 GPU or better):

1. Upload the notebook (e.g. `unsloth_finetune.ipynb`) to Colab.
2. Upload `data/cyber_defense_qa.jsonl` (and `axolotl_config.yaml` for the
   Axolotl notebook) into the Colab session's working directory.
3. Run the cells top to bottom.

The `meta-llama/Llama-3.2-3B-Instruct` model used by the PEFT/TRL and Axolotl
notebooks is gated on Hugging Face — accept the license on the model page and
run `huggingface-cli login` (or set the `HF_TOKEN` secret in Colab) first.
The Unsloth notebook uses `unsloth/Llama-3.2-3B-Instruct`, a re-upload that
isn't gated.

## Limitations

These notebooks have been reviewed for structural/syntax correctness but not
executed end-to-end, since real training requires a CUDA GPU not available on
this development machine.
