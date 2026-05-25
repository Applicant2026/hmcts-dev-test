import { describe, expect, it, vi, beforeEach } from 'vitest';
import { TaskService } from '../services/task-service';
import type { Task, TaskPayload } from '$lib/types/task';


vi.mock('$env/static/public', () => ({
	PUBLIC_API_URL: 'http://127.0.0.1:8000'
}));

const mockPayload: TaskPayload = {
	title: 'Test Task',
	description: 'This is a test task',
	status: 'TO_DO',
	due_date: '2026-06-01T09:00:00Z'
};

const mockTask: Task = {
	id: 1,
	title: 'Test Task',
	description: 'This is a test task',
	status: 'TO_DO',
	status_display: 'To Do',
	due_date: '2026-06-01T09:00:00Z',
	due_date_display: '1 Jun 2026 at 09:00',
	created_at: '2026-05-01T00:00:00Z',
	updated_at: '2026-05-01T00:00:00Z'
};

const mockFetch = vi.fn();
vi.stubGlobal('fetch', mockFetch);

beforeEach(() => {
	mockFetch.mockReset();
});

describe('Create Task', () => {
	it('successfully sends task data to API and returns the created task', async () => {
		mockFetch.mockResolvedValue(
			new Response(JSON.stringify(mockTask), { status: 201 })
		);

		const result = await TaskService.createTask(mockPayload);

		expect(mockFetch).toHaveBeenCalledWith('http://127.0.0.1:8000/api/v1/tasks/', {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify(mockPayload)
		});
		expect(result).toEqual(mockTask);
	});

	it('throws error when the API returns an error response', async () => {
		mockFetch.mockResolvedValue(
			new Response(JSON.stringify({ title: ['This field may not be blank.'] }), { status: 400 })
		);

		await expect(TaskService.createTask(mockPayload)).rejects.toThrow('Failed to create task');
	});
});

describe('Update Task', () => {
	it('successfully sends updated task data to API and returns the updated task', async () => {
		const updatedPayload = { ...mockPayload, status: 'IN_PROGRESS' };
		const updatedTask = { ...mockTask, status: 'IN_PROGRESS' };
		mockFetch.mockResolvedValue(
			new Response(JSON.stringify(updatedTask), { status: 200 })
		);

		const result = await TaskService.updateTask(mockTask.id, updatedPayload);

		expect(mockFetch).toHaveBeenCalledWith('http://127.0.0.1:8000/api/v1/tasks/1/', {
			method: 'PUT',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify(updatedPayload)
		});
		expect(result).toEqual(updatedTask);
	});

	it('throws error when the API returns an error response', async () => {
		mockFetch.mockResolvedValue(
			new Response(JSON.stringify({ detail: 'No Task matches the given query.' }), { status: 404 })
		);

		await expect(TaskService.updateTask(25, mockPayload)).rejects.toThrow('Failed to update task');
	});
});

describe('Delete Task', () => {
	it('successfully deletes a task', async () => {
		mockFetch.mockResolvedValue(new Response(null, { status: 204 }));

		await TaskService.deleteTask(1);

		expect(mockFetch).toHaveBeenCalledWith('http://127.0.0.1:8000/api/v1/tasks/1/', {
			method: 'DELETE'
		});
	});

	it('throws when the API returns an error response', async () => {
		mockFetch.mockResolvedValue(
			new Response(JSON.stringify({ detail: 'No Task matches the given query.' }), { status: 404 })
		);

		await expect(TaskService.deleteTask(25)).rejects.toThrow('Failed to delete task');
	});
});
