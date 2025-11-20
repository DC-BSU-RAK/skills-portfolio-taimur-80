import tkinter as tk
from tkinter import ttk
import random
import os

class ModernJokeTellingAssistant:
    def __init__(self, root):
        self.root = root
        self.root.title("JokePal - Your AI Comedy Assistant")
        self.root.geometry("700x550")
        self.root.configure(bg="#1a1a1a")
        self.root.resizable(False, False)
        
        # Modern color scheme
        self.colors = {
            "primary": "#6366f1",
            "primary_dark": "#4f46e5",
            "secondary": "#f59e0b",
            "dark_bg": "#1a1a1a",
            "card_bg": "#2d2d2d",
            "text_primary": "#ffffff",
            "text_secondary": "#d1d5db",
            "accent": "#10b981"
        }
        
        # Load jokes from file
        self.jokes = self.load_jokes()
        self.current_joke = None
        
        # Create modern GUI
        self.create_modern_gui()
        
    def load_jokes(self):
        """Load jokes from randomJokes.txt in the same directory"""
        try:
            # Get the directory where the script is located
            script_dir = os.path.dirname(os.path.abspath(__file__))
            joke_file_path = os.path.join(script_dir, "randomJokes.txt")
            
            with open(joke_file_path, "r", encoding="utf-8") as file:
                jokes = [line.strip() for line in file if line.strip()]
            
            if not jokes:
                raise ValueError("Joke file is empty")
                
            print(f"Successfully loaded {len(jokes)} jokes from: {joke_file_path}")
            return jokes
            
        except FileNotFoundError:
            print("Error: randomJokes.txt not found in the script directory.")
            print("Please make sure randomJokes.txt exists in the same folder as this script.")
            return []
        except Exception as e:
            print(f"Error loading jokes: {str(e)}")
            return []
    
    def create_modern_gui(self):
        """Create a modern, sleek GUI"""
        # Header
        header_frame = tk.Frame(self.root, bg=self.colors["dark_bg"])
        header_frame.pack(fill="x", padx=20, pady=20)
        
        title_label = tk.Label(
            header_frame,
            text="JokePal",
            font=("Segoe UI", 28, "bold"),
            bg=self.colors["dark_bg"],
            fg=self.colors["text_primary"]
        )
        title_label.pack(side="left")
        
        subtitle_label = tk.Label(
            header_frame,
            text="Your AI Comedy Assistant",
            font=("Segoe UI", 12),
            bg=self.colors["dark_bg"],
            fg=self.colors["text_secondary"]
        )
        subtitle_label.pack(side="left", padx=(10, 0), pady=(8, 0))
        
        # Main card
        self.card_frame = tk.Frame(
            self.root,
            bg=self.colors["card_bg"],
            relief="flat",
            bd=0,
            highlightthickness=0
        )
        self.card_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Joke display area
        self.joke_display_frame = tk.Frame(self.card_frame, bg=self.colors["card_bg"])
        self.joke_display_frame.pack(fill="both", expand=True, padx=30, pady=30)
        
        # Setup label with modern styling
        self.setup_label = tk.Label(
            self.joke_display_frame,
            text="👋 Ready for a laugh?\nClick the button below to hear a joke!" if self.jokes else "❌ No jokes found!\nPlease make sure randomJokes.txt exists in the same folder.",
            font=("Segoe UI", 16),
            bg=self.colors["card_bg"],
            fg=self.colors["text_primary"] if self.jokes else "#ef4444",
            wraplength=550,
            justify="center",
            pady=20
        )
        self.setup_label.pack(expand=True)
        
        # Punchline label with fade-in effect
        self.punchline_label = tk.Label(
            self.joke_display_frame,
            text="",
            font=("Segoe UI", 14, "italic"),
            bg=self.colors["card_bg"],
            fg=self.colors["accent"],
            wraplength=500,
            justify="center"
        )
        self.punchline_label.pack(pady=10)
        
        # Button container
        button_container = tk.Frame(self.card_frame, bg=self.colors["card_bg"])
        button_container.pack(fill="x", padx=30, pady=20)
        
        # Main action button (Alexa)
        self.joke_button = self.create_modern_button(
            button_container,
            "🎭 Alexa, Tell Me a Joke",
            self.colors["primary"],
            self.tell_joke,
            state="normal" if self.jokes else "disabled"
        )
        self.joke_button.pack(fill="x", pady=5)
        
        # Secondary buttons frame
        secondary_buttons_frame = tk.Frame(button_container, bg=self.colors["card_bg"])
        secondary_buttons_frame.pack(fill="x", pady=10)
        
        # Show Punchline button
        self.punchline_button = self.create_modern_button(
            secondary_buttons_frame,
            "💡 Show Punchline",
            self.colors["secondary"],
            self.show_punchline,
            state="disabled"
        )
        self.punchline_button.pack(side="left", fill="x", expand=True, padx=(0, 5))
        
        # Next Joke button
        self.next_button = self.create_modern_button(
            secondary_buttons_frame,
            "🔄 Next Joke",
            "#8b5cf6",
            self.next_joke,
            state="disabled"
        )
        self.next_button.pack(side="left", fill="x", expand=True, padx=5)
        
        # Quit button
        self.quit_button = self.create_modern_button(
            secondary_buttons_frame,
            "🚪 Quit",
            "#ef4444",
            self.root.quit
        )
        self.quit_button.pack(side="left", fill="x", expand=True, padx=(5, 0))
        
        # Status bar
        status_frame = tk.Frame(self.root, bg=self.colors["dark_bg"])
        status_frame.pack(fill="x", padx=20, pady=10)
        
        status_text = f"📚 {len(self.jokes)} jokes loaded • Ready" if self.jokes else "❌ No jokes loaded • Please check randomJokes.txt"
        self.status_label = tk.Label(
            status_frame,
            text=status_text,
            font=("Segoe UI", 9),
            bg=self.colors["dark_bg"],
            fg=self.colors["text_secondary"] if self.jokes else "#ef4444"
        )
        self.status_label.pack(side="left")
        
        # File location info
        file_info = tk.Label(
            status_frame,
            text=f"File: randomJokes.txt",
            font=("Segoe UI", 8),
            bg=self.colors["dark_bg"],
            fg=self.colors["text_secondary"]
        )
        file_info.pack(side="right")
        
        # Add some decorative elements
        self.add_decorative_elements()
    
    def create_modern_button(self, parent, text, color, command, state="normal"):
        """Create a modern styled button"""
        button = tk.Button(
            parent,
            text=text,
            font=("Segoe UI", 11, "bold"),
            bg=color,
            fg="white",
            border=0,
            relief="flat",
            cursor="hand2",
            command=command,
            state=state,
            padx=20,
            pady=12
        )
        
        # Add hover effects
        def on_enter(e):
            if button['state'] != 'disabled':
                button['bg'] = self.darken_color(color, 0.2)
        
        def on_leave(e):
            if button['state'] != 'disabled':
                button['bg'] = color
        
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
        
        return button
    
    def darken_color(self, color, factor=0.2):
        """Darken a hex color by given factor"""
        color = color.lstrip('#')
        rgb = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
        darker = tuple(max(0, int(c * (1 - factor))) for c in rgb)
        return f'#{darker[0]:02x}{darker[1]:02x}{darker[2]:02x}'
    
    def add_decorative_elements(self):
        """Add some decorative elements for modern look"""
        # Add some subtle borders
        self.card_frame.configure(highlightbackground="#404040", highlightthickness=1)
    
    def parse_joke(self, joke_line):
        """Parse a joke line into setup and punchline"""
        if "?" in joke_line:
            parts = joke_line.split("?", 1)
            setup = parts[0] + "?"
            punchline = parts[1].strip()
        elif "|" in joke_line:
            parts = joke_line.split("|", 1)
            setup = parts[0]
            punchline = parts[1]
        else:
            setup = joke_line
            punchline = "No punchline available!"
        
        return setup, punchline
    
    def tell_joke(self):
        """Tell a random joke with smooth transitions"""
        if not self.jokes:
            self.setup_label.config(text="❌ No jokes available!\nPlease make sure randomJokes.txt exists with jokes.")
            return
        
        # Disable joke button temporarily
        self.joke_button.config(state="disabled")
        
        # Brief loading animation
        self.setup_label.config(text="🎭 Thinking of a good one...")
        self.root.update()
        self.root.after(500)  # Brief pause for effect
        
        # Select random joke
        self.current_joke = random.choice(self.jokes)
        setup, punchline = self.parse_joke(self.current_joke)
        
        # Update display with typing effect
        self.animate_text(self.setup_label, setup)
        self.punchline_label.config(text="")
        
        # Store punchline for later
        self.current_punchline = punchline
        
        # Update button states
        self.punchline_button.config(state="normal")
        self.next_button.config(state="normal")
        
        # Update status
        self.status_label.config(text="😄 Joke ready • Click 'Show Punchline'")
    
    def animate_text(self, label, text):
        """Animate text typing effect"""
        label.config(text="")
        self.root.update()
        
        def type_character(i=0):
            if i < len(text):
                current_text = label.cget("text") + text[i]
                label.config(text=current_text)
                self.root.after(30, lambda: type_character(i + 1))
        
        type_character()
    
    def show_punchline(self):
        """Show the punchline with animation"""
        if hasattr(self, 'current_punchline'):
            self.animate_text(self.punchline_label, self.current_punchline)
            self.punchline_button.config(state="disabled")
            self.status_label.config(text="😂 Hope that made you laugh! • Try 'Next Joke'")
    
    def next_joke(self):
        """Prepare for next joke with smooth transition"""
        self.setup_label.config(text="🔄 Getting another joke ready...")
        self.punchline_label.config(text="")
        self.root.update()
        self.root.after(300)
        
        # Reset to initial state
        if self.jokes:
            self.setup_label.config(
                text="👋 Ready for another laugh?\nClick the button below to hear a joke!",
                fg=self.colors["text_primary"]
            )
        else:
            self.setup_label.config(
                text="❌ No jokes available!\nPlease make sure randomJokes.txt exists with jokes.",
                fg="#ef4444"
            )
        
        # Update button states
        self.joke_button.config(state="normal" if self.jokes else "disabled")
        self.punchline_button.config(state="disabled")
        self.next_button.config(state="disabled")
        
        # Update status
        if self.jokes:
            self.status_label.config(text="📚 Ready for next joke • Click above to start")
        else:
            self.status_label.config(text="❌ No jokes loaded • Please check randomJokes.txt")

def main():
    root = tk.Tk()
    app = ModernJokeTellingAssistant(root)
    root.mainloop()

if __name__ == "__main__":
    main()