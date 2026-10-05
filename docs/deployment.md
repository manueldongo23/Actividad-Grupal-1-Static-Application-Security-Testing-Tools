# Deployment Guide (Render)

1. **Create Repository**: Push the project to GitHub.
2. **Verify Actions**: Navigate to the "Actions" tab in your repo and ensure the CI and Security workflows complete successfully.
3. **Create Render Account**: Go to render.com.
4. **New Web Service**: Click "New" -> "Web Service".
5. **Connect GitHub**: Authenticate with GitHub and select your repository.
6. **Configuration**:
   - Environment: Python
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
7. **Deploy**: Click "Create Web Service".
8. **Public URL**: Once deployed, Render will provide a public URL (e.g., `https://secure-notes-xyz.onrender.com`).
