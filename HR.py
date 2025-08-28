import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader
import re

# ---- Resume Reader ----
def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text

# ---- Keyword Analyzer ----
def analyze_resume(text):
    skills = ["python", "excel", "sql", "power bi", "tableau", "machine learning",
              "data analysis", "c#", "asp.net", "communication", "leadership"]

    found_skills = [skill for skill in skills if re.search(skill, text.lower())]
    score = (len(found_skills) / len(skills)) * 100

    return found_skills, round(score, 2)

# ---- Question Generator ----
def generate_questions(skills):
    questions = []
    for skill in skills:
        if skill == "python":
            questions.append("Can you explain how you used Python in your projects?")
        elif skill == "sql":
            questions.append("What types of SQL queries have you written in real projects?")
        elif skill == "excel":
            questions.append("Which advanced Excel functions are you comfortable with?")
        elif skill == "power bi":
            questions.append("Can you explain a dashboard you built in Power BI?")
        elif skill == "machine learning":
            questions.append("Which ML algorithms have you implemented and where?")
        elif skill == "c#":
            questions.append("Tell me about your experience with C# and .NET applications.")
        elif skill == "asp.net":
            questions.append("Have you built any web applications in ASP.NET?")
        elif skill == "communication":
            questions.append("How do you communicate technical findings to non-technical stakeholders?")
        elif skill == "leadership":
            questions.append("Can you share an example of when you led a project or team?")
    return questions

# ---- Main Program ----
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select Resume PDF",
    filetypes=[("PDF files", "*.pdf")]
)

if file_path:
    print("\n📄 Reading Resume...")
    resume_text = extract_text_from_pdf(file_path)

    skills, score = analyze_resume(resume_text)

    print("\n✅ Resume Analysis Complete")
    print(f"Performance Score: {score}%")
    print(f"Detected Skills: {', '.join(skills) if skills else 'No major skills detected'}")

    print("\n💡 Suggested Interview Questions:")
    for q in generate_questions(skills):
        print(f"- {q}")

else:
    print("⚠️ No file selected.")
