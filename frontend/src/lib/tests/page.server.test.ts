import { describe, expect, it, vi, beforeEach } from 'vitest';
import { load } from '../../routes/tasks/all/+page.server';
import type { Task } from '$lib/types/task';


vi.mock('$env/static/public', () => ({
	PUBLIC_API_URL: 'http://127.0.0.1:8000'
}));

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

describe('All Tasks Page Server Load Function', () => {
	it('fetches tasks and returns them', async () => {
		mockFetch.mockResolvedValue(
			new Response(JSON.stringify(mockTask), { status: 200 })
		);

		const result = await load({ fetch: mockFetch } as any);

		expect(mockFetch).toHaveBeenCalledWith('http://127.0.0.1:8000/api/v1/tasks/');
		expect(result).toEqual({ tasks: mockTask });
	});

	it('throws error when the API returns an error response', async () => {
		mockFetch.mockResolvedValue(
			new Response(null, { status: 500 })
		);

		await expect(load({ fetch: mockFetch } as any)).rejects.toThrow('Failed to fetch tasks');
	});
});
