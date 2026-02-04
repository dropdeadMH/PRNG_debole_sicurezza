import time
import secrets

# ============================================================
# 1. PRNG DEBOLE: Linear Congruential Generator (LCG)
# ============================================================

class LCG:
    def __init__(self, seed, a=1103515245, c=12345, m=2**31):
        self.state = seed
        self.a = a
        self.c = c
        self.m = m

    def next(self):
        self.state = (self.a * self.state + self.c) % self.m
        return self.state


# ============================================================
# 2. SERVER VULNERABILE: GENERAZIONE TOKEN
# ============================================================

def generate_vulnerable_token():
    seed = int(time.time())          # SEED PREVEDIBILE!
    prng = LCG(seed)
    token = prng.next()
    return token, seed


# ============================================================
# 3. ATTACCANTE: RECUPERO SEED (Timestamp Attack)
# ============================================================

def recover_seed(observed_token, approx_time, window=5):
    print("\n[ATTACK] Tentativo di recupero del seed...")
    for guessed_seed in range(approx_time - window, approx_time + window + 1):
        prng = LCG(guessed_seed)
        if prng.next() == observed_token:
            print(f"[SUCCESS] Seed recuperato: {guessed_seed}")
            return guessed_seed
    print("[FAIL] Seed non trovato")
    return None


# ============================================================
# 4. ATTACCANTE: PREDIZIONE TOKEN FUTURI
# ============================================================

def predict_next_tokens(seed, count=3):
    prng = LCG(seed)
    prng.next()  # salta il token già osservato
    predictions = [prng.next() for _ in range(count)]
    return predictions


# ============================================================
# 5. VERSIONE SICURA CON CSPRNG
# ============================================================

def generate_secure_token():
    return secrets.token_hex(16)


# ============================================================
# 6. DEMO COMPLETA
# ============================================================

def main():
    print("=" * 60)
    print(" DEMO: ATTACCHI SU PRNG DEBOLI (LCG)")
    print("=" * 60)

    # SERVER GENERA TOKEN
    print("\n[SERVER] Generazione token vulnerabile...")
    token, real_seed = generate_vulnerable_token()
    generation_time = int(time.time())

    print(f"[SERVER] Token generato: {token}")
    print(f"[DEBUG] Seed reale (server): {real_seed}")

    time.sleep(1)

    # ATTACCANTE RECUPERA IL SEED
    recovered_seed = recover_seed(
        observed_token=token,
        approx_time=generation_time
    )

    if recovered_seed is None:
        return

    # ATTACCANTE PREDICE TOKEN FUTURI
    print("\n[ATTACK] Predizione dei prossimi token...")
    predicted_tokens = predict_next_tokens(recovered_seed)

    for i, t in enumerate(predicted_tokens, 1):
        print(f"Predizione token {i}: {t}")

    # SERVER GENERA REALMENTE I TOKEN SUCCESSIVI
    print("\n[SERVER] Generazione reale dei token successivi...")
    prng = LCG(real_seed)
    prng.next()  # primo token già usato

    for i in range(1, 4):
        real_token = prng.next()
        print(f"Token reale {i}: {real_token}")

    # VERSIONE SICURA
    print("\n" + "=" * 60)
    print(" VERSIONE SICURA CON CSPRNG")
    print("=" * 60)

    secure_token = generate_secure_token()
    print(f"[SECURE] Token sicuro: {secure_token}")
    print("[INFO] Questo token non è predicibile né attaccabile")

    print("\nDEMO COMPLETATA")


if __name__ == "__main__":
    main()