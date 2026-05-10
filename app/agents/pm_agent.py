def pm_documentation(model, code_content):

    prompt = f"""
You are a Product Manager.

Generate:

1. Business Overview
2. User Flow
3. Features
4. Business Value
5. Risks
6. Future Improvements

Codebase:
{code_content[:15000]}
"""

    response = model.generate_content(prompt)

    return response.text