# DevOps Starter Lab

This repo implements about 20% of the full DevOps practice list as a starter for students.
It gives a small working app and examples for CI/CD, Docker, nginx, Ansible, systemd,
Certbot hooks, Prometheus, cron migration, and log rotation.

## What is included

- A small Flask app with `/` and `/health` endpoints.
- A multi-stage Dockerfile.
- Docker Compose for `app + postgres + nginx + prometheus + node-exporter`.
- nginx reverse proxy with SSL-ready config, rate limiting, and health checks.
- GitLab CI and Jenkins pipeline examples with build/test/deploy stages.
- Ansible playbooks for idempotent Ubuntu provisioning.
- systemd service and timer examples.
- Certbot deploy hook for nginx reload.
- logrotate config for custom app logs.

## Quick Start

```bash
cd devops-starter-lab
docker compose up --build
```

Then open:

- App through nginx: `http://localhost`
- App direct port: `http://localhost:8000`
- Prometheus: `http://localhost:9090`

## Local App Test

```bash
cd app
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
pytest
```

## Ansible Dry Run

Edit `ansible/inventory.ini`, then run:

```bash
ansible-playbook -i ansible/inventory.ini ansible/playbooks/site.yml --check
```

## Student Tasks To Complete The Other 80%

1. Add deploy logic in `.gitlab-ci.yml` and `Jenkinsfile`.
2. Add a real domain and enable the SSL server block in `nginx/default.conf`.
3. Add Grafana to Docker Compose and import dashboards.
4. Add Alertmanager rules for CPU and disk usage.
5. Add restic or rsync backups to S3-compatible storage.
6. Add fail2ban and SSH hardening role in Ansible.
7. Add WireGuard role and inventory variables.
8. Convert another cron job to a systemd timer.
9. Add a private Docker registry service with basic auth.
10. Deploy this app to k3s using Kubernetes manifests.

## Repo Map

```text
app/                  Flask application and tests
ansible/              Ubuntu provisioning examples
certbot/              certificate renewal hook
ci/                   Jenkinsfile example
nginx/                reverse proxy config
monitoring/           Prometheus config
scripts/              backup script and timer demo script
systemd/              service/timer units
logrotate/            custom app log rotation
docker-compose.yml    local multi-service stack
.gitlab-ci.yml        GitLab CI pipeline
```

