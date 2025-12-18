### **CD Workflow Documentation**

This document explains the Continuous Deployment (CD) workflow defined in [cd.yml](cd.yml). The workflow is automatically triggered on every `push` to the `master` branch and deploys the application to a remote Virtual Private Server (VPS) using Docker.


### **Key Keywords and Structure**

#### **`on:`**
Specifies when the workflow should run.

- **`push`**: Triggers the workflow on every Git push.
- **`branches: [ master ]`**: Restricts execution to pushes made to the `master` branch.

> Only changes pushed to the `master` branch will trigger this deployment.

#### **`jobs:`**
The workflow defines a single job named `deploy`, responsible for building, transferring, and restarting the application on the VPS.

##### **`deploy`**
- **Purpose**: Build a Docker image, transfer it to the VPS, and restart the service.
- **`runs-on: ubuntu-latest`**: Executes on the latest stable Ubuntu virtual machine provided by GitHub Actions.

**Steps:**

1. **Checkout Code**  
   Fetches the repository code using `actions/checkout@v4`.

2. **Set up Docker Buildx**  
   Initializes Docker Buildx via `docker/setup-buildx-action@v3` to enable efficient image builds.

3. **Build Docker Image**  
   Builds a Docker image tagged with the unique Git commit SHA:  
   ```bash
   docker build -t chat:${{ github.sha }} .
   ```
   This ensures every deployment is traceable to a specific commit.

4. **Save Docker Image to tar**  
   Exports the built image into a portable archive:  
   ```bash
   docker save chat:${{ github.sha }} -o chat.tar
   ```

5. **Copy Artifacts to VPS**  
   Uses `appleboy/scp-action@v1.0.0` to securely transfer two files to the VPS:
   - `chat.tar` (the Docker image)
   - `docker-compose.yml` (service configuration)  
   Destination: `/opt/chat/`  
   Authentication uses secrets:
   - `VPS_HOST`
   - `VPS_USER`
   - `VPS_PRIVATE_KEY`

6. **Load Image and Restart Service on VPS**  
   Uses `appleboy/ssh-action@v1.0.3` to execute commands on the VPS:
   ```bash
   cd /opt/chat
   docker load -i chat.tar
   docker compose down
   docker compose up -d
   docker image prune -f
   ```
   This sequence:
   - Loads the new image into Docker
   - Stops the current stack
   - Starts the updated stack in detached mode
   - Cleans up unused Docker images


### **Security & Best Practices**

- **Secrets Management**:  
  Sensitive data (SSH key, host, username) is stored as GitHub Actions secrets—never in code.
- **Immutable Deployments**:  
  Each image is tagged with `github.sha`, ensuring reproducibility and avoiding `latest` ambiguity.
- **Idempotent Deployment**:  
  The workflow is safe to re-run; stopping and starting the stack has no side effects.
- **Minimal Cleanup**:  
  Only unused Docker images are pruned (`image prune`), avoiding unintended side effects on other services.

  
### **Requirements**

1. **On GitHub**:
   - Repository contains:
     - `Dockerfile`
     - `docker-compose.yml` (in root)
   - Secrets configured in **Settings → Secrets and variables → Actions**:
     - `VPS_HOST` (e.g., `192.0.2.1` or `example.com`)
     - `VPS_USER` (e.g., `deploy`)
     - `VPS_PRIVATE_KEY` (private key, **without password**)

2. **On VPS**:
   - Docker and Docker Compose installed
   - User (`VPS_USER`) has:
     - Write permissions to `/opt/chat/`
     - Membership in the `docker` group (to run Docker without `sudo`)


### **Summary**

This CD workflow ensures that every commit merged into `master` is:

-  **Automatically built** as a versioned Docker image  
-  **Securely transferred** to the production server  
-  **Instantly deployed** with zero downtime (if Compose is configured accordingly)  
-  **Traceable** to a specific Git commit  
