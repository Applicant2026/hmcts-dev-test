import { PUBLIC_API_URL } from '$env/static/public';

export const TaskService = {
    async createTask(task: any) {
        const response = await fetch(`${PUBLIC_API_URL}/api/v1/tasks/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(task)
        });
        if (!response.ok) {
            const errorBody = await response.json().catch(() => null);
            throw new Error(`Failed to create task: ${JSON.stringify(errorBody)}`);
        }
        return response.json();
    },

    async deleteTask(taskId: number) {
        const response = await fetch(`${PUBLIC_API_URL}/api/v1/tasks/${taskId}/`, {
            method: 'DELETE'
        });
        if (!response.ok) {
            const errorBody = await response.json().catch(() => null);
            throw new Error(`Failed to delete task: ${JSON.stringify(errorBody)}`);
        }
    }
};