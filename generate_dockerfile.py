import ollama

PROMPT = """
ONLY Generate an ideal dockerfile for {language} with best practices. Do not provide any description.
Include: 
- Base image
- Installation of dependencies
- setting working directory
- adding source code
- running the application 
- multi stage distroless docker image
"""
def generate_dockerfile(language):
    response = ollama.chat(model="llama3.2:1b",messages = [{"role": "user", "content": PROMPT.format(language=language)}])
    return response["message"]["content"]
if __name__ == "__main__":
    language = input("Enter the language you want to use: ")
    dockerfile = generate_dockerfile(language)
    print("\nGenerate Dockerfile:\n")
    print(dockerfile)