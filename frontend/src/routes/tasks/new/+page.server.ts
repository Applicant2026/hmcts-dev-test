import { PUBLIC_API_URL } from '$env/static/public';
import type { PageServerLoad } from './$types';
import type { TaskStatus } from '$lib/types/task';

export const load: PageServerLoad = async ({ fetch }) => {
	const response = await fetch(`${PUBLIC_API_URL}/api/v1/task-statuses/`);

	if (!response.ok) {
		throw new Error('Failed to fetch task statuses');
	}

	const taskStatuses: TaskStatus[] = await response.json();

	return { taskStatuses };
};
