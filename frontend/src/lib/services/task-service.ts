import { PUBLIC_API_URL } from '$env/static/public';
import type { Task, TaskPayload } from '$lib/types/task';

export const TaskService = {
    async createTask(task: TaskPayload): Promise<Task> {
        const response = await fetch(`${PUBLIC_API_URL}/api/v1/tasks/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(task)
        });
        if (!response.ok) {
            throw new Error('Failed to create task');
        }
        return response.json();
    },

    async updateTask(taskId: number, task: TaskPayload): Promise<Task> {
        const response = await fetch(`${PUBLIC_API_URL}/api/v1/tasks/${taskId}/`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(task)
        });
        if (!response.ok) {
            throw new Error('Failed to update task');
        }
        return response.json();
    },

    async deleteTask(taskId: number): Promise<void> {
        const response = await fetch(`${PUBLIC_API_URL}/api/v1/tasks/${taskId}/`, {
            method: 'DELETE'
        });
        if (!response.ok) {
            throw new Error('Failed to delete task');
        }
    }
};