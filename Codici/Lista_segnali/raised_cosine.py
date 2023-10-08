#%%
import numpy as np

def rho(t, alpha, T0, center):
    # t è l'array dei tempi in cui il segnale è valutato
    # alpha è il fattore di roll-off
    # T0 è la larghezza a metà altezza
    # center è il tempo di centro del segnale
    f0 = 1 / T0
    passband = (1 - alpha) / (2 * f0)
    stopband = (1 + alpha) / (2 * f0)
    
    # Inizializzazione
    rho_t = np.zeros(len(t), dtype=complex)
    
    for nch in range(len(center)):
        tt = np.abs(t - center[nch])
        t_minus_passband = np.abs(t - center[nch]) - passband
        
        if alpha == 0:
            rho_t = (t_minus_passband <= 0) + rho_t
        else:
            rho_t = (t_minus_passband <= 0) + \
                    (1/2 * (1 + np.cos(np.pi * f0 / alpha * t_minus_passband)) * (t_minus_passband > 0) * (np.abs(tt) <= stopband)) + \
                    rho_t
    
    return rho_t

# %%
