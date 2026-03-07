# Proiect Kubernetes Cluster - Mihai

## 📅 Status Proiect: Sâmbătă, 7 Martie 2026
Clusterul este complet funcțional, testat după reboot și conectat la GitHub prin SSH.

## 🏗️ Infrastructură Detaliată
* **Nod Master**: 192.168.56.101 (Ubuntu 24.04)
* **Nod Worker**: 192.168.56.102 (Ubuntu 24.04)
* **K3s Version**: v1.34.5

## 📂 Structură Proiect (GitOps)
* `/` - Documentație principală (README).
* `/charts` - Configurații Helm pentru Prometheus, Grafana și Jenkins.
* `/manifests` - Fișiere YAML pentru aplicația proprie.
* `/scripts` - Scripturi de automatizare sau mentenanță.

## 🛠️ Configurații realizate azi:
1. **Networking**: Configurat IP-uri statice pe interfața secundară.
2. **K3s Cluster**: Instalat Master și unit Worker-ul în mod stabil.
3. **Securitate & Acces**: Configurat acces `kubectl` pentru userul `mihai` și chei SSH pentru GitHub.
4. **GitOps Init**: Creat depozitul local și sincronizat cu GitHub.

## 🚀 Plan pentru Mâine (Duminică - Sesiune 2h):
* [ ] **Instalare Helm v3**: Primul pas pentru managementul pachetelor.
* [ ] **Monitoring**: Deploy Prometheus & Grafana folosind Helm.
* [ ] **CI/CD**: Instalare Jenkins în cluster.
* [ ] **Proiect Structura**: Crearea folderelor fizice conform schemei de mai sus.

## ✅ Validări Tehnice
* **Acces fără sudo**: Confirmat.
* **Persistență**: Serviciile K3s pornesc automat la boot.
