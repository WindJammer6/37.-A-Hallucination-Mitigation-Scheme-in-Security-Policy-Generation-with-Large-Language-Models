from openai import OpenAI

client = OpenAI(api_key="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")

def list_available_models():
    """List all available models using OpenAI API"""
    try:
        models = client.models.list()
        available_models = [model.id for model in models.data]
        return sorted(available_models)
    except Exception as e:
        print(f"Error fetching models: {e}")
        return []

# Usage
print("Available models:")
models = list_available_models()
for model in models:
    print(f"  - {model}")