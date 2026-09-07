from pypdf import PdfReader
import re


def read_pdf():
    reader = PdfReader("ml.pdf")

    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text


def search_pdf(question):
    text = read_pdf()

    # Split the complete PDF into smaller sections
    sections = text.split("\n")

    # Get words from the user's question
    question_words = re.findall(r"[a-zA-Z]+", question.lower())

    # Common words that do not help much in searching
    stop_words = {
        "what", "is", "are", "the", "a", "an", "of", "in",
        "to", "for", "about", "tell", "me", "explain",
        "please", "can", "you", "do", "know", "does",
        "how", "and", "or", "on", "with"
    }

    important_words = []

    for word in question_words:
        if word not in stop_words and len(word) > 2:
            important_words.append(word)

    results = []

    # Search every section of the PDF
    for section in sections:
        section = section.strip()

        if section == "":
            continue

        section_words = re.findall(r"[a-zA-Z]+", section.lower())

        score = 0

        for word in important_words:
            if word in section_words:
                score += 1

        if score > 0:
            results.append((score, section))

    # Put the most relevant sections first
    results.sort(reverse=True)

    if len(results) == 0:
        return None

    answer = ""

    # Return the best 3 matching sections
    for score, section in results[:3]:
        answer += section + "\n\n"

    return answer.strip()