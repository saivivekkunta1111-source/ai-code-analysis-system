def architecture_analysis(model, code_content):

    prompt = f"""
You are a Senior Software Architect.

Analyze this codebase and generate a COMPLETE architecture report.

Generate the following sections:

1. System Design
2. Folder Structure
3. Component Relationships
4. Scalability Suggestions
5. Deployment Suggestions
6. Microservices Possibilities
7. Database Suggestions
8. Observability Recommendations
9. Mermaid Diagrams

IMPORTANT:
Include Mermaid diagrams for:
- system architecture
- application flowchart
- dependency graph

Generate VALID Mermaid syntax.

Example Mermaid format:

graph TD
    A[Client] --> B[FastAPI Backend]
    B --> C[AI Agents]
    C --> D[Gemini API]

Also explain:
- how components communicate
- request flow
- backend architecture
- scalability improvements
- production deployment ideas

Codebase:
{code_content[:15000]}
"""

    response = model.generate_content(prompt)

    return response.text