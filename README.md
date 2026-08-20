# finetune

A learning project for exploring LLM finetuning techniques. Phase 1 is a
locally-hosted chatbot via [Ollama](https://ollama.com) with a custom
Modelfile, and a minimal FastAPI-based web chat UI with streaming responses.

Later phases will explore finetuning with Unsloth, Axolotl, and PEFT/TRL,
using notebooks (locally and on Google Colab for GPU access).

## Setup

1. Install [Ollama](https://ollama.com) and pull the base model:
   ```sh
   ollama pull llama3.2
   ```
2. Build the custom model from the Modelfile:
   ```sh
   ollama create finetune-poc -f ollama/Modelfile
   ```
3. Create and activate the conda environment:
   ```sh
   conda env create -f environment.yml
   conda activate finetune-poc
   ```
4. Run the web server:
   ```sh
   uvicorn app.main:app --reload
   ```
5. Open http://localhost:8000 in a browser and start chatting.

## Finetuning experiments (Phase 2)

See [notebooks/](notebooks/README.md) for LoRA finetuning experiments on
Trinity using Unsloth, plain PEFT/TRL, and Axolotl, designed to run in Google
Colab (GPU required).
