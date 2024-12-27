
import ollama
# Set the model name and the message input
model_name = "llama3.2:1b"  # Example, choose the model name as per your preference
command = """
you commands
"""

# Create a request to the Ollama model
response = ollama.chat(model=model_name, messages=[{"role": "user", "content": command}])

# Print the response
print(response['message']['content'])

