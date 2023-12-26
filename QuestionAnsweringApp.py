
import tkinter as tk


# In[2]:


from tkinter import filedialog


# In[3]:


import nltk


# In[10]:


from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag
from nltk.chunk import ne_chunk
import re


# In[32]:


class QuestionAnsweringApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Question Answering App")

        self.textbox = tk.Text(self.root, height=10, width=50)
        self.textbox.pack(pady=10)

        self.browse_button = tk.Button(self.root, text="Browse", command=self.browse_file)
        self.browse_button.pack(pady=5)

        self.question_entry = tk.Entry(self.root, width=50)
        self.question_entry.pack(pady=5)

        self.answer_label = tk.Label(self.root, text="")
        self.answer_label.pack(pady=10)

        self.answer_button = tk.Button(self.root, text="Answer Question", command=self.answer_question)
        self.answer_button.pack(pady=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                self.textbox.delete('1.0', tk.END)
                self.textbox.insert(tk.END, content)
    def answer_question(self):
        context = self.textbox.get("1.0", tk.END)
        question = self.question_entry.get()

        if context and question:
            # Tokenize question
            question_words = set(nltk.word_tokenize(question.lower()))

            # Find the most relevant sentence based on word overlap
            sentences = nltk.sent_tokenize(context)
            max_overlap = 0
            relevant_sentence = ""

            for sent in sentences:
                sent_words = set(nltk.word_tokenize(sent.lower()))
                overlap = len(question_words.intersection(sent_words))
                if overlap > max_overlap:
                    max_overlap = overlap
                    relevant_sentence = sent

            # Display the answer
            if max_overlap > 0:
                answer = relevant_sentence
            else:
                answer = "Sorry, I don't know the answer."

            self.answer_label.config(text="Answer: " + answer)
        else:
            self.answer_label.config(text="Please provide both context and question.")
if __name__ == "__main__":
    root = tk.Tk()
    app = QuestionAnsweringApp(root)
    root.mainloop()


# In[ ]:




