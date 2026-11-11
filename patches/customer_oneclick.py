"""ILAINA-Viewer Customer One Click: zero manual login, explicit SEND/STOP.

The broker issues a short-lived guest ticket. A guest is never authorised as admin;
only a customer-initiated SEND followed by an admin ACCEPT enables a session.
"""
import tkinter as tk
from tkinter import ttk
from common import NAVY, PANEL, TEAL, TEXT, MUTED
from customer import CustomerApp as OriginalCustomerApp


class CustomerApp(OriginalCustomerApp):
    def __init__(self, root):
        super().__init__(root)
        root.title('ILAINA-Viewer | Assistance client')
        root.geometry('474x508')
        root.minsize(430, 485)
        self._auto_started = False
        self.root.after(220, self.connect)

    def _build(self):
        header = tk.Frame(self.root, bg=NAVY)
        header.pack(fill='x', padx=28, pady=(29, 12))
        tk.Label(header, text='◈  ILAINA-VIEWER', fg=TEAL, bg=NAVY,
                 font=('Segoe UI', 23, 'bold')).pack(anchor='w')
        tk.Label(header, text='ASSISTANCE À DISTANCE  •  CLIENT', fg=MUTED, bg=NAVY,
                 font=('Segoe UI', 9, 'bold')).pack(anchor='w', pady=(4, 0))
        machine = tk.Frame(self.root, bg=PANEL, padx=23, pady=20)
        machine.pack(fill='x', padx=24, pady=(8, 18))
        tk.Label(machine, text='VOTRE ORDINATEUR', bg=PANEL, fg=MUTED,
                 font=('Segoe UI', 9, 'bold')).pack(anchor='w')
        tk.Label(machine, text=self.pc, bg=PANEL, fg=TEXT,
                 font=('Segoe UI', 17, 'bold'), anchor='w').pack(fill='x', pady=(7, 0))
        signal = tk.Frame(self.root, bg=NAVY)
        signal.pack(fill='x', padx=25, pady=(0, 12))
        tk.Label(signal, textvariable=self.state_var, fg=TEAL, bg=NAVY,
                 font=('Segoe UI', 13, 'bold')).pack()
        tk.Label(signal, textvariable=self.detail_var, fg=MUTED, bg=NAVY,
                 font=('Segoe UI', 10), wraplength=405, justify='center').pack(pady=(7, 7))
        self.send_btn = ttk.Button(self.root, text='SEND REQUEST  →',
                                   style='IL.TButton', command=self.request,
                                   state='disabled')
        self.send_btn.pack(fill='x', padx=37, pady=(2, 10), ipady=8)
        self.stop_btn = ttk.Button(self.root, text='STOP / ANNULER',
                                   style='Stop.TButton', command=self.stop,
                                   state='disabled')
        self.stop_btn.pack(fill='x', padx=37, ipady=4)
        tk.Label(self.root,
                 text='SEND = mangataka fanampiana sy manaiky ny partage écran,\n'
                      'souris ary clavier rehefa neken’ny technicien.\n'
                      'STOP = mampiato ny contrôle avy hatrany.',
                 fg=MUTED, bg=NAVY, font=('Segoe UI', 9),
                 wraplength=405, justify='center').pack(pady=(19, 8))

    def connect(self):
        if self._auto_started:
            return
        self._auto_started = True
        self.stop(local_only=True)
        self.state_var.set('FIFANDRAISANA...')
        self.detail_var.set('Mifandray amin’ny serveur ILAINA-Viewer...')
        self.bridge.start('https://www.gsmunlockerfix.top/viewer/', '', self.pc)

    def _handle(self, e):
        kind = e.get('type')
        if kind == 'local_error':
            message = e.get('message', '')
            if 'invalide' in message or 'tentatives' in message:
                e = {**e, 'message': 'Mbola tsy nohavaozina ny backend cPanel. Apetraho ny version One-Click V3.'}
            self.state_var.set('TSY AFAKA MIFANDRAY')
        super()._handle(e)
        if kind == 'ready':
            self.detail_var.set('Tsindrio SEND raha mila fanampiana.')
        elif kind == 'transport_down':
            self.detail_var.set('Tsy misy connexion. Hanandrana indray ho azy.')


if __name__ == '__main__':
    root = tk.Tk()
    CustomerApp(root)
    root.mainloop()
