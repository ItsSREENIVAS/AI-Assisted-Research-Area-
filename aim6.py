
import os
from google import genai

# 1. Connect to Gemini API
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("API key not found. Set GEMINI_API_KEY first.")
    raise SystemExit

client = genai.Client(api_key=api_key)

print("\n===== AI RESEARCH ASSISTANT =====\n")

# 2. Get research information
subject_domain = input("Enter Subject Domain: ")
keywords = input("Enter Research Keywords: ")
research_interest = input("Enter Your Research Interest: ")

# 3. Prepare the prompt
prompt = f"""
Act as an academic research assistant.

Based on the following information:

Subject Domain: {subject_domain}
Keywords: {keywords}
Research Interest: {research_interest}

Generate a structured academic research plan.

Include all six sections:

1. POSSIBLE RESEARCH AREAS
Suggest five relevant research areas.

2. INTERDISCIPLINARY RESEARCH TOPICS
Suggest four topics connecting different disciplines.

3. RESEARCH OBJECTIVES
Provide three clear objectives.

4. PRELIMINARY RESEARCH OUTLINE
Include title, background, research problem and research questions.

5. SUGGESTED RESEARCH METHODOLOGY
Include research type, data collection, target group and analysis method.

6. EXPECTED OUTCOMES
Provide three possible outcomes.

Use clear academic English.
Make every section relevant to the given research interest.
Avoid repeating sentences.
"""

# 4. Generate the response using Gemini
print("\nGenerating research suggestions...\n")

try:
    response = client.interactions.create(
        model="gemini-3.8-flash",
        input=prompt
    )

    # 5. Display generated output
    print("\n===== GENERATED RESEARCH OUTPUT =====\n")
    print(response.output_text)
    print("\n===== END OF OUTPUT =====")

except Exception as error:
    print("Error generating response:", error)
