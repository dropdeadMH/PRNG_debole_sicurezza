# PRNG debole e attacco a seed prevedibile

Questo progetto dimostra perché **i generatori pseudo-casuali deboli (PRNG)** non devono essere usati per la generazione di token di sicurezza.

In particolare, viene mostrato un **attacco realistico** contro un *Linear Congruential Generator (LCG)* inizializzato con un **seed prevedibile basato sul timestamp**.

---

## 📌 Obiettivo del progetto

- Mostrare come un PRNG debole possa essere **attaccato**
- Dimostrare un **timestamp attack** per recuperare il seed
- Predire token futuri una volta compromesso il generatore
- Confrontare l’approccio vulnerabile con una **soluzione sicura (CSPRNG)**

---

## 🐍 Requisiti

- Python **3.8+**
- Nessuna dipendenza esterna

---

## ⚙️ Installazione

   ```bash
   git clone https://github.com/dropdeadMH/PRNG_debole_sicurezza.git
   cd PRNG_debole_sicurezza
   python prng.py
