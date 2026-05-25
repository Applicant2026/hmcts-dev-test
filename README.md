# HMCTS Task Manager

A full-stack task management application built with a Django REST Framework backend and a SvelteKit frontend styled with the GOV.UK Design System. It allows users to create, view, edit, and delete tasks, each with a title, description, status, and due date.

## Built With

* [Django](https://www.djangoproject.com/) - Backend web framework
* [Django REST Framework](https://www.django-rest-framework.org/) - REST API toolkit
* [SvelteKit](https://kit.svelte.dev/) - Frontend framework
* [GOV.UK Frontend](https://frontend.design-system.service.gov.uk/) - Design system
* [Vitest](https://vitest.dev/) - Frontend unit testing
* [uv](https://docs.astral.sh/uv/) - Python dependency management

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) — Python package and virtual environment manager
- Node.js 20+

```
# Verify your versions
python --version
uv --version
node --version
```

### Installing

Clone the repository:

```
git clone https://github.com/Applicant2026/hmcts-dev-test.git
cd hmcts-dev-test
```

Both the backend and frontend must be running simultaneously. Open two terminal windows.

**Backend**

Install Python dependencies and apply database migrations:

```
cd backend
uv sync
uv run python src/manage.py migrate
```

Create the environment file:

```
cp backend/src/.env.example backend/src/.env
```

Start the Django development server:

```
uv run python src/manage.py runserver
```

The API will be available at http://127.0.0.1:8000.

**Frontend**

Install Node dependencies:

```
cd frontend
npm install
```

Create the environment file:

```
echo "PUBLIC_API_URL=http://127.0.0.1:8000" > frontend/.env
```

Start the SvelteKit development server:

```
npm run dev
```

The application will be available at http://localhost:5173.

**Verify the setup**

With both servers running, open http://localhost:5173/tasks/all in your browser. You should see the task list page. To create your first task, click "Create New Task".

## Running the tests

### Backend tests

The backend uses Django's built-in test runner. Tests cover the `Task` model, serializer, and API viewset:

```
cd backend
uv run python src/manage.py test src
```

### Frontend tests

The frontend uses Vitest for unit testing. Tests cover the `TaskService` (create, update, delete) and the `tasks/all` page server load function:

```
cd frontend
npm test
```

### Coding style tests

**Frontend** — runs Prettier formatting checks and ESLint:

```
cd frontend
npm run lint
```

**Backend** — runs Ruff linting:

```
cd backend
uv run ruff check src
```
