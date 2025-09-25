# DocSync

Documentation synchronization service that keeps your docs in sync across GitHub, Notion, Confluence, and other platforms.

## Project Structure

```
DocSync/
├── backend/          # FastAPI backend service
├── frontend/         # Next.js frontend application
├── docker-compose.yml # Development environment setup
└── README.md
```

## Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd DocSync
   ```

2. **Set up environment variables**
   ```bash
   # Backend
   cp backend/.env.example backend/.env
   # Frontend
   cp frontend/.env.local.example frontend/.env.local
   ```

3. **Start the development environment**
   ```bash
   docker-compose up -d
   ```

4. **Access the applications**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

## Technology Stack

- **Backend**: FastAPI, PostgreSQL, Redis, SQLAlchemy
- **Frontend**: Next.js, TypeScript, Tailwind CSS, React Query
- **Infrastructure**: Docker, Docker Compose

## Development

See the individual README files in the `backend/` and `frontend/` directories for detailed setup instructions.
