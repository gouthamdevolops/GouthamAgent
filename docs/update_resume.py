import fitz
import os

def main():
    # 1. Open the PDF
    pdf_path = r"C:\Users\WorkStation\Downloads\GOUTHAM_ALAKUNTLA-.pdf"
    temp_path = r"C:\Users\WorkStation\Downloads\GOUTHAM_ALAKUNTLA-_temp.pdf"
    
    doc = fitz.open(pdf_path)
    page = doc[0]

    # 2. Delete old links in the Projects section
    # Projects section y-range is roughly 500 to 648
    links = page.get_links()
    for link in links:
        if 500 <= link["from"].y0 <= 648:
            page.delete_link(link)

    # 3. Apply redaction on the Summary text area (y: 109.0 to 143.0)
    rect_summary = fitz.Rect(35.2, 109.0, 574.8, 143.0)
    page.add_redact_annot(rect_summary, fill=(1, 1, 1))

    # 4. Apply redaction on the entire Projects content area (y: 502.0 to 648.0)
    rect_projects = fitz.Rect(35.2, 502.0, 578.0, 648.0)
    page.add_redact_annot(rect_projects, fill=(1, 1, 1))

    # 5. Apply all redactions
    page.apply_redactions()

    # 6. Insert new Summary text
    new_summary = (
        "Full-Stack & Generative AI Engineer who designs, builds, and ships AI-powered software products. "
        "Creator of Vibely, an AI-powered app builder, and GouthamAgent, a custom AI agent built by extending "
        "the open-source DataAgentBench framework. Passionate about AI Agents, LLM applications, and modern "
        "full-stack software engineering, with AI/LLM research experience at IIT Kharagpur and IIT Patna."
    )
    page.insert_textbox(rect_summary, new_summary, fontsize=8.2125, fontname="helv", color=(17/255, 17/255, 17/255), lineheight=1.2)

    # Helper function to draw a bullet point (circle + text)
    def draw_bullet(y_start, text_content, height=15.0):
        # Draw filled circle bullet at x=40.5
        page.draw_circle(fitz.Point(40.5, y_start + 4.0), 1.2, color=(17/255, 17/255, 17/255), fill=(17/255, 17/255, 17/255))
        # Draw text starting at x=46.3
        rect_text = fitz.Rect(46.3, y_start, 577.5, y_start + height)
        page.insert_textbox(rect_text, text_content, fontsize=7.785, fontname="helv", color=(17/255, 17/255, 17/255), lineheight=1.1)

    # 7. Draw Project 1 (GouthamAgent)
    # Title: GouthamAgent ↗ GitHub
    y_title1 = 504.6
    w1 = fitz.get_text_length("GouthamAgent", fontname="hebo", fontsize=8.2125)
    page.insert_text((35.25, y_title1 + 8.2125 * 0.905), "GouthamAgent", fontsize=8.2125, fontname="hebo", color=(17/255, 85/255, 204/255))
    page.insert_text((35.25 + w1, y_title1 + 8.2125 * 0.905), " ↗", fontsize=7.785, fontname="helv", color=(17/255, 85/255, 204/255))
    w2 = fitz.get_text_length(" ↗", fontname="helv", fontsize=7.785)
    page.insert_text((35.25 + w1 + w2, y_title1 + 8.2125 * 0.905), " GitHub", fontsize=7.785, fontname="hebo", color=(17/255, 85/255, 204/255))

    # Insert link for Project 1
    w3 = fitz.get_text_length(" GitHub", fontname="hebo", fontsize=7.785)
    link_rect1 = fitz.Rect(35.25, 504.6, 35.25 + w1 + w2 + w3, 514.0)
    page.insert_link({"kind": 2, "from": link_rect1, "uri": "https://github.com/gouthamdevolops/GouthamAgent"})

    # Project 1 Description (starts at x=35.25, height=15.0)
    y_desc1 = 515.5
    desc_rect1 = fitz.Rect(35.25, y_desc1, 577.5, y_desc1 + 15.0)
    desc_text1 = "Custom AI agent built by extending the open-source DataAgentBench framework for data analysis and tool orchestration."
    page.insert_textbox(desc_rect1, desc_text1, fontsize=7.785, fontname="helv", color=(17/255, 17/255, 17/255), lineheight=1.1)

    # Project 1 Bullets (Bullet 1 has a height of 22.0 to allow 2 lines wrapping)
    draw_bullet(525.5, "Designed and implemented GouthamAgent by extending the open-source DataAgentBench framework with custom prompting and intelligent tool orchestration.", height=22.0)
    draw_bullet(544.5, "Developed custom prompting strategies and tool orchestration for AI-driven data analysis.")
    draw_bullet(554.5, "Improved secure sandbox execution, validation workflows, and automated testing using GitHub Actions CI/CD.")
    draw_bullet(564.5, "Published the project with documentation, architecture diagrams, setup guides, and a production-ready GitHub repository.")

    # Project 1 Tech (height=15.0, separators updated to pipe characters)
    y_tech1 = 574.5
    tech_rect1 = fitz.Rect(35.25, y_tech1, 577.5, y_tech1 + 15.0)
    tech_text1 = "Tech: Python | AI Agents | LLMs | Prompt Engineering | Docker | GitHub Actions | CI/CD"
    page.insert_textbox(tech_rect1, tech_text1, fontsize=7.785, fontname="helv", color=(68/255, 68/255, 68/255), lineheight=1.1)

    # 8. Draw Project 2 (RAG-Based PDF Question-Answering Chatbot)
    # Title: RAG-Based PDF Question-Answering Chatbot ↗ Code
    y_title2 = 588.5
    w1_p2 = fitz.get_text_length("RAG-Based PDF Question-Answering Chatbot", fontname="hebo", fontsize=8.2125)
    page.insert_text((35.25, y_title2 + 8.2125 * 0.905), "RAG-Based PDF Question-Answering Chatbot", fontsize=8.2125, fontname="hebo", color=(17/255, 85/255, 204/255))
    page.insert_text((35.25 + w1_p2, y_title2 + 8.2125 * 0.905), " ↗", fontsize=7.785, fontname="helv", color=(17/255, 85/255, 204/255))
    w2_p2 = fitz.get_text_length(" ↗", fontname="helv", fontsize=7.785)
    page.insert_text((35.25 + w1_p2 + w2_p2, y_title2 + 8.2125 * 0.905), " Code", fontsize=7.785, fontname="hebo", color=(17/255, 85/255, 204/255))

    # Insert link for Project 2
    w3_p2 = fitz.get_text_length(" Code", fontname="hebo", fontsize=7.785)
    link_rect2 = fitz.Rect(35.25, y_title2, 35.25 + w1_p2 + w2_p2 + w3_p2, y_title2 + 9.4)
    page.insert_link({"kind": 2, "from": link_rect2, "uri": "https://github.com/gouthamdevolops/RAG-Based-PDF-Question-Answering-Chatbot"})

    # Project 2 Bullets (y: 600.0, 610.5, 621.0, 631.5)
    draw_bullet(600.0, "Built a Retrieval-Augmented Generation system that answers natural-language questions over user-uploaded PDFs.")
    draw_bullet(610.5, "Implemented document parsing, chunking, and embedding generation; stored vectors in Milvus for fast semantic search.")
    draw_bullet(621.0, "Improved answer accuracy with context-grounded generation, reducing off-topic and hallucinated responses.")
    draw_bullet(631.5, "Shipped an interactive chat interface in Streamlit with source-document references.")

    # Project 2 Tech (height=15.0)
    y_tech2 = 642.5
    tech_rect2 = fitz.Rect(35.25, y_tech2, 577.5, y_tech2 + 15.0)
    tech_text2 = "Tech: Python, LangChain, Milvus, Embeddings, Streamlit"
    page.insert_textbox(tech_rect2, tech_text2, fontsize=7.785, fontname="helv", color=(68/255, 68/255, 68/255), lineheight=1.1)

    # 9. Save the modified PDF to temp path
    doc.save(temp_path, incremental=False, encryption=fitz.PDF_ENCRYPT_KEEP)
    doc.close()
    
    # Replace the original with the temp file
    if os.path.exists(temp_path):
        if os.path.exists(pdf_path):
            os.remove(pdf_path)
        os.rename(temp_path, pdf_path)
        
    print("Resume PDF updated successfully!")

if __name__ == "__main__":
    main()
