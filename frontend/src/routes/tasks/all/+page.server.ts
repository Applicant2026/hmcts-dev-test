import { PUBLIC_API_URL } from '$env/static/public';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ fetch }) => {
	const res = await fetch(`${PUBLIC_API_URL}/api/v1/tasks/`);

	if (!res.ok) {
		throw new Error('Failed to fetch tasks');
	}

	const tasks = await res.json();

	return {
		tasks
	};
};
