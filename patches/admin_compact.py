"""ILAINA-Viewer Admin V4 — compact password-only console."""
import tkinter as tk
from tkinter import ttk, messagebox
from admin import AdminApp as BaseAdmin
from common import DEFAULT_URL, NAVY, PANEL, TEAL, TEXT, MUTED

class AdminApp(BaseAdmin):
    def __init__(self, root):
        super().__init__(root)
        root.title('ILAINA-Viewer | Admin')
        root.geometry('920x585')
        root.minsize(730,470)
    def _build(self):
        heading=tk.Frame(self.root,bg=NAVY)
        heading.pack(fill='x',padx=16,pady=(12,6))
        tk.Label(heading,text='◈ ILAINA-VIEWER',fg=TEAL,bg=NAVY,
            font=('Segoe UI',18,'bold')).pack(side='left')
        tk.Label(heading,text='ADMIN',fg=MUTED,bg=NAVY,
            font=('Segoe UI',9,'bold')).pack(side='left',padx=10,pady=(6,0))
        tk.Label(heading,textvariable=self.status_var,fg=TEAL,bg=NAVY,
            font=('Segoe UI',9,'bold')).pack(side='right')
        self.login_bar=tk.Frame(self.root,bg=PANEL,padx=12,pady=10)
        self.login_bar.pack(fill='x',padx=16,pady=(0,8))
        tk.Label(self.login_bar,text='PASSWORD ADMIN',fg=MUTED,bg=PANEL,
            font=('Segoe UI',9,'bold')).pack(side='left',padx=(0,10))
        self.password_entry=ttk.Entry(self.login_bar,textvariable=self.token_var,
            show='●',style='IL.TEntry',width=29)
        self.password_entry.pack(side='left',fill='x',expand=True,padx=(0,10))
        self.password_entry.bind('<Return>',lambda _e:self.connect())
        ttk.Button(self.login_bar,text='LOGIN',style='IL.TButton',
            command=self.connect).pack(side='right')
        self.root.after(100,self.password_entry.focus_set)
        line=tk.Frame(self.root,bg=NAVY)
        line.pack(fill='x',padx=18,pady=(0,9))
        tk.Label(line,textvariable=self.pc_var,bg=NAVY,fg=TEXT,
            font=('Segoe UI',10,'bold')).pack(side='left')
        self.stop_btn=ttk.Button(line,text='STOP',style='Stop.TButton',
            command=self.stop,state='disabled')
        self.stop_btn.pack(side='right')
        self.pending_btn=ttk.Button(line,text='DEMANDES (0)',
            style='Secondary.TButton',command=self._notify_pending)
        self.pending_btn.pack(side='right',padx=(0,9))
        self.canvas=tk.Canvas(self.root,bg='#070D15',highlightthickness=0,
            cursor='crosshair',takefocus=1)
        self.canvas.pack(fill='both',expand=True,padx=16,pady=(0,12))
        self.canvas.bind('<Configure>',lambda e:self._draw())
        self.canvas.bind('<Motion>',self._motion)
        for i,button in ((1,'left'),(2,'middle'),(3,'right')):
            self.canvas.bind(f'<ButtonPress-{i}>',lambda e,b=button:self._button(e,b,True))
            self.canvas.bind(f'<ButtonRelease-{i}>',lambda e,b=button:self._button(e,b,False))
        self.canvas.bind('<MouseWheel>',self._wheel)
        self.canvas.bind('<KeyPress>',lambda e:self._key(e,True))
        self.canvas.bind('<KeyRelease>',lambda e:self._key(e,False))
        self.canvas.bind('<FocusOut>',self._focus_lost)
        self._draw()
    def connect(self):
        password=self.token_var.get()
        if not password:
            messagebox.showwarning('ILAINA-Viewer','Ampidiro ny PASSWORD ADMIN.',parent=self.root)
            return
        self.bridge.start(DEFAULT_URL,password)
        self.status_var.set('CONNEXION...')
    def _handle(self,e):
        kind=e.get('type')
        super()._handle(e)
        if kind=='ready':
            self.token_var.set('')
            self.login_bar.pack_forget()
        elif kind in ('local_error','transport_down') and not self.bridge.ready:
            if not self.login_bar.winfo_manager():
                self.login_bar.pack(fill='x',padx=16,pady=(0,8),
                    after=self.root.winfo_children()[0])

if __name__=='__main__':
    root=tk.Tk()
    AdminApp(root)
    root.mainloop()
