import { PUBLIC_API_URL } from '$env/static/public';
import type { PageServerLoad } from './$types';
import type { Task } from '$lib/types/task';

export const load: PageServerLoad = async ({ fetch }) => {
	const response = await fetch(`${PUBLIC_API_URL}/api/v1/tasks/`);

	if (!response.ok) {
		throw new Error('Failed to fetch tasks');
	}

	const tasks: Task[] = await response.json();

	return { tasks };
};
