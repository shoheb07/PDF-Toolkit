import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger, PdfReader, PdfWriter

# Main Window
root = tk.Tk()
root.title("PDF Toolkit")
root.geometry("500x350")

# Merge PDFs
def merge_pdfs():

    files = filedialog.askopenfilenames(
        filetypes=[("PDF Files", "*.pdf")]
    )

    if not files:
        return

    merger = PdfMerger()

    for pdf in files:
        merger.append(pdf)

    output = filedialog.asksaveasfilename(
        defaultextension=".pdf"
    )

    if output:

        merger.write(output)
        merger.close()

        messagebox.showinfo(
            "Success",
            "PDFs Merged Successfully!"
        )

# Split PDF
def split_pdf():

    file = filedialog.askopenfilename(
        filetypes=[("PDF Files", "*.pdf")]
    )

    if not file:
        return

    reader = PdfReader(file)

    for page_num in range(len(reader.pages)):

        writer = PdfWriter()

        writer.add_page(
            reader.pages[page_num]
        )

        with open(
            f"page_{page_num+1}.pdf",
            "wb"
        ) as output_pdf:

            writer.write(output_pdf)

    messagebox.showinfo(
        "Success",
        "PDF Split Completed!"
    )

# Extract Page
def extract_page():

    file = filedialog.askopenfilename(
        filetypes=[("PDF Files", "*.pdf")]
    )

    if not file:
        return

    page_num = int(
        page_entry.get()
    ) - 1

    reader = PdfReader(file)

    writer = PdfWriter()

    writer.add_page(
        reader.pages[page_num]
    )

    output = filedialog.asksaveasfilename(
        defaultextension=".pdf"
    )

    if output:

        with open(output, "wb") as pdf:

            writer.write(pdf)

        messagebox.showinfo(
            "Success",
            "Page Extracted!"
        )

# GUI Widgets
title = tk.Label(
    root,
    text="PDF Toolkit",
    font=("Arial", 20)
)

title.pack(pady=20)

merge_btn = tk.Button(
    root,
    text="Merge PDFs",
    width=25,
    command=merge_pdfs
)

merge_btn.pack(pady=10)

split_btn = tk.Button(
    root,
    text="Split PDF",
    width=25,
    command=split_pdf
)

split_btn.pack(pady=10)

page_entry = tk.Entry(root)
page_entry.pack(pady=10)

extract_btn = tk.Button(
    root,
    text="Extract Page",
    width=25,
    command=extract_page
)

extract_btn.pack(pady=10)

root.mainloop()
