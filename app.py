import gradio as gr

def generate_questions(text):
    if not text.strip():
        return "Please enter some text."

    sentences = text.split(".")
    questions = []

    count = 1
    for sentence in sentences:
        s = sentence.strip()
        if s:
            questions.append(f"{count}. What is {s}?")
            count += 1
        if count > 5:
            break

    if not questions:
        return "Unable to generate questions. Try different text."

    return "\n\n".join(questions)


# UI
with gr.Blocks(theme=gr.themes.Soft(primary_hue="indigo", secondary_hue="blue")) as demo:

    gr.Markdown("# 📚 Smart Study Assistant")
    gr.Markdown("Generate questions from your study notes using AI")

    with gr.Row():
        input_text = gr.Textbox(
            lines=10,
            label="📥 Input Text",
            placeholder="Paste your study material here..."
        )

        output_text = gr.Textbox(
            lines=10,
            label="📤 Generated Questions"
        )

    with gr.Row():
        submit_btn = gr.Button("✨ Generate Questions", variant="primary")
        clear_btn = gr.Button("🧹 Clear")

    submit_btn.click(fn=generate_questions, inputs=input_text, outputs=output_text)
    clear_btn.click(lambda: ("", ""), outputs=[input_text, output_text])

demo.launch()
