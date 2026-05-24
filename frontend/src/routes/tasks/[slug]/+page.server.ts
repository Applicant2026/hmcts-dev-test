import { PUBLIC_API_URL } from '$env/static/public';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ fetch, params }) => {
	const [taskRes, statusesRes] = await Promise.all([
		fetch(`${PUBLIC_API_URL}/api/v1/tasks/${params.slug}/`),
		fetch(`${PUBLIC_API_URL}/api/v1/task-statuses/`)
	]);

	if (!taskRes.ok) {
		throw new Error('Failed to fetch task details');
	}

	if (!statusesRes.ok) {
		throw new Error('Failed to fetch statuses');
	}

	const [task, taskStatuses] = await Promise.all([taskRes.json(), statusesRes.json()]);

	return {
		task: task,
		taskStatuses: taskStatuses
	};
};
