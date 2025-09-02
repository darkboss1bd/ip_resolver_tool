import tkinter as tk
from tkinter import ttk, messagebox
import socket
import pyperclip

# Main Application
class IPResolverTool:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 darkboss1bd - Advanced IP Resolver")
        self.root.geometry("700x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#121212")

        # Icon (Optional: you can add .ico file)
        # root.iconbitmap('hacker.ico')

        self.setup_ui()

    def setup_ui(self):
        # Hacker-style ASCII Banner
        banner_text = r"""
  ___ _   _ ____  _     ____  _____ ____  
 / __| | | |  _ \| |   |  _ \| ____|  _ \ 
| (__| |_| | |_) | |   | |_) |  _| | |_) |
 \___|\___/|____/|_|   |____/|_____|____/ 
        Advanced IP Resolver Tool
           Coded by: darkboss1bd
        """

        banner = tk.Label(
            self.root,
            text=banner_text,
            font=("Courier", 10, "bold"),
            fg="#00ff00",
            bg="#121212",
            justify="left",
            anchor="w"
        )
        banner.pack(pady=10, padx=10)

        # Info Links (Clickable)
        link_frame = tk.Frame(self.root, bg="#121212")
        link_frame.pack(pady=5)

        tk.Label(link_frame, text="Contact Me:", fg="white", bg="#121212").pack(side="left", padx=5)

        self.make_clickable_label(link_frame, "Telegram", "https://t.me/darkvaiadmin", "#0088ff")
        tk.Label(link_frame, text=" | ", fg="white", bg="#121212").pack(side="left")
        self.make_clickable_label(link_frame, "My Website", "https://serialkey.top/", "#00ff88")

        # Input Frame
        input_frame = tk.Frame(self.root, bg="#121212")
        input_frame.pack(pady=20)

        tk.Label(input_frame, text="Enter Website URL:", font=("Helvetica", 12), fg="white", bg="#121212").pack()
        
        self.url_entry = ttk.Entry(input_frame, width=50, font=("Helvetica", 12))
        self.url_entry.pack(pady=5, ipady=5)

        self.resolve_btn = ttk.Button(input_frame, text="🔍 Resolve IP", command=self.resolve_ip)
        self.resolve_btn.pack(pady=10)

        # Result Frame
        result_frame = tk.Frame(self.root, bg="#121212")
        result_frame.pack(pady=10, fill="x", padx=50)

        tk.Label(result_frame, text="Resolved IP Address:", font=("Helvetica", 12), fg="white", bg="#121212").pack()

        self.ip_text = tk.Text(result_frame, height=2, width=40, font=("Helvetica", 12), bg="#1e1e1e", fg="#00ff00", bd=2, relief="solid")
        self.ip_text.pack(pady=5)
        self.ip_text.config(state="disabled")

        # Copy Button
        self.copy_btn = ttk.Button(result_frame, text="📋 Copy IP", command=self.copy_ip)
        self.copy_btn.pack(pady=5)

        # Animation Console (Hacker Style)
        self.console = tk.Text(self.root, height=10, width=80, bg="#000000", fg="#00ff00", font=("Courier", 9), state="normal")
        self.console.pack(pady=20)
        self.console.insert("end", "[+] System initialized...\n")
        self.console.insert("end", "[+] Waiting for input...\n")
        self.console.config(state="disabled")

    def make_clickable_label(self, parent, text, url, color):
        label = tk.Label(parent, text=text, fg=color, bg="#121212", cursor="hand2", font=("Helvetica", 10, "underline"))
        label.pack(side="left")
        label.bind("<Button-1>", lambda e: self.open_url(url))

    def open_url(self, url):
        import webbrowser
        webbrowser.open(url)

    def resolve_ip(self):
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showwarning("Input Error", "Please enter a website URL!")
            return

        # Clean URL (remove http/https and trailing slashes)
        if "http://" in url or "https://" in url:
            url = url.split("://")[1]
        url = url.split("/")[0].strip()

        try:
            self.console_update(f"[+] Resolving IP for: {url}...")
            ip = socket.gethostbyname(url)
            self.console_update(f"[✓] IP Found: {ip}")

            self.ip_text.config(state="normal")
            self.ip_text.delete(1.0, "end")
            self.ip_text.insert("end", ip)
            self.ip_text.config(state="disabled")
        except socket.gaierror:
            self.console_update(f"[×] Failed to resolve IP for: {url}")
            messagebox.showerror("Resolution Error", f"Could not resolve IP address for '{url}'.\nCheck the domain and try again.")
        except Exception as e:
            self.console_update(f"[!] Error: {str(e)}")
            messagebox.showerror("Error", str(e))

    def copy_ip(self):
        ip = self.ip_text.get(1.0, "end").strip()
        if ip and ip != "":
            pyperclip.copy(ip)
            self.console_update("[✓] IP copied to clipboard!")
            messagebox.showinfo("Copied", "IP address copied to clipboard!")

    def console_update(self, message):
        self.console.config(state="normal")
        self.console.insert("end", message + "\n")
        self.console.see("end")
        self.console.config(state="disabled")

# Run the app
if __name__ == "__main__":
    try:
        import pyperclip
    except ImportError:
        print("Please install pyperclip: pip install pyperclip")
        exit()

    root = tk.Tk()
    app = IPResolverTool(root)
    root.mainloop()