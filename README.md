cat > README.md <<'EOF'
# CartNest

**A cloud-native e-commerce platform built to demonstrate full-stack development and real-world DevOps practices.**

CartNest is a hands-on project for building, testing, containerizing, deploying, and operating an e-commerce application across development and production environments.

## Project goals

- Build a responsive shopping experience with React and TypeScript.
- Develop a REST API with Python and FastAPI.
- Persist products and orders in PostgreSQL.
- Run the application locally with Docker Compose.
- Automate linting, testing, security checks, and image publishing with GitHub Actions.
- Store versioned container images in GitHub Container Registry (GHCR).
- Deploy workloads to Kubernetes using Deployments, Services, ConfigMaps, Secrets, probes, resource controls, and persistent storage.
- Maintain environment-specific Kubernetes configuration with Kustomize.
- Practice rolling deployments, rollback, scaling, troubleshooting, and application self-healing.
- Progress toward monitoring, infrastructure as code, and GitOps.

## Planned technology stack

| Area | Technology |
|---|---|
| Frontend | React, TypeScript, Vite |
| Backend | Python, FastAPI |
| Database | PostgreSQL |
| Local development | Docker, Docker Compose |
| Orchestration | Kubernetes, kubectl, kind |
| Kubernetes configuration | YAML, Kustomize |
| CI/CD | GitHub Actions |
| Container registry | GitHub Container Registry |
| Testing | Pytest, HTTPX, Vitest |
| Security | Dependency and container image scanning |
| Future infrastructure | Terraform, AWS EKS |
| Future observability | Prometheus, Grafana |

## Architecture

The planned application consists of three main components:

1. **Frontend:** Product catalog, shopping cart, and order history.
2. **Backend API:** Product and order operations, validation, and health endpoints.
3. **Database:** PostgreSQL persistence for application data.

The application will first run locally. It will then be containerized and deployed to a local Kubernetes cluster. Development and production configurations will be introduced before progressing to cloud infrastructure.

## Repository layout

```text
cartnest/
├── frontend/
├── backend/
│   ├── app/
│   └── tests/
├── database/
│   └── migrations/
├── tests/
│   └── integration/
├── k8s/
│   ├── base/
│   └── overlays/
│       ├── development/
│       └── production/
├── docs/
├── .github/
│   └── workflows/
├── .gitignore
└── README.md