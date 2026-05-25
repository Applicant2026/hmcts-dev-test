import { PUBLIC_API_URL } from '$env/static/public';
import type { PageServerLoad } from './$types';
import type { Task, TaskStatus } from '$lib/types/task';

export const load: PageServerLoad = async ({ fetch, params }) => {
	const [taskRes, statusesRes] = await Promise.all([
		fetch(`${PUBLIC_API_URL}/api/v1/tasks/${params.slug}/`),
		fetch(`${PUBLIC_API_URL}/api/v1/task-statuses/`)
	]);

	if (!taskRes.ok) {
		throw new Error('Failed to fetch task details');
	}
	if (!statusesRes.ok) {
		throw new Error('Failed to fetch task statuses');
	}

	const task: Task = await taskRes.json();
	const taskStatuses: TaskStatus[] = await statusesRes.json();

	return { task, taskStatuses };
};
