import tkinter as tk
from tkinter import scrolledtext

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatovací aplikace")
        
        self.responses = {
            "ahoj": "Ahoj! Jak se máš?",
            "jak se maš": "Nevím jak ty!",
            "co je Python?": "Python je programovací jazyk.",
            "kolikrat sis dnes prdnul":"16"

    
        }
        
        self.chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20)
        self.chat_window.grid(row=0, column=0, padx=10, pady=10)
        self.chat_window.configure(state='disabled')
        
        self.message_entry = tk.Entry(root, width=50)
        self.message_entry.grid(row=1, column=0, padx=10, pady=10)
        self.message_entry.bind("<Return>", self.send_message)
        
        self.send_button = tk.Button(root, text="Odeslat", command=self.send_message)
        self.send_button.grid(row=2, column=0, padx=10, pady=10)
    
    def send_message(self, event=None):
        message = self.message_entry.get()
        if message.strip():
            self.chat_window.configure(state='normal')
            self.chat_window.insert(tk.END, f"Ty: {message}\n")
            self.chat_window.configure(state='disabled')
            self.message_entry.delete(0, tk.END)
            self.respond(message)
    
    def respond(self, message):
        if message in self.responses:
            response = self.responses[message]
        else:
            response = "Nemám odpověď, co mam dat na to "
            self.chat_window.configure(state='normal')
            self.chat_window.insert(tk.END, f"Albert: {response}\n")
            self.chat_window.configure(state='disabled')
            
            def learn_response(event=None):
                user_response = self.message_entry.get()
                if user_response.strip():
                    self.responses[message] = user_response
                    self.chat_window.configure(state='normal')
                    self.chat_window.insert(tk.END, f"Albert: diky za odpověd '{message}'!\n")
                    self.chat_window.configure(state='disabled')
                    self.message_entry.unbind("<Return>")  
                    self.message_entry.delete(0, tk.END)

            self.message_entry.bind("<Return>", learn_response)
        self.chat_window.configure(state='normal')
        self.chat_window.insert(tk.END, f"Albert: {response}\n")
        self.chat_window.configure(state='disabled')


if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()
