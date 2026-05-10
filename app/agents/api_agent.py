def api_analysis(model, code_content):

    prompt = f"""
    Analyze all APIs in this project.

    Give:
    1. API Endpoints
    2. Request Methods
    3. Request/Response Details
    4. Security Risks
    5. API Improvements

    Code:
    {code_content[:15000]}
    """

    response = model.generate_content(prompt)

    return response.text