"""ILAINA-Viewer Customer V4: compact one-click SEND / STOP UI."""
import tkinter as tk
from tkinter import ttk
from customer_oneclick import CustomerApp as BaseCustomer
from common import NAVY, PANEL, TEAL, TEXT, MUTED

class CustomerApp(BaseCustomer):
    def __init__(self,root):
        super().__init__(root)
        root.title('ILAINA-Viewer | Customer')
        root.geometry('385x355')
        root.minsize(365,345)
    def _build(self):
        title=tk.Frame(self.root,bg=NAVY)
        title.pack(fill='x',padx=17,pady=(14,7))
        tk.Label(title,text='◈ ILAINA-VIEWER',fg=TEAL,bg=NAVY,
            font=('Segoe UI',17,'bold')).pack(anchor='w')
        tk.Label(title,text='CUSTOMER  •  ASSISTANCE À DISTANCE',
            fg=MUTED,bg=NAVY,font=('Segoe UI',8)).pack(anchor='w')
        panel=tk.Frame(self.root,bg=PANEL,padx=13,pady=11)
        panel.pack(fill='x',padx=16,pady=(3,8))
        tk.Label(panel,text='VOTRE PC',fg=MUTED,bg=PANEL,
            font=('Segoe UI',8,'bold')).pack(anchor='w')
        tk.Label(panel,text=self.pc,fg=TEXT,bg=PANEL,
            font=('Segoe UI',13,'bold'),anchor='w').pack(fill='x')
        tk.Label(self.root,textvariable=self.state_var,bg=NAVY,fg=TEAL,
            font=('Segoe UI',11,'bold')).pack(pady=(2,0))
        tk.Label(self.root,textvariable=self.detail_var,bg=NAVY,fg=MUTED,
            font=('Segoe UI',8),wraplength=345,justify='center').pack(pady=(2,6))
        self.send_btn=ttk.Button(self.root,text='SEND REQUEST  →',
            style='IL.TButton',command=self.request,state='disabled')
        self.send_btn.pack(fill='x',padx=22,pady=(0,6))
        self.stop_btn=ttk.Button(self.root,text='STOP / ANNULER',
            style='Stop.TButton',command=self.stop,state='disabled')
        self.stop_btn.pack(fill='x',padx=22)
        tk.Label(self.root,
            text='SEND: partage écran et contrôle après ACCEPT.\n'
                 'STOP: arrêt immédiat à tout moment.',
            bg=NAVY,fg=MUTED,font=('Segoe UI',8),justify='center'
        ).pack(pady=(10,2))

if __name__=='__main__':
    root=tk.Tk()
    CustomerApp(root)
    root.mainloop()
