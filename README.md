# 🚀 Proiect Kubernetes Cluster (K3s) - Mihai

## 📅 Jurnal de Bord: Sâmbătă, 7 Martie 2026
Scopul primei sesiuni a fost ridicarea infrastructurii de bază și stabilirea fluxului de lucru prin Git.

---

## 🏗️ 1. Arhitectura Clusterului
* **Nod Master**: 192.168.56.101 (Ubuntu 24.04)
* **Nod Worker**: 192.168.56.102 (Ubuntu 24.04)
* **Interfață Rețea**: `enp0s8` (Host-Only VirtualBox)

### 🛠️ Comenzi de Administrare Noduri (Repetiție):
* **Verificare status noduri**: `kubectl get nodes`
* **Detalii complete nod**: `kubectl describe node master-k3s`
* **Verificare resurse (CPU/RAM)**: `kubectl top nodes` (necesită Metrics Server)

---

## 🔐 2. Securitate și Acces (RBAC Local)
Am configurat accesul pentru utilizatorul non-root `mihai` pentru a nu folosi `sudo` la fiecare comandă.

### 🛠️ Procedura de mutare Kubeconfig:
1. `mkdir -p $HOME/.kube`
2. `sudo cp /etc/rancher/k3s/k3s.yaml $HOME/.kube/config`
3. `sudo chown $USER:$USER $HOME/.kube/config`
4. `export KUBECONFIG=$HOME/.kube/config` (adăugat în `.bashrc`)

---

## 📦 3. Git & GitHub (Fluxul SSH)
Am eliminat nevoia de parole folosind chei asimetrice (Public/Private Key).

### 🛠️ Comenzi Cheie Git:
* **Generare cheie SSH**: `ssh-keygen -t ed25519 -C "master-k3s-laptop"`
* **Vizualizare cheie publică**: `cat ~/.ssh/id_ed25519.pub`
* **Setare URL SSH**: `git remote set-url origin git@github.com:UTILIZATOR/k3s-cluster-project.git`
* **Push cod**: `git add . && git commit -m "mesaj" && git push`

---

## 📂 4. Structură Proiect (GitOps Ready)
* `/charts` - Configurații Helm (Prometheus, Grafana, Jenkins).
* `/manifests` - Fișiere YAML (Deployment, Service, Ingress).
* `/scripts` - Automatizări Bash.

---

## 🚀 Plan Duminică, 8 Martie 2026 (Work in Progress):
1.  **Instalare Helm v3**: `curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash`
2.  **Configurare Jenkins**: Automatizarea fluxului de Deploy.
3.  **Monitoring**: Implementare Stack Prometheus & Grafana via Helm.

---
*Notă: Acest document servește ca suport de curs pentru sedimentarea noțiunilor DevOps.*
