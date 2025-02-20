# Correction_qcm



## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended next steps.

Already a pro? Just edit this README.md and make it your own. Want to make it easy? [Use the template at the bottom](#editing-this-readme)!

## Add your files

- [ ] [Create](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://docs.gitlab.com/ee/gitlab-basics/add-file.html#add-a-file-using-the-command-line) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin https://devops.telecomste.fr/mhajar.youness/correction_qcm.git
git branch -M main
git push -uf origin main
```

## Integrate with your tools

- [ ] [Set up project integrations](https://devops.telecomste.fr/mhajar.youness/correction_qcm/-/settings/integrations)

## Collaborate with your team

- [ ] [Invite team members and collaborators](https://docs.gitlab.com/ee/user/project/members/)
- [ ] [Create a new merge request](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
- [ ] [Automatically close issues from merge requests](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically)
- [ ] [Enable merge request approvals](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/)
- [ ] [Set auto-merge](https://docs.gitlab.com/ee/user/project/merge_requests/merge_when_pipeline_succeeds.html)

## Test and Deploy

Use the built-in continuous integration in GitLab.

- [ ] [Get started with GitLab CI/CD](https://docs.gitlab.com/ee/ci/quick_start/index.html)
- [ ] [Analyze your code for known vulnerabilities with Static Application Security Testing (SAST)](https://docs.gitlab.com/ee/user/application_security/sast/)
- [ ] [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto Deploy](https://docs.gitlab.com/ee/topics/autodevops/requirements.html)
- [ ] [Use pull-based deployments for improved Kubernetes management](https://docs.gitlab.com/ee/user/clusters/agent/)
- [ ] [Set up protected environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html)

***

## Correction Automatique des QCM

Ce projet permet de corriger automatiquement des QCM à partir d'images scannées ou téléchargées. Il offre une interface utilisateur basée sur Streamlit et permet une visualisation conviviale des résultats.
## execution 

* double clique sur run.bat 
* deposer l'image qcm.jpeg
* cliquer sur corriger

## Pré-requis

Avant de commencer, assurez-vous d'avoir les éléments suivants :

Python 3.11 ou version supérieure : Disponible sur python.org.

Git : Installer Git.

Pip : Gestionnaire de paquets Python (installé par défaut avec Python).

Installation

# 1. Cloner le dépôt Git

Clonez le dépôt sur votre machine locale :

git clone [https://devops.telecomste.fr/mhajar.youness/correction_qcm.git](https://github.com/mhajar11/QCM-auto-correction
cd correction_qcm

# 2. Créer un environnement virtuel

Créez un environnement virtuel Python et activez-le :

- Windows

python -m venv venv
venv\Scripts\activate

- macOS/Linux

python3 -m venv venv
source venv/bin/activate

# 3. Installer les dépendances

Installez les dépendances listées dans requirements.txt :

pip install -r requirements.txt

Instructions d'utilisation

## 1. Lancer l'application Streamlit

Exécutez la commande suivante pour lancer l'interface utilisateur :

streamlit run script_interface.py

## 2. Utilisation

Définissez les réponses correctes pour chaque question.

Téléchargez l'image scannée d'un QCM.

Visualisez les réponses détectées, le score et les questions correctes.


## Fonctionnalités

- Détection et correction automatique des QCM :

- Binarisation et extraction des composantes connexes.

- Analyse des cases cochées pour déterminer les réponses.

- Calcul du score final.

- Interface utilisateur conviviale via Streamlit.

- Visualisation des images intermédiaires (images binaires, filtrées, annotées).

- Génération de fichiers exécutables pour faciliter le partage.

## Dépendances

Les principales bibliothèques Python utilisées sont :

* Streamlit : Interface utilisateur.

* OpenCV : Traitement d'image.

* NumPy : Calculs matriciels et numériques.

## Licence

Ce projet est sous licence MIT. Vous êtes libre de l'utiliser, de le modifier et de le distribuer, sous réserve de conserver les mentions de droits d'auteur.
