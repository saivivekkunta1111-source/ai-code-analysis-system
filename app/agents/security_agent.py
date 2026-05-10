def security_analysis(model, code_content):

    prompt = f"""
Analyze this codebase for security issues.

Generate:

1. Hardcoded Secrets
2. Authentication Risks
3. API Security
4. Input Validation Problems
5. Recommendations

Codebase:
{code_content[:15000]}
"""

    response = model.generate_content(prompt)

    return response.text