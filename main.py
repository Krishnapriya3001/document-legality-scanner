from scanner import extract_text, check_document

image_path = "sample_docsagreement.jpg"

text = extract_text(image_path)

keywords = check_document(text)

print("Keywords detected:", keywords)

if len(keywords) >= 2:
    print("Result: Document appears VALID")
else:
    print("Result: Document may be SUSPICIOUS")