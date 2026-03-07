# Proiect Kubernetes Cluster - Mihai

## 📅 Status Proiect: Sâmbătă, 7 Martie 2026
Clusterul este complet funcțional și a trecut testul de stabilitate după reboot.

## 🏗️ Infrastructură
* **Nod Master**: 192.168.56.101 (Ubuntu 24.04)
* **Nod Worker**: 192.168.56.102 (Ubuntu 24.04)
* **K3s Version**: v1.34.5

## 🛠️ Configurații realizate azi:
1.  **Rețea**: Configurat interfete enp0s8 pentru comunicare internă.
2.  **Permisiuni**: Utilizatorul 'mihai' are acces la kubectl prin config-ul local.
3.  **Helm**: Instalat și pregătit pentru deploy-uri.

## 🚀 Plan pentru Mâine (Duminică):
* Instalare Prometheus & Grafana (Monitoring)
* Pregătire mediu Jenkins (CI/CD)
* Creare fișiere Helm Chart pentru aplicație

## ✅ Validare Stabilitate
* [07-03-2026 10:17] Test Reboot efectuat: Clusterul revine automat în starea Ready.
