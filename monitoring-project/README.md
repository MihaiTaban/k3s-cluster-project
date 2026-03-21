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

## 🛠️ 5. Management și Persistență

### 5.1. Instalare Helm (Pe Master)
\`\`\`bash
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
\`\`\`

### 5.2. Configurare Stocare Jenkins
\`\`\`bash
sudo mkdir -p /data/jenkins && sudo chown -R 1000:1000 /data/jenkins
\`\`\`

---

## 🚀 6. Configurare Jenkins (Namespace: cicd)

### 6.1. Instalare prin Helm
\`\`\`bash
kubectl create namespace cicd
helm repo add jenkins https://charts.jenkins.io
helm repo update
helm install jenkins jenkins/jenkins -n cicd -f charts/jenkins/values.yaml
\`\`\`

### 6.2. Operațiuni în Interfața Jenkins (http://192.168.56.102:32000)
După logare, am configurat Pipeline-ul de monitorizare astfel:
1. **New Item** -> Nume: \`deploy-monitoring\` -> Tip: **Pipeline**.
2. **Pipeline Definition**: Selectat "Pipeline script from SCM".
3. **SCM**: Git.
4. **Repository URL**: \`https://github.com/MihaiTaban/k3s-cluster-project.git\`.
5. **Branch Specifier**: \`*/main\` (Am corectat de la master la main).
6. **Script Path**: \`Jenkinsfile\`.

### 6.3. Drepturi de Execuție (RBAC)
Pentru ca Pipeline-ul să poată crea resurse în cluster, am rulat pe Master:
\`\`\`bash
kubectl create clusterrolebinding jenkins-agent-admin-binding \\
    --clusterrole=cluster-admin \\
    --serviceaccount=cicd:default
\`\`\`

---

## 📊 7. Monitorizare Prometheus (Namespace: monitoring)

Instalarea este realizată automat prin Jenkins. Am folosit o configurație **Ultra-Lite** pentru a proteja memoria RAM (2GB):
- **Resurse**: Limitare la 256Mi RAM per pod.
- **Acces UI**: Configurat ca NodePort pe portul **32100**.
- **URL**: http://192.168.56.102:32100

---

## 🛠️ Jurnal de Troubleshooting

| Etapa | Problema | Cauza | Soluție |
| :--- | :--- | :--- | :--- |
| **Jenkins** | CrashLoopBackOff | Startup lent al Java. | Crescut \`initialDelaySeconds\` la 120s. |
| **Jenkins UI** | Pipeline Fail (Git) | Branch default greșit. | Schimbat din \`*/master\` în \`*/main\`. |
| **Pipeline** | Permission Denied | Lipsă drepturi Agent. | Creat \`ClusterRoleBinding\` pentru serviceaccount. |
| **Cluster** | API Handshake Timeout | RAM 100% (Prometheus Stack). | Trecere la Prometheus Lite (fără Operator/Grafana). |

---

*Notă: Acest document servește ca suport de curs pentru sedimentarea noțiunilor DevOps.*
