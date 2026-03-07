# Proiect Kubernetes Cluster - Mihai

## 📅 Status Proiect: Sâmbătă, 7 Martie 2026
Clusterul este complet funcțional și a trecut testul de stabilitate după reboot.

## 🏗️ Infrastructură Detaliată
* **Nod Master**: 192.168.56.101 (Ubuntu 24.04)
* **Nod Worker**: 192.168.56.102 (Ubuntu 24.04)
* **K3s Version**: v1.34.5
* **Interfață Rețea Cluster**: enp0s8

## 📂 Structură Proiect
* `/` - Documentație principală
* `/helm-charts` - (Mâine) Configurații Prometheus, Grafana, Jenkins
* `/apps` - (În curând) Manifestele aplicației propriu-zise

## 🛠️ Configurații realizate azi:
1. **Rețea**: Configurat interfete enp0s8 pentru comunicare internă.
2. **Permisiuni**: Utilizatorul 'mihai' are acces la kubectl prin config-ul local (/home/mihai/.kube/config).
3. **Helm**: Instalat și pregătit pentru deploy-uri.

## ✅ Validări Tehnice
* **Acces fără sudo**: Confirmat.
* **Persistență**: Serviciile K3s pornesc automat la boot.

## 🚀 Plan pentru Mâine (Duminică):
* Instalare Prometheus & Grafana (Monitoring) în namespace-ul `monitoring`.
* Pregătire mediu Jenkins (CI/CD) în namespace-ul `cicd`.
* Creare fișiere Helm Chart pentru aplicație.
